# !/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2018-08-14 18:54
# @Author  : Jackadam
# @Email   :jackadam@sina.com
# @File    : tree.py
# @Software: PyCharm

#本例是说一个父母有多个孩子。
#可以通过父母查孩子。也能通过孩子查父母。

import sqlalchemy
from sqlalchemy import Table, Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import sessionmaker,backref

engine = create_engine('sqlite:///test1.db', encoding='utf-8')

Base = declarative_base()  # 生成orm基类


class Parent(Base):
    __tablename__ = 'parent'
    id = Column(Integer, primary_key=True)
    children = relationship("Child",)
    name = Column(String(20))
    # 在父表类中通过 relationship() 方法来引用子表的类集合
    def __repr__(self):
        return 'name:%s' % self.name

class Child(Base):
    __tablename__ = 'child'
    id = Column(Integer, primary_key=True)
    parent_id = Column(Integer, ForeignKey('parent.id'), nullable=False)#这里用表名，不是类名
    parent=relationship('Parent')
    name = Column(String(20))

    # 在子表类中通过 foreign key (外键)引用父表的参考字段
    def __repr__(self):
        return 'name:%s' % self.name

Base.metadata.create_all(engine)  # 创建表结构
Session_class = sessionmaker(bind=engine)  # 创建与数据库的会话session class ,注意,这里返回给session的是个class,不是实例
Session = Session_class()  # 生成session实例
# 基础结束

def add():
    # 插入开始
    parent1 = Parent(name='张三')
    Session.add(parent1)
    parent2 = Parent(name='李四')
    Session.add(parent2)
    parent3 = Parent(name='王五')
    Session.add(parent3)
    Session.commit()
    child1 = Child(name='张大毛', parent_id=parent1.id)
    Session.add(child1)
    child2 = Child(name='张二毛', parent_id=parent1.id)
    Session.add(child2)
    child3 = Child(name='李明', parent_id=parent2.id)
    Session.add(child3)
    child4 = Child(name='李小明', parent_id=parent2.id)
    Session.add(child4)
    Session.commit()

# # 类似连表，显示结构。
# print('查找--------------------------------')
# da = Session.query(Parent, Child).filter(Child.parent_id == Parent.id).filter(Child.name == '张大毛').all()
# print(da)
#
# # # 查找出孩子的信息
# db = Session.query(Parent).filter(Parent.name == '张三').first()
# print(db)
# print(db.name)
# print(db.children)
#
# #相当于，查过Parent，直接查出Child
# dc=Session.query(Parent).filter(Parent.name == '李四').first()
# dc.children=Session.query(Child).filter(Child.parent_id == dc.id).all()
# print(dc)
# print(dc.name)
# print(dc.children)


# add()
da=Session.query(Child).filter(Child.name=='李明').first()
print(da)
print(da.parent)
