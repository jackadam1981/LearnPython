# !/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2017-12-24 19:40
# @Author  : Jackadam
# @Email   :
# @File    : 03.threading_for.py
# @Software: PyCharm
'''
通过循环启动多个线程

'''
import threading
import time
def print_str(str):
    if str =='test1':
        time.sleep(5)
    elif str == 'test2':
        time.sleep(2)
    print('print',str)
    time.sleep(2)
    print('print', str)
# t1 = threading.Thread(target=print_str,args=('test1',))  #记得args后面的逗号。
# t2 = threading.Thread(target=print_str,args=('test2',))
for i in range(50):
    t = threading.Thread(target=print_str,args=('%s'%i,))
    t.start()
