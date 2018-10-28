# !/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2018-10-21 2:09
# @Author  : Jackadam
# @Email   :
# @File    : test.py
# @Software: PyCharm
from flask import Flask
from tools.check import check_config,up_alembic


def create_app(str='pro'):
    global db
    global type
    # type = str   #这个可以使用手动指定运行环境
    type = check_config()   #这个是自动判断运行环境
    app = Flask(__name__)
    if str == 'home':
        from config import HomeConfig as Config
    elif str == 'pro':
        from config import ProductionConfig as Config
    elif str == 'dev':
        from config import DevelopmentConfig as Config
    elif str == 'test':
        from config import TestingConfig as Config
    else:
        from config import TestingConfig as Config
    app.config.from_object(Config)
    db = Config.DATABASE_URI
    up_alembic(db)
    return app



# 创建flask应用
app = (create_app(str='dev'))

@app.route('/')
def index():
    return type + '模式--数据库位置' + db


if __name__ == '__main__':

    app.run()
