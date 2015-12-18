import os
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from flask import Flask, request, flash, url_for, redirect, \
     render_template, abort, send_from_directory
from utils import utils
import models
import requests
from flask.json import jsonify
import urllib
from SEAPI import SEAPI

try:
    import json
except ImportError:
    import simplejson as json

app = Flask(__name__)
utils.load_config(app)

from models import db

db.init_app(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/<path:resource>')
def serveStaticResource(resource):
    return send_from_directory('static/', resource)

@app.route("/test")
def test():
    return "<strong>It's Alive and pushed via Travis! Hooray! {}</strong>".format(app.config['CLIENT_SECRET'])
    
@app.route("/logintest")    
def login_test():
    payload = {
        'client_id': app.config['CLIENT_ID'],
        'scope': '',
        'redirect_uri': app.config['LOGIN_TOKEN'],
        'state': ''
    }
    redirect_url = "https://stackexchange.com/oauth?" + urllib.urlencode(payload)
    return redirect(redirect_url)
    
@app.route("/request_token")    
def request_token():
    payload = {
        'code': request.args.get('code'),
        'client_id': app.config['CLIENT_ID'],
        'client_secret': app.config['CLIENT_SECRET'],
        'redirect_uri': app.config['LOGIN_TOKEN']
    }
    r = requests.post('https://stackexchange.com/oauth/access_token', data=payload)
    # Convert response to dictionary, since it's text and not json we do this
    print
    print
    print r.text
    print
    print
    qs = r.text
    r = {x.split('=')[0]:x.split('=')[1] for x in qs.split("&")}
    
    SITE = SEAPI.SEAPI('stackoverflow', key=app.config['APP_KEY'], access_token=r['access_token'])
    user_data = SITE.fetch('/me', pagesize=100, filter='!23DDSb5p1Qj1Bj3trg(qA')
    vars = "Content-Type: text/plain\n\n"
    for key, value in user_data['items'][0].iteritems():
        vars += "{} => {} <br/>\n".format(key, value)
    return vars
    # r.text => access_token=gKNUw5P0JtW8L(LemYBmOw))&expires=86399
    # Use this to create a user. Use SEAPI to query /me end point
    # If user already exists, don't recreate, but do update the active flag
    # Don't need access key in user class
    # Redirect back to root with log in completed and this user object
    # How do I store client_secret outside of GitHub?
    # Use local MySQL for development!
    
@app.route("/login_success")    
def login_success():
    return request.query_string
    
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
    app.run(host=app.config['IP'], port=app.config['PORT'])
