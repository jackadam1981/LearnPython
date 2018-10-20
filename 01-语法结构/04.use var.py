#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2017/10/26 19:52
# @Author  : Jackadam
# @Email   : 
# @File    : 06.use var.py
# @Software: PyCharm
#不建议用加号，建议用.format

name = 'jack'
age = 18
print( name ,age)
print('姓名:',name,'年龄:',age)
print('姓名:'  +name+'   年龄:'+str(age))
print('姓名：%s'%name)
print('姓名：%s  年龄：%i' % (name,age))

print('姓名：{_name}  年龄：{_age}'.format(_name=name,
                                   _age=age))
print('姓名：{0}  年龄：{1}'.format(name,age))

