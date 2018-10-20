# !/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2017/12/13 15:23
# @Author  : Jackadam
# @Email   :
# @File    : 07.date.py.py
# @Software: PyCharm
#时间戳是通用的。
import time,datetime
#当前时间：
print(datetime.datetime.now())#2017-12-13 15:25:28.892519  带毫秒的当前时间字符串
print(type(datetime.datetime.now()))#格式是datetime.datetime,不能直接写数据库，文件记录，需要str转换
now = str(datetime.datetime.now())
print(now)
print(now[:10])
print(type(now))
print('--------')

#时间戳转datetime
t=time.time()  #获取当前时间戳
print(type(t))
print(t)
t=datetime.datetime.fromtimestamp(t) #把时间戳转为datetime
print(type(t))
print(t)
print(type(t.date()))#datetime的日期数据
#datetime转换时间戳
dtime = datetime.datetime.now()
ans_time = time.mktime(dtime.timetuple())
print(ans_time)
print('--------')

#自定义一个时间,最少定义3位，最多定义7位，顺序是年，月，日，时，分，秒，毫秒
d1 = datetime.datetime(1970,1,1,0,0,0,1)
print(d1)
print(type(d1))
print('--------')


# #时间加减

print(datetime.datetime.now())  # 返回 2016-08-19 12:47:03.941925
print(datetime.date.fromtimestamp(time.time()))  # 时间戳直接转成日期格式 2016-08-19
print(datetime.datetime.now())
print(datetime.datetime.now() + datetime.timedelta(3))  # 当前时间+3天
print(datetime.datetime.now() + datetime.timedelta(-3))  # 当前时间-3天
print(datetime.datetime.now() + datetime.timedelta(hours=3))  # 当前时间+3小时
print(datetime.datetime.now() + datetime.timedelta(minutes=30))  # 当前时间+30分
print(datetime.datetime.now() + datetime.timedelta(seconds =3))  # 当前时间+3秒

c_time = datetime.datetime.now()
print(c_time.replace(minute=3, hour=2))  # 时间替换

#时间比较：
d1 = datetime.datetime(1970,1,1)
d2 = datetime.datetime(1981,2,16)
print( d1+datetime.timedelta(1000) > d2)
print(d1 <d2)
print(d1!=d2)
d3 = d1
print(d1 > d2)
