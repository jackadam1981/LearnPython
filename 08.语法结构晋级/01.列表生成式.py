# !/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2018-10-21 23:17
# @Author  : Jackadam
# @Email   :
# @File    : 01.列表生成式.py
# @Software: PyCharm
# 非常python
a = [1, 2, 3]
print(a)

a = []
for i in range(5):
    a.append(i)
print(a)

b=[i*3+2 for i in range(5)]
print(b)