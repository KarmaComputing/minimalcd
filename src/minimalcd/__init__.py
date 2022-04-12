from tabnanny import verbose
from flask import Flask
from dotenv import load_dotenv
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

load_dotenv(verbose=True)  # take environment variables from .env.

# See https://flask.palletsprojects.com/en/2.1.x/patterns/packages/#simple-packages
application = Flask(__name__)

db = SQLAlchemy(application)
migrate = Migrate(application, db)

import minimalcd.views
