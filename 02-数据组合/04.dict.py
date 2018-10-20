#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2017/10/29 19:15
# @Author  : Jackadam
# @Email   : 
# @File    : 03.dict.py
# @Software: PyCharm
#字典
info = {
    'name1':'jack',
    'name2':'rose',
    'name3':'tom',
    'name4':'jerry',
    'name5':'james'
}
info['name6']='adam'   #增加
print(info['name3'])      #查找
print(info.get('name3'))  #查找最好用get，如果不存在，返回None
info['name5']= 'band'  #改写
print(info)
del info['name6']      #删除
print(info)

for i in info:
    print(i)
    print(info[i])

dict = {"a": "apple", "b": "banana", "o": "orange"}

print("##########dict######################")
for i in dict:
    print("dict[%s]=" % i, dict[i])

print("###########items#####################")
for (k, v) in dict.items():
    print("dict[%s]=" % k, v)

print("###########打印所有键名####################")
print(dict.keys())

for i in dict.keys():
    print(i)