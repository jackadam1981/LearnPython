#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2017/10/26 19:48
# @Author  : Jackadam
# @Email   : 
# @File    : if else.py
# @Software: PyCharm
#如果判断

username = 'jack'
password = '123'
_username = input('username：')
_password = input('password：')

#尝试登陆
if username == _username and password == _password:
    #登陆成功
    print('ok')
else:
    #登陆失败
    print('error')

answer = 10
guess = int(input('猜一个：'))
if answer == guess:
    print('猜对了')
elif answer >guess:
    print('猜小了')
else:
    print('猜大了')

guess = int(input('请输入10以下的一个数字'))
if guess <3:
    print('小于3')
elif guess <5:
    print('小于5')
elif guess <7 :
    print('小于7')
elif guess <9:
    print('小于9')
else:
    print('大于9')