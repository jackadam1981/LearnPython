#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2017/11/8 17:47
# @Author  : Jackadam
# @Email   : 
# @File    : 06.datetime.py
# @Software: PyCharm
# _*_coding:utf-8_*_
'''
python 中 time 有四种格式：
timestamp,float格式
时间戳（1970纪元后经过的浮点秒数）。基础时间数据
struct tuple(time.struct_time 或 datetime.datetime),
时间格式，可以计算，是解析过的数组
str
字符串格式，便于阅读
常用的：
float --> struct tuple: time.localtime(float)
float --> datetime: datetime.datetime.fromtimestamp(float)
struct time tuple --> float: time.mktime(struct time tuple)
struct time tuple --> str: time.strftime(format, struct time tuple)
struct time tuple --> datetime: datetime(*time_tuple[0:6])
datetime --> str: datetime.strftime(format, datetime)
datetime --> struct time tuple: datetime.timetuple()
str --> struct time tuple: time.strptime(str, format)
str --> datetime: datetime.strptime(str, format)
'''
import time, datetime

# time.time   返回当前时间的时间戳（1970纪元后经过的浮点秒数）（格林尼治时间）。
# 1分钟60秒，1小时3600秒，1天86400秒。
print('时间戳')
print(time.time())
print(type(time.time()))
print('----------')

# time.localtime() 作用是格式化时间戳为本地的时间（时间元组）。
# 不输入参数，返回本地时间，（本时区）
#  如果sec参数未输入，则以当前时间为转换标准。
print('时间元组')
print(time.localtime())
print(type(time.localtime()))
print('----------')

print('时间字符串')
print('1970-01-01 01:01:01')
print('19700101010101')
print('----------')
# 自定义一个时间戳，转换为时间元组
print('时间戳，转换为元组')
t = 0.0
t1 = time.localtime(t)
print('时间localtime,本地时间', t1)
t1 = time.gmtime(t)
print('时间gmtime,格林尼治时间', t1)
print(type(t1))
print('----------')

# time ctime()时间戳转字符串,无参数返回当前时间
print('时间戳转字符串，不适合中国用')
t = 0.0
t1 = time.ctime(t)
print(t1)
t2 = time.ctime()
print(t2)
print('----------')

# 适合中国用的时间戳转字符串
print('适合我们用的时间戳转字符串，分两步，1：时间戳转时间元组，2：时间元组转字符串')
t = 0.0
t1 = time.localtime(t)
t2 = time.strftime('%Y-%m-%d %H:%M:%S')
print(t2)
print('----------')

# time.mktime(t),把给定的元组（本地时间）转换为时间戳
# 自定义一个时间元组,9位年月日时分秒，后3位为0
print('元组，转为时间戳')
t = (1970, 1, 1, 8, 0, 0, 0, 0, 0)
secs = time.mktime(t)
print(secs)
print('----------')

# time.strftime()函数接收以时间元组，并返回以可读字符串表示的当地时间，
# 格式由参数format决定。无输入，则输出当前时间
print('元组，转为时间字符串')
t = (1970, 1, 1, 8, 0, 0, 0, 0, 0)
t1 = time.strftime('%Y-%m-%d %H:%M:%S', t)
t2 = time.strftime('%Y-%m-%d %H:%M:%S')
print(t1)
print(t2)
print('----------')

# time.strptime()函数根据指定的格式把一个时间字符串解析为时间元组。
print('字符串，转换为时间元组')
t = '1970-01-01'
t = time.strptime(t, "%Y-%m-%d")
print(t)
t = '19700101'
t = time.strptime(t, "%Y%m%d")
print(t)
print('----------')

print('字符串转时间戳，分两步')
string_2_struct = time.strptime("2016/05/22", "%Y/%m/%d")  # 将 日期字符串 转成 struct时间对象格式
print(string_2_struct)
struct_2_stamp = time.mktime(string_2_struct)  # 将struct时间对象转成时间戳
print(struct_2_stamp)
print('--------')

# # time.clock用于计算执行时间
# t0 = time.clock()  # 第一次调用time.clock，标记一个时间为0.0
# time.sleep(2)
# t1 = time.clock()  # 第二次调用，从第一个time.clock开始到现在的时间
# time.sleep(2)
# t2 = time.clock()  # 第三次调用，从第一个time.clock开始到现在的时间
# print(t0)
# print(t1)
# print(t2)
# print(t1 - t0)
# print(t2 - t1)
# print(t2 - t0)

# time.sleep(5)#以秒为单位暂停

#以下字符串方便用来存记录，
now_time = time.strftime('%Y-%m-%d %H:%M:%S')  # 20171123093804  当前时间
print(now_time)
print(type(now_time))  # 格式是字符串
print('----------')
now=str(datetime.datetime.now())
print(now)
print(type(now))    #格式是字符串 带毫秒的
print('----------')
today = time.strftime('%Y%m%d')  # 20171123 当前日期
print(today)
print(type(today))  # 格式是字符串
print('----------')