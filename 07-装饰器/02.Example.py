# !/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2018-10-21 15:15
# @Author  : Jackadam
# @Email   :
# @File    : 02.Example.py
# @Software: PyCharm

import time


def timer(func):
    def warpper(*args, **kwargs):
        t1 = time.time()
        func()
        t2 = time.time()
        print('执行时间为：',t2 - t1)
    return warpper


@timer
def test():
    time.sleep(2)
    print('in test')


if __name__ == '__main__':
    print('out test')
    test()
