
from datetime import datetime
from email.policy import default
from enum import unique
from system import db, login_manager, ma, bcrypt
from flask_login import UserMixin, current_user
import secrets

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(15), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)
    picture = db.Column(db.Integer, nullable=False)
    pokemon = db.Column(db.Integer, nullable=False)
    tagline = db.Column(db.String(100), nullable=False)
    token = db.Column(db.String, default='', unique=True)