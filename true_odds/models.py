from . import db

class Game(db.Model):
    index = db.Column(db.Integer, primary_key=True, autoincrement=True)
    date = db.Column(db.String(20))
    A = db.Column(db.String(50))  # Adjust the type and length accordingly
    B = db.Column(db.String(50))
    A_win = db.Column(db.Float)
    B_win = db.Column(db.Float)
    ABS_diff = db.Column(db.Float)
    prediction = db.Column(db.String(50))