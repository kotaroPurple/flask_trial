
# import os
from flask import Flask
# from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__, template_folder='../templates/')
# base_dir = os.path.dirname(__file__)
# app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///" + os.path.join(base_dir, "CRM.db")
# db = SQLAlchemy(app)
