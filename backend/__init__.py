from flask import Flask
from flask_mysqldb import MySQL
from flask_cors import CORS
# from flask_session import Session
from backend.config import CONFIG


app = Flask(
	__name__,
	template_folder = '../frontend/templates',
	static_folder = '../frontend/templates/static'
)

# configure MySQL
app.config.update(CONFIG)

# initialize MySQL
mysql = MySQL(app)
# Session(app)
CORS(app)

# must import after create app 
from backend import routes
