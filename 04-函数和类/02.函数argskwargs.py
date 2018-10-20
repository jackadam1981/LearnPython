# !/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2018-02-04 11:17
# @Author  : Jackadam
# @Email   :
# @File    : 02.函数argskwargs.py
# @Software: PyCharm
'''
例1：展示*args的用法，传入多个参数，不进行预先定义。
本例传入了3个参数。没有预先定义。在函数内自动生成元组（）
'''
def q1(*args):
    print('例1')
    print(args)
    print(type(args))
    print(args[0])
t1 = 123
t2 = 234
t3 = 345
q1(t1, t2, t3)
print('-----------------')
'''
例2，和例1一样，但是传入字符串，元组，列表，都会在函数内生成元组（）
注意引入参数时要有*号，
没有星号，函数把你传入的参数列表（元组，字符串）当作一个参数来处理。
有星号时，函数把你传入的参数列表（元组，字符串）当作多个参数来处理，在函数内生成元组（）
如最后一个调用q2(t3)
'''
def q2(*args):
    print('例2')
    print(args)
    print(type(args))
    print(args[0])
t1 = 123,234,345
q2(*t1)
t2 = (234,345,456)
q2(*t2)
t3=[345,456,567]
q2(*t3)
q2(t3)
print('-----------------')
'''
例3，本例展示使用**kwargs，传入字典,函数内同样还是字典。
'''
def q3(**kwargs):
    print('例3')
    print(kwargs)
    print(type(kwargs))
    print(kwargs['name1'])
di = {
    'name1': 'jack',
    'name2': 'rose',
}
q3(**di)
print('-----------------')
'''
例4：本例展示，函数定义时，可以同时使用*args，**kwargs来定义函数。
但是引用时，可以分开引用，只引用*args，或只引用**kwargs，暂时屏蔽函数内对元组和字典的使用，避免报错。
'''
def q4(*args,**kwargs):
    print('例4')
    print(args)
    # print(args[0])
    print(kwargs)
    # print(kwargs.get('name1'))
t1 = 123,234,345
di = {
    'name1': 'jack',
    'name2': 'rose',
}
q4(*t1)
print('---')
q4(**di)
print('-----------------')
'''
例5，本例展示同时定义*args,**kwargs,并且同时使用。
'''
def q5(*args,**kwargs):
    print('例5')
    print(args)
    print(args[0])
    print(kwargs)
    print(kwargs.get('name1'))
t1 = 123,234,345
di = {
    'name1': 'jack',
    'name2': 'rose',
}
q5(*t1,**di)
print('-----------------')
'''
例6，本例展示把*args，作为多余的参数传入函数，也是看代码经常看到的。
'''
def q6(t1,t2,*args):
    print('例6')
    print(t1)
    print(t2)
    print(args)
    print(args[0])
t1 = 123,234,345
q6('t123','t234',*t1)
print('-----------------')
'''
例7，本例展示把**kwargs，作为多余的参数传入函数，也是看代码经常看到的。
'''
def q7(k1,k2,**kwargs):
    print('例7')
    print(k1)
    print(k2)
    print(kwargs)
    print(kwargs.get('name1'))
    pass
di = {
        'name1': 'jack',
        'name2': 'rose',
}
q7(k1='t123',k2='t234',**di)
print('-----------------')
'''
例8，本例展示把*args,**kwargs共同使用，作为多余的参数传入函数，也是看代码经常看到的。
除函数定义的k1,k2,又在引用时，加入了  't345',k3=1,
结果
t123   （k1）
t234    (k2)
('t345', 123, 234, 345) (args)
{'k3': 1, 'k4': 2, 'name1': 'jack', 'name2': 'rose'}     (kwargs)
jack  kwargs['name1']
'''
def q8(k1,k2,*args,**kwargs):
    print('例8'    )
    print(k1)
    print(k2)
    print(args)
    print(kwargs)
    print(kwargs.get('name1'))
    pass
t1 = 123,234,345
di = {
        'name1': 'jack',
        'name2': 'rose',
}
q8('t123','t234','t345',k3=1,k4=2,*t1,**di)
print('-----------------')