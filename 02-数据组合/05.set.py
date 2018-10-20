#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2017/10/29 21:01
# @Author  : Jackadam
# @Email   : 
# @File    : set.py
# @Software: PyCharm
# set自动去重，但是没有值，只有key
s = set([3, 5, 9, 10])  # 创建一个数值集合

t = set("Hello")  # 创建一个唯一字符的集合

x = 'x'

a = t | s  # t 和 s的并集

b = t & s  # t 和 s的交集

c = t - s  # 求差集（项在t中，但不在s中）

d = t ^ s  # 对称差集（项在t或s中，但不会同时出现在二者中）

# 基本操作：

t.add('x')  # 添加一项

s.update([10, 37, 42])  # 在s中添加多项

# 使用remove()可以删除一项：

t.remove('H')

len(s)
# set 的长度

x in s
# 测试 x 是否是 s 的成员

x not in s
# 测试 x 是否不是 s 的成员

s.issubset(t)
s <= t
# 测试是否 s 中的每一个元素都在 t 中

s.issuperset(t)
s >= t
# 测试是否 t 中的每一个元素都在 s 中

s.union(t)
s | t
# 返回一个新的 set 包含 s 和 t 中的每一个元素

s.intersection(t)
s & t
# 返回一个新的 set 包含 s 和 t 中的公共元素

s.difference(t)
s - t
# 返回一个新的 set 包含 s 中有但是 t 中没有的元素

s.symmetric_difference(t)
s ^ t
# 返回一个新的 set 包含 s 和 t 中不重复的元素

s.copy()
# 返回 set “s”的一个浅复制
