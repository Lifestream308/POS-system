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
    category1 = db.Column(db.String(15), nullable=False)
    category2 = db.Column(db.String(15), nullable=False)
    token = db.Column(db.String, default='', unique=True)
    posts = db.relationship('Post', backref='author', lazy=True)

    def __init__(self, username, email, password, category1, category2, token=''):
        self.username = username
        self.email = email
        self.password = password
        self.category1 = category1
        self.category2 = category2
        self.token = self.set_token(20)

    def set_token(self, length): 
        return secrets.token_hex(length)

    def __repr__(self):
        return f"User('{self.username}', '{self.email}')"

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    price = db.Column(db.Integer, nullable=False)
    user_token = db.Column(db.String, db.ForeignKey('user.token'), nullable=False)

    def __init__(self, title, price, author, user_token):
        self.title = title
        self.price = price
        self.author = author
        self.user_token = user_token

    def __repr__(self):
        return f"Post('{self.title}', '{self.date_posted}')"

class UserSchema(ma.Schema):
    class Meta:
        fields = ['id', 'username', 'email']

user_schema = UserSchema()
users_schema = UserSchema(many=True)

class PostSchema(ma.Schema):
    class Meta:
        fields = ['id', 'title', 'price']

post_schema = PostSchema()
posts_schema = PostSchema(many=True)