# !/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2018-10-20 21:44
# @Author  : Jackadam
# @Email   :
# @File    : app.py
# @Software: PyCharm
import os
from flask import Flask, session, request
from flask_session import Session
from redis import Redis

app = Flask(__name__)
app.config['SESSION_TYPE'] = 'redis'   #session存储格式为redis
app.config['SESSION_REDIS'] = Redis(    #redis的服务器参数
    host='192.168.1.3',                 #服务器地址
    port=6379)                           #服务器端口

app.config['SESSION_USE_SIGNER'] = True   #是否强制加盐，混淆session
app.config['SECRET_KEY'] = os.urandom(24)  #如果加盐，那么必须设置的安全码，盐
app.config['SESSION_PERMANENT'] = False  #sessons是否长期有效，false，则关闭浏览器，session失效
app.config['PERMANENT_SESSION_LIFETIME'] = 3600   #session长期有效，则设定session生命周期，整数秒，默认大概不到3小时。
Session(app)


@app.route('/')
def default():
    return session.get('key', 'not set')

@app.route('/test/')
def test():
    session['key'] = 'test'
    return 'ok'

@app.route('/set/')
def set():
    arg = request.args.get('key')
    print(arg)
    session['key'] = arg
    return 'ok'


@app.route('/get/')
def get():
    return session.get('key', 'not set')


@app.route('/pop/')
def pop():
    session.pop('key')
    return session.get('key', 'not set')


@app.route('/clear/')
def clear():
    session.clear()
    return session.get('key', 'not set')


if __name__ == "__main__":
    app.run(debug=True)