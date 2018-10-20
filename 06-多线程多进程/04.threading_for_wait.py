# !/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2017-12-24 20:06
# @Author  : Jackadam
# @Email   :
# @File    : 04.threading_for_wait.py
# @Software: PyCharm
'''
python中
线程等待用join
'''
import threading,time

def run(n,t):
    print('print-%s'%n)
    time.sleep(t)
    print('end-%s'%n)

t_line=[]
for i in range(20):
    t = threading.Thread(target=run,args=(i,i))
    t.start()
    t_line.append(t)
for j in t_line:
    j.join()
print('all_end')