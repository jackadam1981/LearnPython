#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2017/10/29 21:09
# @Author  : Jackadam
# @Email   : 
# @File    : string.py
# @Software: PyCharm
test = 'abcdefghijklmnopqrstuvwxyz'
print(test)
print(test[1:5])    #可以切片
print(test.capitalize())  #首字母大写
print(test.count('a'))#计数
print(test.center(50,'-')) #美观打印
print(test.encode('utf-8'))#转码
print(test.endswith('yz'))  #判断结尾
print(test.endswith('zz'))  #判断结尾
test = 'a\tbcdefghijklmnopqrstuvwxyz' #\t是tab键
print(test.expandtabs(tabsize=5)) #定义tab键的长度
test = 'abcdefghijklmnopqrstuvwxyz'
print(test.find('i')) #找到位置
test ="My name is {name},I'm {age} old."
print(test.format(name ='jack', age = 20)) #格式化输出
print(test.format_map({'name':'rose','age':18})) #另一种格式化输出
print('abc123'.isalnum()) #是否数字字母
print('abc123!@#'.isalnum())#不包含符号
print('abcABC'.isalpha())#是否字母
print('abcABC123'.isalpha())#是否字母不含数字
print('1a'.isdecimal())#是否10进制
print('10'.isdigit())#是否数字
print('aa'.isidentifier())#是否是合法标识符
print('a'.islower())#是否小写
print('123a'.isnumeric())#是否纯数字
print(' '.isspace())#是否空格
print('My name is jack'.istitle())#是否首字母全大写
print('My name is jack'.isprintable())#是否可以打印tty drive 不可以打印
print('My name is jack'.isupper())#是否全大写
print('My name is jack'.join('------'))#分割组合  分割joni里面的，把前面的加进去
print('+'.join(['1','2','3']))   #1+2+3
print(test.ljust(50,'*'))  #用*在后面补齐50位
print(test.rjust(50,'*'))  #用*在前面补齐50位
print('jack'.upper()) #全换大写
print('Jack'.lower()) #全换小写
print('\n  test  \n') #\n是回车
print('--')
print('\n  test  \n'.rstrip())  #去掉右边的空格和回车
print('--')
print('\n  test  \n'.lstrip())#去掉左边的空格和回车
print('--')
print('\n  test  \n'.split()) #去掉两边的空格和回车

p = str.maketrans('abcdefg','1234567')   #明文替换
print('jack'.translate(p))

print('jack adam'.replace('a','A'))   #替换
print('jack adam'.replace('a','A',2)) #替换几个
print('-----------------------')
print('jack adam'.find('a')) #查找一个字符的位置
print('jack adam'.rfind('a'))#查找某字符的最右的位置
print('jack adam'.split())# 用空格分成字符串
print('jack adam'.split('a'))# 用a分成字符串 a就没了
print('jack \nadam'.splitlines())# 用换行分成字符串
print('Jack Adam'.swapcase())#大小写转换
print('jack adam'.title())#首字母大写
print('jack adam'.zfill(50))#用0填充50位

print('------------------------------')
str='abcdefg'
tag = 'abcdefg'
if tag in str:
    print('yes')
if str ==tag:
    print('yes yes')


