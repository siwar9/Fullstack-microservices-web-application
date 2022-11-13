from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
import os
from marketplace.config import DEV_DB, PROD_DB


app = Flask(__name__)
if os.environ.get('DEBUG') == '1':
    app.config["SQLALCHEMY_DATABASE_URI"] = DEV_DB
else:
    app.config["SQLALCHEMY_DATABASE_URI"] = PROD_DB
app.config['SECRET_KEY']='njdncveofhv478oer3hvjab5sxckha865z'

basedir= os.path.abspath(os.path.dirname(__file__))
ALLOWED_EXTENSIONS = {'jpg','JPG','png','PNG','gif','GIF','jpeg','JPEG'}
app.config['UPLOAD_FOLDER'] = os.path.join(basedir, 'static/images')

db = SQLAlchemy(app)
bcrypt = Bcrypt(app)

from marketplace.admin import routes
from marketplace.products import routes
from marketplace.carts import carts