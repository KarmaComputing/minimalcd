from tabnanny import verbose
from flask import Flask
from dotenv import load_dotenv
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate, upgrade
import os

load_dotenv(verbose=True)  # take environment variables from .env.

# See https://flask.palletsprojects.com/en/2.1.x/patterns/packages/#simple-packages
application = Flask(__name__)
application.config.update(os.environ)

db = SQLAlchemy(application)
migrate = Migrate(application, db)

with application.app_context():
    upgrade()  # upgrade database schema to latest version


class Principle(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    principle = db.Column(db.String(128))


import minimalcd.views
