#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2017/10/29 15:14
# @Author  : Jackadam
# @Email   : 
# @File    : 01.list.py
# @Software: PyCharm

names = ['jack', 'rose', 'tom', 'jerry', 'jerry']
print(names)
print(names[0])
names[0] = 'adam'  # 改
print(names[0])
print(names[2:])  # 从左开始右边所有
print(names[-3:])  # 从右开始右边所有
print(names[:-2])  # 从右开始左边所有
print(names[1:3])  # 左向右切片
print(names[-2:-1])  # 右向左切片

names.append('alex')  # 增加
print(names)

names.insert(1, 'james')  # 指定位置插入
print(names)

names.remove('james')  # 删除
print(names)

del names[1]  # 删除
print(names)

names.pop()  # 删除最后一个
# names.pop(1)  ==  del names[1]

print(names.index('tom'))  # 查找
print(names.count('jerry'))  # 统计数量
names.reverse()  # 反转顺序
print(names)
names.sort()  # 按首字母顺序排序   符号--数字--字母
print(names)

names2 = [1, 2, 3, 4]
names.extend(names2)  # 两个列表的合并
print(names)
del names2

# 拼接列表为字符串
print('---------')
names = ['jack', 'rose', 'tom', 'jerry', 'jerry']
end = ''.join(names)
print(end)
# 注意，这种拼接方法，不支持int 数字，只支持字符串
# names2 = [1, 2, 3, 4]
# end = ''.join(names2)
# print(end)
# 可以这样来玩
a = [ 2, 3, 4]
for i in range(len(a)):
    a[i]=str(a[i])
print(a)
str1=''.join(a)
print(str1)

#简写
a = [3,4,5,6]
b = [ str(i) for i in a ]
str2 = ''.join(b)
print(str2)


#二维列表转一维
print('二维列表转一维')
from itertools import chain
list_ =[['K154', 'K151'], ['K1102', 'K1103', 'K1102'], 'K7959', 'K7960', ['K1101', 'K1104', 'K1101'], ['K152', 'K153']]
a=list(chain.from_iterable(list_))
print(list_)
print(a)
list_ =[['K154', 'K151'], ['K1102', 'K1103', 'K1102'], ['K7959',],[ 'K7960',], ['K1101', 'K1104', 'K1101'], ['K152', 'K153']]
a=list(chain.from_iterable(list_))
print(list_)
print(a)