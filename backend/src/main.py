from flask import Flask
from models import db
from blueprints import create_blueprints
from flask_cors import CORS
from populate_db import check_if_db_populated, populate_db
import os

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv("DATABASE_URL")
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

CORS(app, resources={
    r"/*": {
        "origins": "*",
        "methods": ["GET", "POST", "PUT", "DELETE", "OPTIONS"],
        "allow_headers": ["Content-Type", "Authorization"],
        "supports_credentials": False
    }
})

with app.app_context():
    db.create_all()

    if not check_if_db_populated():
        populate_db()

create_blueprints(app)

@app.route("/")
def home():
    return "¡Bienvenido al backend de la Delivery App!"

if __name__ == "__main__":
    app.run(debug=True, port=5000, host="0.0.0.0")