# !/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2018-10-20 21:44
# @Author  : Jackadam
# @Email   :
# @File    : app.py
# @Software: PyCharm
import os
from flask import Flask,render_template
from flask_script import Manager

app=Flask(__name__)
app.debug = True
manager=Manager(app)

@app.route('/')
def index():
    return render_template('index.html')


@manager.command
def dev():
    from livereload.server import Server
    server = Server(app.wsgi_app)
    server.watch('**/*.*')
    server.serve(open_url=True)

if __name__ == '__main__':
    # manager.run()
    app.run()