# !/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2018-10-20 22:25
# @Author  : Jackadam
# @Email   :
# @File    : run_dev.py
# @Software: PyCharm
import os
command='python app.py dev'
print(command)
os.chdir(os.getcwd())
os.system(command)