from flask import Flask
from models import db
from blueprints import create_blueprints

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://user:password@db:5432/delivery_app'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

with app.app_context():
    db.create_all()

create_blueprints(app)

@app.route("/")
def home():
    return "¡Bienvenido al backend de la Delivery App!"

if __name__ == "__main__":
    app.run(debug=True, port=5000, host="0.0.0.0")