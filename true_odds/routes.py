from . import app, db
import pandas as pd
import sqlite3
from flask import redirect, render_template, url_for
from true_odds.models import Game, Team 
from sqlalchemy import and_, or_
from datetime import datetime
import re
libraries = {'re': re}
today_date = datetime.now().date()

paths = {
        'game': 'all_season_preds',
        'team': '2023_stats'
         }

def load_data():
    conn = sqlite3.connect('./instance/predict.db')
    for db_name, path in paths.items():
        print(path)
        csv_path = f'./true_odds/static/Database/{path}.csv'
        data = pd.read_csv(csv_path)
        data.to_sql(name=db_name, con=conn, if_exists='replace', index=True)

@app.route('/', methods=['POST', 'GET'])
@app.route('/home')
def index():
    return render_template('index.html', **libraries)

@app.route('/pred')
def predict_page():
    data = Game.query.filter(Game.date >= today_date)
    cols = data.first().__table__.columns.keys()
    return render_template('pred.html', table=data, columns=cols, **libraries)

@app.route('/team/<teamname>')
def team_page(teamname):
    team_db = Game.query.filter(or_(Game.A == teamname, Game.B == teamname))
    stats_db = Team.query.filter(Team.team_name == teamname)
    cols = stats_db.first().__table__.columns.keys()
    return render_template('team_preds.html', name=teamname, table=team_db, columns=cols, stats=stats_db, **libraries)

@app.route('/day/<date>')
def date_page(date):
    date_db = Game.query.filter(Game.date == date)
    cols = date_db.first().__table__.columns.keys()
    return render_template('day_preds.html', day=date, table=date_db, columns=cols, **libraries)

@app.route('/duel/<team_a>_vs_<team_b>-<pred_idx>')
def duel_page(team_a, team_b, pred_idx):
    preds = Game.query.filter(Game.index == pred_idx)
    a_stats = Team.query.filter(Team.team_name == team_a)
    b_stats = Team.query.filter(Team.team_name == team_b)
    return render_template('duel_page.html', t1=a_stats, t2=b_stats, prediction=preds, **libraries)


@app.route('/about')
def about_page():
    return render_template('about.html', **libraries)