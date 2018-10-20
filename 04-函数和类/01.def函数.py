#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2017/11/16 19:24
# @Author  : Jackadam
# @Email   : 
# @File    : 01.def函数.py
# @Software: PyCharm
#函数就是实现一个特定功能的程序块
#下面这个函数实现了打印helloworld的功能
def print_hello():
    print('hello world!')
#这是调用方法
print_hello()
#下面的函数，实现了传入参数的功能
#在函数中可以嵌套使用其他函数
def print_name(name):
    print_hello()
    print('hello',name)
#带参数的调用方法
print_name('jack')