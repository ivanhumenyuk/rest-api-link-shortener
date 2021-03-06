from flask import Flask
from db_config import Config
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from flask_restful import Api
from resources.link.controller import LinkShort, LinkRedirection

app = Flask(__name__)
app.config.from_object(Config)

api = Api(app)
api.add_resource(LinkShort, '/shorten')
api.add_resource(LinkRedirection, '/<short_hash>')

from db import db

db.init_app(app)
migrate = Migrate(app, db)

manager = Manager(app)
manager.add_command('db', MigrateCommand)

from resources.link.scheduler import scheduler

scheduler.start()
