#!flask/bin/python3.5
from app import db
import pymysql
pymysql.install_as_MySQLdb()

db.create_all()

from app import User
u = User(username='launzun', email='rsj@pyte.vip') 
db.session.add(u)                                     
db.session.commit()                      
users = User.query.all()                