from . import db

class Game(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    date = db.Column(db.String(20))
    A = db.Column(db.String(50), db.ForeignKey('team.team_name'))  # Adjust the type and length accordingly
    B = db.Column(db.String(50), db.ForeignKey('team.team_name'))
    A_win = db.Column(db.Float)
    B_win = db.Column(db.Float)
    ABS_diff = db.Column(db.Float)
    prediction = db.Column(db.String(50))
    #teams = db.Column(db.Integer, db.ForeignKey('team.team_name'))

class Team(db.Model):
    team_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    team_name = db.Column(db.String(20))
    games = db.relationship('Game', backref='team_name', lazy=True)

    