from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.script import Manager
from flask.ext.migrate import Migrate, MigrateCommand
from utils import utils
import models

app = Flask(__name__)
utils.load_config(app)
models.db.init_app(app)

migrate = Migrate(app, models.db)
manager = Manager(app)
manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()