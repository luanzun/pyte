import os
basedir = os.path.abspath(os.path.dirname(__file__))

# dialect+driver://username:password@host:port/database?charset=utf8
# 配置 sqlalchemy  数据库驱动://数据库用户名:密码@主机地址:端口/数据库?编码
SQLALCHEMY_DATABASE_URI = 'mysql://pyte.vip:pyte.vip@139.199.6.52:3306/pyte.vip?charset=utf8'
#设置这一项是每次请求结束后都会自动提交数据库中的变动

SQLALCHEMY_TRACK_MODIFICATIONS = True
SQLALCHEMY_COMMIT_ON_TEARDOWN = True