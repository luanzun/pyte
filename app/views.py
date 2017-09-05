from flask import render_template, flash, redirect
from app import app

@app.route('/sololearn/')
def sololearn():
    modules = [
        {
            'moduleid': '1',
            'name': '基础概念'
        },{
            'moduleid': '2',
            'name': '控制结构'
        }
    ]
    posts = [
        {
            'moduleid':'1',
            'lessonnumber': '1',
            'lessontitle': '什么是 Python?',
            'lessonurl': 'https://mp.weixin.qq.com/s/Bl_GR5J2nG5WbtpctkYlvw',
            'quizzes': '2'
        },
        {
            'moduleid':'1',
            'lessonnumber': '2',
            'lessontitle': '你的第一个项目',
            'lessonurl': 'https://mp.weixin.qq.com/s/u8btIkEx6EvGnnXZ3DBC9g',
            'quizzes': '2'
        },
        {
            'moduleid':'1',
            'lessonnumber': '3',
            'lessontitle': '简单操作',
            'lessonurl': 'http://mp.weixin.qq.com/s/JmHrjjvZdc9Qvc8KhdNQXg',
            'quizzes': '4'
        },
        {
            'moduleid':'1',
            'lessonnumber': '4',
            'lessontitle': '浮点数',
            'lessonurl': 'http://mp.weixin.qq.com/s/nYhfiDEsVhKpQAIdTzQ03g',
            'quizzes': '2'
        },
        {
            'moduleid': '1',
            'lessonnumber': '5',
            'lessontitle': '幂运算',
            'lessonurl': 'http://mp.weixin.qq.com/s/KeaJ2u2kU1b5Fg256GdcYQ',
            'quizzes': '2'
        },
        {
            'moduleid': '1',
            'lessonnumber': '6',
            'lessontitle': '字符串',
            'lessonurl': 'http://mp.weixin.qq.com/s/cquQKBsCZ-opjnVm3CiIkg',
            'quizzes': '3'
        },
        {
            'moduleid': '1',
            'lessonnumber': '7',
            'lessontitle': '简单的输入和输出',
            'lessonurl': 'http://mp.weixin.qq.com/s/dPtA2giDSsHOJxaLf7VkUA',
            'quizzes': '2'
        },
        {
            'moduleid': '1',
            'lessonnumber': '8',
            'lessontitle': '字符串操作',
            'lessonurl': 'https://mp.weixin.qq.com/s/TSHfIT_DjdvyC8AhntFqwQ',
            'quizzes': '3'
        },
        {
            'moduleid': '1',
            'lessonnumber': '9',
            'lessontitle': '类型转换',
            'lessonurl': 'http://mp.weixin.qq.com/s/V6jHITRHUos9MzYuKft-kA',
            'quizzes': '2'
        },
        {
            'moduleid': '1',
            'lessonnumber': '10',
            'lessontitle': '变量',
            'lessonurl': 'http://mp.weixin.qq.com/s/PloTNCi1U0haSwHE2vyHvQ',
            'quizzes': '4'
        },
        {
            'moduleid': '1',
            'lessonnumber': '11',
            'lessontitle': '赋值运算符',
            'lessonurl': 'http://mp.weixin.qq.com/s/69ND1knvCQxLEwXfd-Kgpg',
            'quizzes': '2'
        },
        {
            'moduleid': '1',
            'lessonnumber': '12',
            'lessontitle': '使用编辑器',
            'lessonurl': 'http://mp.weixin.qq.com/s/-HVSLmaH2iChJyQPWl0Hog',
            'quizzes': '1'
        },
        {
            'moduleid': '1',
            'lessonnumber': '13',
            'lessontitle': '单元测试',
            'lessonurl': 'http://mp.weixin.qq.com/s/5EvNqKHBbOVjMTk2KeTgiw',
            'quizzes': '5'
        },
        {
            'moduleid': '2',
            'lessonnumber': '14',
            'lessontitle': '布尔运算 & 比较',
            'lessonurl': 'http://mp.weixin.qq.com/s/_lHIf3YWR0hcwrKfwlduhg',
            'quizzes': '4'
        },
        {
            'moduleid': '2',
            'lessonnumber': '15',
            'lessontitle': 'if 语句',
            'lessonurl': 'http://mp.weixin.qq.com/s/lY70QOUKm0cvsN78DSRQdQ',
            'quizzes': '3'
        },
        {
            'moduleid': '2',
            'lessonnumber': '16',
            'lessontitle': 'else 语句',
            'lessonurl': 'http://mp.weixin.qq.com/s/SVG_rBI_oEyTcLDjjhBBIQ',
            'quizzes': '3'
        },
        {
            'moduleid': '2',
            'lessonnumber': '17',
            'lessontitle': 'Boolean Logic',
            'lessonurl': '',
            'quizzes': '3'
        },
        {
            'moduleid': '2',
            'lessonnumber': '18',
            'lessontitle': 'Operator Precedence',
            'lessonurl': '',
            'quizzes': '2'
        },
        {
            'moduleid': '2',
            'lessonnumber': '19',
            'lessontitle': 'while Loops',
            'lessonurl': '',
            'quizzes': '4'
        }
    ]
    return render_template("sololearn.html",
        title = 'SoloLearn Python 课程',
        coursetitle = 'SoloLearn Python 课程',
        modules = modules,
        posts = posts)

@app.route('/soloLearn/')
def soloLearn():
    return redirect('/sololearn/', 301)

@app.route('/sololearn/module-1-quiz/')
def quiz():
    options = [
        {
            'examid': '1',
            'content': '703'
        },{
            'examid': '1',
            'content': '10.0'
        },{
            'examid': '1',
            'content': '73.0'
        }
    ]
    posts = [
        {
            'examid': '1',
            'exam': '下面代码会输出什么内容？',
            'content':'>>> spam = "7"<br>>>> spam = spam + "0"<br>>>> eggs = int(spam) + 3<br>>>> print(float(eggs))',
            'type': 'radio',
            'answer': '73.0'
        }
    ]
    return render_template("quiz.html",
        title = '单元测试',
        options =options,
        posts = posts)


@app.route('/upload/', methods=['GET', 'POST'])
def upload():
    pass
if __name__ == '__main__':
    app.run(debug=True)

@app.route('/editor/')

def editor():
    return render_template("editor.html")

@app.route('/')
def index():
    user = { 'nickname': '朋友' } # fake user
    posts = [ # fake array of posts
        {
            'author': { 'nickname': 'John' },
            'body': '欢迎来到 Pyte！'
        },
        {
            'author': { 'nickname': 'Susan' },
            'body': '“祝贺你，你很幸运!'
        }

    ]
    return render_template("index.html",
        title = '首页',
        user = user,
        posts = posts)