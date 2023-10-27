from . import app, db
import pandas as pd
import sqlite3
from flask import redirect, render_template, url_for
from true_odds.models import Game, Team 
from sqlalchemy import and_, or_
from datetime import datetime
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
    return render_template('index.html')

@app.route('/pred')
def predict_page():
    data = Game.query.filter(Game.date >= today_date)
    return render_template('pred.html', table=data)

@app.route('/team/<teamname>')
def team_page(teamname):
    team_db = Game.query.filter(or_(Game.A == teamname, Game.B == teamname))
    return render_template('team_preds.html', name=teamname, table=team_db)

@app.route('/day/<date>')
def date_page(date):
    date_db = Game.query.filter(Game.date == date)
    return render_template('team_preds.html', name=date, table=date_db)

@app.route('/stats/<teamname>')
def team_stats_page(teamname):
    team_db = Team.query.filter(Team.team_name == teamname)
    return render_template('team_bio.html', name=teamname, stats=team_db)

@app.route('/about')
def about_page():
    return render_template('about.html')