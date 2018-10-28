# !/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2018-10-21 23:22
# @Author  : Jackadam
# @Email   :
# @File    : 02.列表生成器.py
# @Software: PyCharm
#生成式直接生成完整的列表
#生成器生成一个对象，每次调用后改变为下一个。

import time


# a = [i * 3.1415926 for i in range(50)]
# b = (i * 3.1415926 for i in range(50))
# print(a)
# print(b)


def timmer(func):
    def wapper(*args, **kwargs):
        start_time = time.time()
        res = func(*args, **kwargs)
        end_time = time.time()
        print('用时', end_time - start_time)
        return res

    return wapper


@timmer
# 生成式
def scs(int):
    return [i * 3.1415926 for i in range(int)]


@timmer
# 生成器
def scq(int):
    return (i * 3.1415926 for i in range(int))


# 通过计时装饰器，可以明显看出生成相同数量的生成式比生成器慢的多
scs(5000000)
scq(5000000)

# 打印出啦，生成式，是生成了完整的列表，而生成器是一个对象。
print(scs(20))
print(scq(20))

q=scq(50)

#打印对象，只会显示
print(q)

print(q.__next__())
print(q)
print(q.__next__())
print(q.__next__())
print(q.__next__())
print(q.__next__())
print(q.__next__())
print(q.__next__())
print(q.__next__())
print(q.__next__())