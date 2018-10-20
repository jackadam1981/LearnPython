#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2017/11/16 18:01
# @Author  : Jackadam
# @Email   : 
# @File    : 04.ConfigParser.py
# @Software: PyCharm
from configparser import ConfigParser
fp = 'conf.ini'   #定义配置文件名
conf = ConfigParser()   #实例化
conf.read(fp)       # 打开conf
conf.add_section('Section1')   #添加conf节点
conf.set('Section1', 'name', 'jack')   #添加值
conf.set('Section1', 'age', '23')
conf.set('Section1', 'worker', 'CEO')
conf.add_section('Section2')   #添加conf节点
conf.set('Section2', 'name', 'rose')   #添加值
conf.set('Section2', 'age', '21')
conf.set('Section2', 'worker', 'CCC')
with open(fp, 'w') as fw:   #循环写入
    conf.write(fw)

'''
[Section1]
name = jack
age = 23
worker = CEO

'''


#读取配置文件
from configparser import ConfigParser
fp = 'conf.ini'   #定义配置文件名
conf = ConfigParser()   #实例化
conf.read(fp)       # 打开conf
name = conf.get('Section1','name')
print(name)
'''
1）读取配置文件
read(filename) 直接读取ini文件内容
sections() 得到所有的section，并以列表的形式返回
options(section) 得到该section的所有option
items(section) 得到该section的所有键值对
get(section,option) 得到section中option的值，返回为string类型
getint(section,option) 得到section中option的值，返回为int类型，还有相应的getboolean()和getfloat() 函数。
'''
section= conf.sections()
print(section)
option =conf.options('Section1')
print(option)
item=conf.items('Section1')
print(item)

#改写操作
conf.set('Section1', 'name', 'jackadam')        #设置为新值
with open(fp, 'w') as fw:   #循环写入
    conf.write(fw)
from configparser import ConfigParser          #重新读取
fp = 'conf.ini'   #定义配置文件名
conf = ConfigParser()   #实例化
conf.read(fp)       # 打开conf
name = conf.get('Section1','name')
print(name)