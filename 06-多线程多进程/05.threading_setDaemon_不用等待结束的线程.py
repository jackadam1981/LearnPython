# !/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2017-12-24 20:20
# @Author  : Jackadam
# @Email   :
# @File    : 05.threading_setDaemon_不用等待结束的线程.py
# @Software: PyCharm
'''
第一个for循环，会等待所有线程结束，整个程序结束
第二个for循环，会直接退出，不等待线程结束
'''
import threading,time

def run(n,t):
    print('print-%s'%n)
    time.sleep(t)
    print('end-%s'%n)


# for i in range(20):
#     t = threading.Thread(target=run,args=(i,i))
#     t.start()
# print('test1_end')

for i in range(20):
    t = threading.Thread(target=run,args=(i,i))
    t.setDaemon(True)
    t.start()

print('test2_end')