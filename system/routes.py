from flask import render_template, url_for, flash, redirect, request, abort, jsonify
from system import app, db, bcrypt
# from system.forms import RegistrationForm, AccountForm, LoginForm, PostForm
from system.models import User
from flask_login import login_user, current_user, logout_user, login_required

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html')