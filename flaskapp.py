import os
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from flask import Flask, request, flash, url_for, redirect, \
     render_template, abort, send_from_directory

app = Flask(__name__)
app.config.from_pyfile('flaskapp.cfg')
db = SQLAlchemy(app)

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column('user_id', db.Integer, primary_key=True)
    name = db.Column(db.String(60))

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/<path:resource>')
def serveStaticResource(resource):
    return send_from_directory('static/', resource)

@app.route("/test")
def test():
    return "<strong>It's Alive and pushed via Travis! Hooray!</strong>"
    
@app.route("/envvars")
def print_environment_variables():
    vars = "Content-Type: text/plain\n\n"
    for key in os.environ.keys():
        vars += "{} => {} <br/>\n".format(key, os.environ[key])
    return vars
    
@app.route("/setup_db")
def setup_database():
    db.create_all()
    return "Works"


if __name__ == '__main__':
    app.run()
