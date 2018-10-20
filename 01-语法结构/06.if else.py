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
_username = input('username')
_password = input('password')

if username == _username and password == _password:
    print('ok')
else:
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