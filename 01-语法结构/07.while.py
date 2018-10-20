#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2017/10/26 20:10
# @Author  : Jackadam
# @Email   : 
# @File    : 07.while.py
# @Software: PyCharm
count = 0
answer = 10

while True:
    print(count)
    count += 1
    guess = int(input('猜一个'))
    if guess == answer:
        print('ok')
        break
    elif guess > answer:
        print('猜大了')
    else:
        print('猜小了')

    if count ==10:
        break
print('第二个while')
count = 0
while count <3:
    count +=1
    guess = int(input('猜一个'))
    if guess == answer:
        print('ok')
        break
    elif guess < answer:
        print('猜小了')
    else:
        print('猜大了')
else:
    print('机会用完了')