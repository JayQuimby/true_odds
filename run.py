from true_odds.routes import load_data
from true_odds import app, db

update_db = False

if __name__ == '__main__':
    if update_db:
        with app.app_context():
            db.create_all()
            load_data()

    app.run(debug=True, host='0.0.0.0', port=5000)