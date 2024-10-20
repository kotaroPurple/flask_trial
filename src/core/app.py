
from pathlib import Path

from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__, template_folder='../templates/')

# register DB
db_path = Path(__file__).parents[1] / 'DB' / 'trial.db'
print('----')
print(db_path)
print()
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///" + str(db_path)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
