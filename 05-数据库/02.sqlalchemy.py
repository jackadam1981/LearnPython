# !/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2017-12-31 0:12
# @Author  : Jackadam
# @Email   :
# @File    : 03.sqlalchemy.py
# @Software: PyCharm

from sqlalchemy_demo.settings import Session,User

# 插入开始
# user_obj = User(name="alex", password="alex3714")  # 生成你要创建的数据对象
# print(user_obj.name, user_obj.id)  # 此时还没创建对象呢，不信你打印一下id发现还是None
#
# Session.add(user_obj)  # 把要创建的数据对象添加到这个session里， 一会统一创建
# print(user_obj.name, user_obj.id)  # 此时也依然还没创建
#
# Session.commit()  # 现此才统一提交，创建数据
# 插入结束

# 查询开始
# my_user = Session.query(User).filter_by(name="alex").first()
my_user = Session.query(User).first()
print(my_user)
print(my_user.name, my_user.password)
# 查询结束

# 修改开始
# my_user = Session.query(User).filter_by(name="alex").first()
#
# my_user.name = "Alex Li"
#
# Session.commit()
# 修改技术

# 多条件查询
objs = Session.query(User).filter(User.id > 0).filter(User.id < 7).all()
# 多条件查询

# 统计
# Session.query(User).filter(User.name.like("Ra%")).count()
# 统计

# 分组
# from sqlalchemy import func
#
# print(Session.query(func.count(User.name), User.name).group_by(User.name).all())
# 分组

