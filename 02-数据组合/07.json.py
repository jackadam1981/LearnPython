#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2017/11/2 16:23
# @Author  : Jackadam
# @Email   : 
# @File    : 04.json.py
# @Software: PyCharm
import json

user = [
    [1, [
        11,
        12
    ]],
    [2, [
        21,
        22
    ]],
]
print(user)
print(type(user))
json_str = json.dumps(user)
print(json_str)
print(type(json_str))
new_user = json.loads(json_str)
print(new_user)
print(type(new_user))

with open("record.json", "w") as f:
    json.dump(new_user, f)
    print("存入文件完成...")

with open('record.json', 'r') as load_f:
    load_list = json.load(load_f)
    print('读取文件完成...')

print(load_list)
print(type(load_list))
