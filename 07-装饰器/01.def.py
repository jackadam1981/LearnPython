# !/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2018-10-21 12:41
# @Author  : Jackadam
# @Email   :
# @File    : 01.def.py
# @Software: PyCharm


# 可以在函数中调用函数

def foo():
    print('foo')
    bar()


def bar():
    print('bar')


foo()
