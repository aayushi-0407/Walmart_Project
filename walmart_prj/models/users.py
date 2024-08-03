from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt

db = SQLAlchemy()
bcrypt = Bcrypt()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)
    height = db.Column(db.Float, nullable=True, default=0.0)
    weight = db.Column(db.Float, nullable=True, default=0.0)

    def __init__(self, username, password, height=0.0, weight=0.0):
        self.username = username
        self.password_hash = bcrypt.generate_password_hash(password).decode('utf-8')
        self.height = height
        self.weight = weight

    def check_password(self, password):
        return bcrypt.check_password_hash(self.password_hash, password)
