from flask import request, render_template
from project.app import app

from project.models import *


@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/blank')
def blank():
    return render_template('blank.html')

@app.route('/buttons')
def buttons():
    return render_template('buttons.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/flot')
def flot():
    return render_template('flot.html')

@app.route('/morris')
def morris():
    return render_template('morris.html')

@app.route('/forms')
def forms():
    return render_template('forms.html')

@app.route('/notifications')
def notifications():
    return render_template('notifications.html')

@app.route('/grid')
def grid():
    return render_template('grid.html')

@app.route('/panels-wells')
def panels_wells():
    return render_template('panels-wells.html')

@app.route('/tables')
def tables():
    return render_template('tables.html')

@app.route('/icons')
def icons():
    return render_template('icons.html')

@app.route('/typography')
def typography():
    return render_template('typography.html')