# !/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2018-10-21 15:26
# @Author  : Jackadam
# @Email   :
# @File    : 05.高阶函数+嵌套函数=装饰器.py
# @Software: PyCharm


print('------演示版------')
import time


# 高阶函数，作为装饰器的名字。
def timmer(func):
    # 嵌套一个函数，可以实现新的功能。
    def wapper(*args, **kwargs):
        start_time = time.time()
        # 把被装饰的函数的返回值拿出啦
        res = func(*args, **kwargs)
        end_time = time.time()
        print(end_time - start_time)
        # 返回返回值
        return res

    return wapper


@timmer
def test():
    time.sleep(1)
    print('in test')
    return 'hello'


print(test())

print('++++++分解一++++++')
# 用高阶函数增加一个功能，但是返回值出错了。
def test():
    time.sleep(1)
    print('in test')
    return 'hello'


def timmer(func):
    start_time = time.time()
    # 把被装饰的函数的返回值拿出啦
    func()
    end_time = time.time()
    print(end_time - start_time)


timmer(test)

print('++++++分解二++++++')
# 把被装饰的函数的返回值拿出啦

def test():
    time.sleep(1)
    print('in test')
    return 'hello'


def timmer(func):
    start_time = time.time()
    # 把被装饰的函数的返回值拿出啦
    res = func()
    end_time = time.time()
    print(end_time - start_time)
    return res


print(timmer(test))

print('++++++分解三++++++')


# 加入嵌套函数
def test():
    time.sleep(1)
    print('in test')
    return 'hello'


def timmer(func):
    def wapper():
        start_time = time.time()
        res = func()
        end_time = time.time()
        print(end_time - start_time)
        return res

    return wapper()


timmer(test)
print(timmer(test))

print('++++++分解四++++++')


# 覆盖原有函数，修正调用方式,由于还需要重新调用，所以返回函数名，而不返回结果了
def test():
    time.sleep(1)
    print('in test')
    return 'hello'


def timmer(func):
    def wapper():
        start_time = time.time()
        res = func()
        end_time = time.time()
        print(end_time - start_time)
        return res

    return wapper


test = timmer(test)
print(test())

print('++++++分解五++++++')


# 正常的装饰器调用

def timmer(func):
    def wapper():
        start_time = time.time()
        res = func()
        end_time = time.time()
        print(end_time - start_time)
        return res

    return wapper


@timmer
def test():
    time.sleep(1)
    print('in test')
    return 'hello'


test()


print('++++++分解六++++++')


# 再加一层，给装饰器传入参数。

def timmer(str):
    def add(func):
        def wapper():
            start_time = time.time()
            print(str)
            res = func()
            end_time = time.time()
            print(end_time - start_time)
            return res

        return wapper
    return add


@timmer(str='jack')
def test1():
    time.sleep(1)
    print('in test1')
    return 'hello'

@timmer(str='rose')
def test2():
    time.sleep(1)
    print('in test2')
    return 'hello'

test1()
test2()


print('++++++分解七++++++')


# 传入被装饰函数的参数

def timmer(str):
    def add(func):
        def wapper(*args,**kwargs):
            start_time = time.time()
            print(str)
            res = func(*args,**kwargs)
            end_time = time.time()
            print(end_time - start_time)
            return res

        return wapper
    return add


@timmer(str='jack')
def test1(int):
    time.sleep(int)
    print('in test1')
    return 'hello'

@timmer(str='rose')
def test2(int):
    time.sleep(int)
    print('in test2')
    return 'hello'

test1(1)
test2(2)