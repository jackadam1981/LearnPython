# !/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2018-10-28 10:46
# @Author  : Jackadam
# @Email   :
# @File    : check.py
# @Software: PyCharm

from os import popen
import socket

#获取IP
def get_host_ip():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(('8.8.8.8', 80))
        ip = s.getsockname()[0]
    finally:
        s.close()
    return ip

#获取hostname
def get_host_name():
    return popen('hostname').read()


# 根据IP地址和计算机名，判断运行环境
def check_config():
    # 检查自己的IP
    ip = get_host_ip()
    ip = ip.split('.')
    ip_1 = ip[0]
    ip_3 = ip[0] + ip[1] + ip[2]
    hostname = get_host_name().split()[0]
    if ip_1 == '10' or ip_3 == '19216843' or hostname == 'db97344c7f2c':
        conf = 'dev'
    elif ip_3 == '1921681' or hostname == '28e05706b638':
        conf = 'home'
    elif hostname == '530f92b85101':
        conf = 'test'
    else:
        conf = 'pro'
    return conf

def up_alembic(DATA_BASE_URI):
    from configparser import ConfigParser

    fp = 'alembic.ini'  # 定义配置文件名
    conf = ConfigParser()  # 实例化
    conf.read(fp)  # 打开conf
    conf.set('alembic', 'sqlalchemy.url', DATA_BASE_URI)
    with open(fp, 'w') as fw:  # 循环写入
        conf.write(fw)