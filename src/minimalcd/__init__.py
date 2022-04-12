from flask import Flask

# See https://flask.palletsprojects.com/en/2.1.x/patterns/packages/#simple-packages

application = Flask(__name__)

import minimalcd.views
