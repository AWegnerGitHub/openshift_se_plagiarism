import os
from datetime import datetime
from flask import Flask, request, flash, url_for, redirect, \
     render_template, abort, send_from_directory

app = Flask(__name__)
app.config.from_pyfile('flaskapp.cfg')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/<path:resource>')
def serveStaticResource(resource):
    return send_from_directory('static/', resource)

@app.route("/test")
def test():
    return "<strong>It's Alive and pushed via Travis!</strong>"
    
@app.route("/envvars")
def print_environment_variables():
    vars = "Content-Type: text/plain\n\n"
    for key in os.environ.keys():
        vars += "{} => {} <br/>\n".format(key, os.environ[key])
    return vars


if __name__ == '__main__':
    app.run()

db.create_all()