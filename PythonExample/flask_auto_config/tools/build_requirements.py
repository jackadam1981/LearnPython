# !/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2018-08-27 20:28
# @Author  : Jackadam
# @Email   :jackadam@sina.com
# @File    : build_requirements.py
# @Software: PyCharm
import os, sys
command = 'pip freeze > ../requirements.txt'
print(command)
os.system(command)


