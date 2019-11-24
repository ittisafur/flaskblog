from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_user import UserManager

from flaskblog.config import ConfigClass

app = Flask(__name__)
app.config.from_object(ConfigClass)
db = SQLAlchemy(app)

from flaskblog.Models.models import User, Role, UserRoles

user_manager = UserManager(app, db, User)

from flaskblog import routes
