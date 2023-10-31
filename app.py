# app.py

from config import ConfigSingleton
from waitress import serve

app = ConfigSingleton.get_app()
db = ConfigSingleton.get_db()

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    serve(app, host="0.0.0.0", port=5000)
