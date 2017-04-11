from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    user = { 'nickname': '爸爸' } # fake user
    posts = [ # fake array of posts
        {
            'author': { 'nickname': 'John' },
            'body': '在波特兰美好的一天!'
        },
        {
            'author': { 'nickname': 'Susan' },
            'body': '“复仇者联盟”电影太好看了!'
        }
    ]
    return render_template("index.html",
        title = '首页',
        user = user,
        posts = posts)