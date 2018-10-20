#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2017/10/26 19:16
# @Author  : Jackadam
# @Email   : 
# @File    : 04.input.py
# @Software: PyCharm
#接收用户输入信息用input就可以了
#还有输入密码的，也就是隐藏的,pycharm中不好用，要到命令行去
import getpass
name = input('name:')
age = input('age:')
print( name ,age)
print('姓名:'  +name+'   年龄:'+age)
print('姓名：%s'%name)
print('姓名：%s  年龄：%s' % (name,age))
password = getpass.getpass('password：')
print(password)

