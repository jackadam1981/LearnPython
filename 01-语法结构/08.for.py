#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2017/10/26 20:21
# @Author  : Jackadam
# @Email   : 
# @File    : for.py
# @Software: PyCharm
answer = 10
for i in range(3):
    guess = int(input('猜一个'))
    if  guess == answer:
        print('ok')
        break
    elif guess > answer:
        print('猜大了')
    else:
        print('猜小了')
else:
    print('机会用完了')

for i in range(10):
    print('loop',i)
print('---------')
for i in range(0,10,2):  #最后一个２是步进值
    print('loop',i)
print('---------')
for i in range(1,11):  #或者可以定义从１开始到１１，也是１０个循环
    print('loop',i)
print('---------')