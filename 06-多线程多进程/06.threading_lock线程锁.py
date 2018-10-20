# !/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2017-12-24 21:04
# @Author  : Jackadam
# @Email   :
# @File    : 06.threading_lock线程锁.py
# @Software: PyCharm
import threading
import time
lock = threading.Lock()
num = 0
def run (n):
    global num
    num = num + 1
t_jobs=[]
for i in range(50):
    print(i)
    t = threading.Thread(target=run,args=(i,))
    t.start()
    t_jobs.append(t)
for j in t_jobs:
    j.join()
print(num)





# def run(n):
#     lock.acquire()
#     global num
#     num +=1
#     lock.release()
# lock = threading.Lock()
# num = 0
# t_objs = [] #存线程实例
# for i in range(50):
#     t = threading.Thread(target=run,args=("t-%s" %i ,))
#     t.start()
#     t_objs.append(t) #为了不阻塞后面线程的启动，不在这里join，先放到一个列表里
# for t in t_objs: #循环线程实例列表，等待所有线程执行完毕
#     t.join()
# print("----------all threads has finished...",threading.current_thread(),threading.active_count())
# print("num:",num)