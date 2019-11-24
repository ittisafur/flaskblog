from flaskblog import db
from flask import render_template, redirect, url_for
from flaskblog.Forms.forms import RegisterForm
from werkzeug.security import generate_password_hash
from flaskblog.Models.models import User


def RegisterController():
    form = RegisterForm()
    if form.validate_on_submit():
        password_hash = generate_password_hash(form.password.data)
        user = User(username=form.username.data, email=form.email.data, password=password_hash)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('home'))
    return render_template('register.html', form=form)
