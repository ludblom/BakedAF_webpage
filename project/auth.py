from flask import Blueprint, render_template, redirect, url_for, request, flash
from flask_login import login_user, logout_user, login_required
from werkzeug.security import generate_password_hash, check_password_hash
from .models import User
from . import db


auth = Blueprint('auth', __name__)


@auth.route('/login')
def login():
    return render_template('login.html')


@auth.route('/login', methods=['POST'])
def login_post():
    uname = request.form.get('uname')
    password = request.form.get('password')
    remember = True if request.form.get('remember') else False

    user = User.query.filter_by(uname=uname).first()

    if not user or not check_password_hash(user.password, password):
        flash('Denied! Check your login details.')
        return redirect(url_for('auth.login'))

    login_user(user, remember=remember)
    return redirect(url_for('main.profile'))


@auth.route('/signup')
def signup():
    return render_template('signup.html')


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('main.index'))


@auth.route('/signup', methods=['POST'])
def signup_post():
    uname = request.form.get('uname')
    password = request.form.get('password')

    user = User.query.filter_by(uname=uname).first()

    if user:
        flash('Username already taken')
        return redirect(url_for('auth.signup'))

    new_user = User(uname=uname, password=generate_password_hash(password, method='sha256'))

    # Add the new user
    db.session.add(new_user)
    db.session.commit()

    return redirect(url_for('auth.login'))
