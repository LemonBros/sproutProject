#import flask
from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy 
from flask_migrate import Migrate

#import first party code
from config import Config

#initalize the application
app = Flask(__name__, static_folder='static')
login = LoginManager(app)
login.Login_view = 'home'
#setting up configuration for the Flask application 
app.config.from_object(Config)

#setting up the ORM model libraries 
db = SQLAlchemy(app)
migrate= Migrate(app, db)

from app import controller, routes, model