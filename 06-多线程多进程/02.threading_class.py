# !/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2017-12-24 19:24
# @Author  : Jackadam
# @Email   :
# @File    : 02.threading_class.py
# @Software: PyCharm
import threading
class MyThread(threading.Thread):
    def __init__(self,name):
        super(MyThread,self).__init__()
        self.n = name


    def run(self):
        print('sss',self.n)

t1 = MyThread('t1')
t2 = MyThread('t2')

t1.start()
t2.start()