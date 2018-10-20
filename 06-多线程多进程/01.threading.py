# !/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2017-12-24 18:03
# @Author  : Jackadam
# @Email   :
# @File    : 01.threading.py
# @Software: PyCharm
import threading
import time
def print_str(str):
    if str =='test1':
        time.sleep(5)
    elif str == 'test2':
        time.sleep(2)
    print('print',str)

t1 = threading.Thread(target=print_str,args=('test1',))  #记得args后面的逗号。
t2 = threading.Thread(target=print_str,args=('test2',))

print_str('test1')
print_str('test2')
# t1.start()
# t2.start()

'''
如果用
print_str('test1')
print_str('test2')
则先输出test1，后输出test2，两个函数顺序执行。
如果用
t1.start()
t2.start()
则先输出test2，后输出test1.两个函数是同时开始执行，因为t2是执行print_str('test2')，
在函数内部只等待2秒，所以先输出。
'''