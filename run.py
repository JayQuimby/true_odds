from routes import load_data
from utils import app, db

update_db = False
testing = True
if __name__ == '__main__':
    if update_db:
        with app.app_context():
            db.create_all()
            load_data()
    if testing:
        app.run(debug=True, host='0.0.0.0', port=5000)
    else:
        app.run(port=5000)