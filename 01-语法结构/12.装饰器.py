# !/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2018-07-29 22:28
# @Author  : Jackadam
# @Email   :jackadam@sina.com
# @File    : 02.Example.py
# @Software: PyCharm
#装饰器就是函数调用函数。

def func1(a,b):
    print(a,b)

func1(1,2)

def func2(a,b):
    func1(a,b)

func2(2,3)

