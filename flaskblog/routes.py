from flask import render_template
from flaskblog import app
from flaskblog.Controllers.logincontroller import LoginController
from flaskblog.Controllers.registercontroller import RegisterController
from flask_user import roles_required, login_required


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/about')
def about():
    return render_template('layout.html')


@app.route('/contact')
def contact():
    return render_template('layout.html')


@app.route('/register', methods=['GET', 'POST'])
def register():
    return RegisterController()


@app.route('/login', methods=['GET', 'POST'])
def login():
    return LoginController()


@app.route('/logout')
def logout():
    return render_template('layout.html')


@app.route('/account')
def account():
    return render_template('layout.html')


@app.route('/createpost')
def create_post():
    return render_template('layout.html')
