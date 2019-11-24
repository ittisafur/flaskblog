from flask import render_template, redirect, url_for
from flask_login import login_user
from flaskblog.Forms.forms import LoginForm
from flaskblog.Models.models import User
from werkzeug.security import check_password_hash


def LoginController():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user and check_password_hash(user.password, form.password.data):
            login_user(user)
            redirect(url_for('home'))
    return render_template('login.html', form=form)
