# !/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2018-08-23 21:03
# @Author  : Jackadam
# @Email   :jackadam@sina.com
# @File    : 04.多对一关系.py
# @Software: PyCharm
# !/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2018-08-14 18:54
# @Author  : Jackadam
# @Email   :jackadam@sina.com
# @File    : tree.py
# @Software: PyCharm
import sqlalchemy
from sqlalchemy import Table, Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import sessionmaker,backref

engine = create_engine('sqlite:///test3.db', encoding='utf-8')

Base = declarative_base()  # 生成orm基类


association_table = Table('association', Base.metadata,
    Column('Parent_ID', Integer, ForeignKey('parent.id')),
    Column('Child_ID', Integer, ForeignKey('child.id'))
)

class Parent(Base):
    __tablename__ = 'parent'
    id = Column(Integer, primary_key=True)
    name=Column(String(8))
    children = relationship(
        "Child",
        secondary=association_table,
        back_populates="parents")
    def __repr__(self):
        return 'name:%s' % self.name

class Child(Base):
    __tablename__ = 'child'
    id = Column(Integer, primary_key=True)
    name = Column(String(8))
    parents = relationship(
        "Parent",
        secondary=association_table,
        back_populates="children")
    def __repr__(self):
        return 'name:%s' % self.name
Base.metadata.create_all(engine)  # 创建表结构

Session_class = sessionmaker(bind=engine)  # 创建与数据库的会话session class ,注意,这里返回给session的是个class,不是实例
Session = Session_class()  # 生成session实例


# 基础结束

def add():
    # 插入开始
    child1 = Child(name='张大毛')
    Session.add(child1)
    child2 = Child(name='张二毛')
    Session.add(child2)
    child3 = Child(name='李天明')
    Session.add(child3)
    child4 = Child(name='李小明')
    Session.add(child4)
    Session.commit()
    parent1 = Parent(name='张三')
    Session.add(parent1)
    parent2 = Parent(name='张三媳妇')
    Session.add(parent2)
    parent3 = Parent(name='李明')
    Session.add(parent3)
    parent4 = Parent(name='李明媳妇')
    Session.add(parent4)
    Session.commit()



# 如果表不存在，则创建
check = Session.query(Parent).filter(Parent.name == '张三').first()
if check == None:
    add()
else:
    pass

# #关系的插入
# p1=Session.query(Parent).filter(Parent.name=='张三').first()
# p2=Session.query(Parent).filter(Parent.name=='张三媳妇').first()
# c1=Session.query(Child).filter(Child.name=='张大毛').first()
# c2=Session.query(Child).filter(Child.name=='张二毛').first()
#
# p3=Session.query(Parent).filter(Parent.name=='李明').first()
# p4=Session.query(Parent).filter(Parent.name=='李明媳妇').first()
# c3=Session.query(Child).filter(Child.name=='李天明').first()
# c4=Session.query(Child).filter(Child.name=='李小明').first()
#
# p1.children=[c1,c2]
# p2.children=[c1,c2]
#
# c3.parents=[p3,p4]
# c4.parents=[p3,p4]
# Session.add_all([p1,p2,])
# Session.commit()




# #查询通过孩子的名字找父母
# c1=Session.query(Child).filter(Child.name=='张大毛').first()
# print(c1.parents)
# #查询通过父母的名字找孩子
# p1=Session.query(Parent).filter(Parent.name=='李明媳妇').first()
# print(p1.children)

# #通过孩子删除一个父母
# c1=Session.query(Child).filter(Child.name=='张大毛').first()
# p1=Session.query(Parent).filter(Parent.name=='张三').first()
# c1.parents.remove(p1)


# #通过父母删除一个孩子
# c2=Session.query(Child).filter(Child.name=='李天明').first()
# p2=Session.query(Parent).filter(Parent.name=='李明').first()
# p2.children.remove(c2)
#
# Session.commit()
#
# #查询通过孩子的名字找父母
# c3=Session.query(Child).filter(Child.name=='张大毛').first()
# print(c3.parents)
# #查询通过父母的名字找孩子
# p3=Session.query(Parent).filter(Parent.name=='李明').first()
# print(p3.children)


#删除任意一个孩子或父母，则对应关系会自动删除。
#先看一下父母信息。
p1=Session.query(Parent).filter(Parent.name=='张三').first()
p2=Session.query(Parent).filter(Parent.name=='张三媳妇').first()
p3=Session.query(Parent).filter(Parent.name=='李明').first()
p4=Session.query(Parent).filter(Parent.name=='李明媳妇').first()

print(p1.children)
print(p2.children)
print(p3.children)
print(p4.children)

#删除一个child
c1=Session.query(Child).filter(Child.name=='张二毛').first()
Session.delete(c1)
Session.commit()

#再看一下父母信息。
p1=Session.query(Parent).filter(Parent.name=='张三').first()
p2=Session.query(Parent).filter(Parent.name=='张三媳妇').first()
p3=Session.query(Parent).filter(Parent.name=='李明').first()
p4=Session.query(Parent).filter(Parent.name=='李明媳妇').first()

print(p1.children)
print(p2.children)
print(p3.children)
print(p4.children)



