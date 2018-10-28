# !/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2018-10-21 15:25
# @Author  : Jackadam
# @Email   :
# @File    : 04.嵌套函数.py
# @Software: PyCharm

#嵌套函数
#在一个函数里面用def又声明一个函数，叫函数的嵌套。
def func1():
    print('in func1')
    def func2():
        print('in func2')
    func2()

func1()
