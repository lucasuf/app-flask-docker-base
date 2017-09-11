# app.py


from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from flask_migrate import Migrate,MigrateCommand
from flask_script import Manager

from project.config import BaseConfig


app = Flask(__name__)
app.config.from_object(BaseConfig)

# --- Flask-SQLAlchemy ---
db = SQLAlchemy(app)

# --- Flask-Migrate ---
migrate = Migrate(app, db)

# --- Flask-Script ---
manager = Manager(app)
manager.add_command('db', MigrateCommand)


