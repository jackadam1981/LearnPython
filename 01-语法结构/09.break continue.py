#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2017/10/26 21:00
# @Author  : Jackadam
# @Email   : 
# @File    : 09.task01.py
# @Software: PyCharm
'''
break 语句可以跳出 for 和 while 的循环体。
continue语句被用来告诉Python跳过当前循环块中的剩余语句，然后继续进行下一轮循环。
用break continue 写一个乘法表
外层用while　内层用for
外层用for  内层用while
end=''是输出不换行
'''
i = 0
while True:
    i = i + 1
    for j in range (1,10):
        if j >i:
            continue
        elif j == i :
            print('%i X %i = %i   '%(j,i,j*i))
        else:
            print('%i X %i = %i   ' % (j, i, j * i),end='')
    if i >= 9:
        break


for i in range (1,10):
    if i > 9 :
        break
    j = 0
    while j<10:
        j = j + 1
        if j>i:
            continue
        elif j == i :
            print('%i X %i = %i   '%(j,i,j*i))
        else:
            print('%i X %i = %i   ' % (j, i, j * i),end='')
