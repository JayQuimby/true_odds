from . import app, db
import pandas as pd
from flask import redirect, render_template, url_for
from true_odds.models import Game
from sqlalchemy import and_, or_
from datetime import datetime
today_date = datetime.now().date()

def load_data():
    csv_path = './true_odds/static/Database/all_season_preds.csv'
    data = pd.read_csv(csv_path)
    data.to_sql(name='game', con=db.engine, if_exists='replace', index=True)

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

@app.route('/about')
def about_page():
    return render_template('about.html')