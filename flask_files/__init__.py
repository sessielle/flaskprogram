from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SECRET_KEY'] = 'thisisflaskapplication'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database/flask.db'


db = SQLAlchemy(app)

from flask_files import flask_app
