import os
from flask import Flask
from flask_session import Session
from models.users import db, bcrypt
from resources.auth import auth_bp
from resources.health import health_bp
def generate_secret_key():
    return os.urandom(24)

app = Flask(__name__)
app.config['SECRET_KEY'] = generate_secret_key()
app.config['SESSION_TYPE'] = 'filesystem'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
Session(app)

db.init_app(app)
bcrypt.init_app(app)

# Register blueprints
app.register_blueprint(auth_bp)
app.register_blueprint(health_bp)

with app.app_context():
    db.create_all()
if __name__ == '__main__':
    app.run(debug=True)
