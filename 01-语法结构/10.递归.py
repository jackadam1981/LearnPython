#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2017/11/19 9:13
# @Author  : Jackadam
# @Email   : 
# @File    : 02.递归.py
# @Software: PyCharm
def f(i):
    if i >= 1:
        f(i - 1)
        print(i)
#执行debug可见，i=9,满足if条件，递归执行f（9-1），i=8，满足if条件，递归执行f（8-1），直到i=1，满足if条件，递归执行f（0）
#一直在进入函数，进了9层，直到f（0），不满足if条件，才执行完一遍f函数
#返回上一层，继续下一条语句print（i），输出1，再返回上一层，输出2

def ff(i):
    if i >= 1:
        ff(i - 1)
        for j in range(1,i+1):
            print('%d*%d=%d\t'%(j,i,j*i),end='')
            if j ==i :
                print('\n')


if __name__ == '__main__':
    f(9)
    ff(9)


