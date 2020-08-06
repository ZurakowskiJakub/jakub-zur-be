from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from util import cPrint

app = Flask(__name__)
app.config.from_object('env_config.Dev')

db = SQLAlchemy(app)
