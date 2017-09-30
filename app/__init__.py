from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap
app = Flask(__name__)
app.config.from_object('config')

#数据库
app.config['SECRET_KEY'] = 'Thisissuooisedtobesecret!'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://testuser:testuser521@localhost:3306/test'
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN']=True
bootstrap = Bootstrap(app)
db = SQLAlchemy(app)
from app import views