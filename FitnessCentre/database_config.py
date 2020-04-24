import os
from flask import Flask
from flask_sqlalchemy  import SQLAlchemy

app = Flask(__name__)
base_dir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(base_dir, 'database.db')
app.config['SECRET_KEY'] = 'secret'
db = SQLAlchemy(app)