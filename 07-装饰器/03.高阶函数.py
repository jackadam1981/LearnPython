# !/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2018-10-21 15:25
# @Author  : Jackadam
# @Email   :
# @File    : 03.高阶函数.py
# @Software: PyCharm
'''
高阶函数：
1.把一个函数名当作参数，传入另一个函数。
    可以在不改变函数的情况下，改变函数的运行方式，为其添加功能。
2.返回值中包含函数名

满足上列条件之一，即为高阶函数
'''
import time


# 普通函数
def func1():
    time.sleep(1)
    print('in func1')


# 高阶函数
def func2(func):
    time.sleep(1)
    func()
    print('in func2')


# 调用的时候，注意使用的是函数名，不带（）
func2(func1)
# 便于理解：
# 仅用函数名，不带括号，则是内存地址。
print(func1)
# 传递函数名，实际是传递内存地址。
# 在内存地址上加（）就是运行这个函数内容
func3 = func1
func3()

print('--------------------------------')

#返回函数名（既函数内存地址）
def func4(func):
    print('in func4')
    return func

print(func4(func1))

#假设我们覆盖func,那么就可以在不改变原函数的调用方式的情况下，给函数添加功能
print('覆盖func')
func1=func4(func1)

func1()
