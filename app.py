from flask import Flask, redirect, render_template, url_for
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import and_, or_
import pandas as pd

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']= 'sqlite:///predict.db'
db = SQLAlchemy(app)

class Game(db.Model):
    index = db.Column(db.Integer, primary_key=True, autoincrement=True)
    date = db.Column(db.String(20))
    A = db.Column(db.String(50))  # Adjust the type and length accordingly
    B = db.Column(db.String(50))
    A_win = db.Column(db.Float)
    B_win = db.Column(db.Float)
    ABS_diff = db.Column(db.Float)
    prediction = db.Column(db.String(50))

def load_data():
    csv_path = './static/Database/all_season_preds.csv'
    data = pd.read_csv(csv_path)
    data.to_sql(name='game', con=db.engine, if_exists='replace', index=True)

@app.route('/', methods=['POST', 'GET'])
@app.route('/home')
def index():
    return render_template('index.html')

@app.route('/pred')
def predict_page():
    data = Game.query.all()
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

if __name__ == '__main__':
    with app.app_context():
        #db.create_all()
        load_data()

    app.run(debug=True, host='0.0.0.0', port=5000)