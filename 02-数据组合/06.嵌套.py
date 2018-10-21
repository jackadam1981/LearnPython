#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2017/10/29 21:18
# @Author  : Jackadam
# @Email   : 
# @File    : 06.py
# @Software: PyCharm
u1 = [410103, 4, 1]
u2 = [510103, 4, 1]
u3 = [610103, 4, 2]
u4 = [710103, 4, 2]
u5 = [810103, 11, 1]
u6 = [910103, 11, 1]
u7 = [110103, 11, 2]
u8 = [120103, 11, 2]
test = [u1, u2, u3, u4, u5, u6, u7, u8]
list_all = [
    [4, [
        [410103, 4],
        [510103, 5]
    ]],
    [11, [
        [610103, 5],
        [710103, 7]

    ]]
]
# print(test)
a_all = set([u1[1], u2[1], u3[1], u4[1], u5[1], u6[1], u7[1], u8[1]])
b_all = set([u1[2], u2[2], u3[2], u4[2], u5[2], u6[2], u7[2], u8[2]])
a_list = list(a_all)
a_list.sort()
b_list = list(b_all)
b_list.sort()
# print(a_list)
# print(b_list)
user = []
for i in a_list:
    print(i)
    temp = []
    for j in test:
        if j[1] == i:
            temp.append(j)
    print(temp)
    user.append([i, temp])
print(user)
print(user[0][1][1][0])
print(user[1])
