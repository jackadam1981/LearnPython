# !/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2018-08-23 21:03
# @Author  : Jackadam
# @Email   :jackadam@sina.com
# @File    : 04.多对一关系.py
# @Software: PyCharm
#本例是计划生育，一对夫妻只能有一个孩子。
#这种数据结构我用在记录类型。

import sqlalchemy
from sqlalchemy import Table, Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import sessionmaker,backref

engine = create_engine('sqlite:///test2.db', encoding='utf-8')

Base = declarative_base()  # 生成orm基类


class Parent(Base):
    __tablename__ = 'parent'
    id = Column(Integer, primary_key=True)
    name=Column(String(16))
    child_id = Column(Integer, ForeignKey('child.id'))
    child = relationship("Child", back_populates="parents")

class Child(Base):
    __tablename__ = 'child'
    id = Column(Integer, primary_key=True)
    name = Column(String(16))
    parents = relationship("Parent", back_populates="child")

Base.metadata.create_all(engine)  # 创建表结构
Session_class = sessionmaker(bind=engine)  # 创建与数据库的会话session class ,注意,这里返回给session的是个class,不是实例
Session = Session_class()  # 生成session实例


# 基础结束

def add():
    # 插入开始
    child1 = Child(name='张大毛')
    Session.add(child1)
    child3 = Child(name='李明')
    Session.add(child3)
    Session.commit()
    parent1 = Parent(name='张三',child_id=child1.id)
    Session.add(parent1)
    parent2 = Parent(name='张三媳妇',child_id=child1.id)
    Session.add(parent2)
    parent3 = Parent(name='李六',child_id=child3.id)
    Session.add(parent3)
    Session.commit()

# add()

#查询,通过孩子查父母
da=Session.query(Child).filter(Child.name=='张大毛').first()
print(da.parents)
for i in da.parents:
    print(i.name)

#查询，通过父母查孩子
db=Session.query(Parent).filter(Parent.name=='张三').first()
print(db)
print(db.child.name)





