# !/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2017-12-30 10:24
# @Author  : Jackadam
# @Email   :
# @File    : config.py
# @Software: PyCharm

import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///test.db', encoding='utf-8')

Base = declarative_base()  # 生成orm基类


class User(Base):
    __tablename__ = 'user'  # 表名
    id = Column(Integer, primary_key=True)
    name = Column(String(32))
    password = Column(String
(64))


Base.metadata.create_all(engine)  # 创建表结构

Session_class = sessionmaker(bind=engine)  # 创建与数据库的会话session class ,注意,这里返回给session的是个class,不是实例
Session = Session_class()  # 生成session实例