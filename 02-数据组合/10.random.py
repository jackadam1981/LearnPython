#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2017/11/8 17:49
# @Author  : Jackadam
# @Email   : 
# @File    : 05.print(py
# @Software: PyCharm
import random
from random import random, uniform, randint, randrange, choice, sample, shuffle

list = ['jack', 'rose', 'tom', 'jerry']
print(random())  # 随机小数 0.0 <= x < 1.0
print(uniform(1, 10))  # 随机小数 x, 1.0 <= x < 10.0
print(randint(1, 10))  # 随机整数 1 to 10, endpoints included
print(randrange(0, 101, 2))  # 随机0-101，步进2，也就是偶数
print(randrange(0, 101, 5))  # 随机0-101，步进5，也就是5的倍数
print(choice('abcdefghij'))  # 随机字符串中的一个字符
items = [1, 2, 3, 4, 5, 6, 7]
print(items)
shuffle(items)  # 重新随机排序
print(items)
print(sample([1, 2, 3, 4, 5], 3))  # 随机选3个
