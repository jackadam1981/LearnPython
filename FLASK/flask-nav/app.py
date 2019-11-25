'''
动态更新导航栏
'''
import os
from flask import Flask, render_template, session
from flask_nav import Nav
from flask_nav.elements import Navbar, View
from flask_bootstrap import Bootstrap

nav = Nav()

app = Flask(__name__)
app.config['SECRET_KEY'] = os.urandom(24)
Bootstrap(app)
nav.init_app(app)


@nav.navigation()
def top_nav():
    '''
    动态生成导航栏
    :return:
    '''
    items = [View('Home', 'index'), View('Shopping Area', 'index')]
    #基础导航栏
    # 如果有session信息，且是login设置的session，则在导航增加一个导航选项。
    if session.get('username') == 'xxx':
        items.append(View('Secret Shop', 'secret'))

    return Navbar('', *items)


@app.route('/')
def index():
    '''
    默认首页
    :return:
    '''
    return render_template('index.html')


@app.route('/login/')
def login():
    '''
    默认登陆页，简单设置一个session
    :return:
    '''
    session['username'] = 'xxx'
    return render_template('index.html')


@app.route('/logout/')
def logout():
    '''
    简单登出页，清除session
    :return:
    '''
    session.clear()
    return render_template('index.html')


@app.route('/_secret/')
def secret():
    '''
    简单加密页，仅作了导航菜单隐藏
    :return:
    '''
    return 'You found the secret shop!'


if __name__ == '__main__':
    app.run(debug=True)
