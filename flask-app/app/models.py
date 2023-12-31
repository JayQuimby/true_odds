from . import db

class Game(db.Model):
    index = db.Column(db.Integer(), primary_key=True, autoincrement=True)
    date = db.Column(db.String(20))
    A = db.Column(db.String(30))  # Adjust the type and length accordingly
    B = db.Column(db.String(30))
    A_win = db.Column(db.Float)
    B_win = db.Column(db.Float)
    ABS_diff = db.Column(db.Float)
    prediction = db.Column(db.String(30))

class Team(db.Model):
    index = db.Column(db.Integer(), primary_key=True, autoincrement=True)
    team_name = db.Column(db.String(30))
    pass_completion = db.Column(db.Float)
    pass_attempts = db.Column(db.Float)
    pass_completion_percent	= db.Column(db.Float)
    pass_yards = db.Column(db.Float)
    pass_td = db.Column(db.Float)
    rush_attempt = db.Column(db.Float)
    rush_yards = db.Column(db.Float)
    avg_rush_yard = db.Column(db.Float)
    rush_td = db.Column(db.Float)
    num_plays = db.Column(db.Float)
    total_yard = db.Column(db.Float)
    yard_per_play = db.Column(db.Float)
    pass_first_down = db.Column(db.Float)
    rush_first_down = db.Column(db.Float)
    penalty_first = db.Column(db.Float)
    first_downs = db.Column(db.Float)
    penalty = db.Column(db.Float)
    penalty_yards = db.Column(db.Float)
    lost_fumble = db.Column(db.Float)
    interceptions = db.Column(db.Float)
    turnovers = db.Column(db.Float)
    SRS = db.Column(db.Float)
    SOS = db.Column(db.Float)
    de_pass_completion = db.Column(db.Float)
    de_pass_attempts = db.Column(db.Float)
    de_pass_completion_percent = db.Column(db.Float)
    de_pass_yards = db.Column(db.Float)
    de_pass_td = db.Column(db.Float)
    de_rush_attempt = db.Column(db.Float)
    de_rush_yards = db.Column(db.Float)
    de_avg_rush_yard = db.Column(db.Float)
    de_rush_td = db.Column(db.Float)
    de_num_plays = db.Column(db.Float)
    de_total_yard = db.Column(db.Float)
    de_yard_per_play = db.Column(db.Float)
    de_pass_first_down = db.Column(db.Float)
    de_rush_first_down = db.Column(db.Float)
    de_penalty_first = db.Column(db.Float)
    de_first_downs = db.Column(db.Float)
    de_penalty = db.Column(db.Float)
    de_penalty_yards = db.Column(db.Float)
    de_lost_fumble = db.Column(db.Float)
    de_interceptions = db.Column(db.Float)
    de_turnovers = db.Column(db.Float)


    