from flask import Flask
from db_config import Configuration
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api


app = Flask(__name__)
api = Api(app)

app.config.from_object(Configuration)
db = SQLAlchemy(app)

