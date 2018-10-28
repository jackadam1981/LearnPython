# !/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2018-10-28 9:25
# @Author  : Jackadam
# @Email   :
# @File    : config.py
# @Software: PyCharm


# 环境基类
class Base_Config(object):
    DEBUG = False
    TESTING = False
    LOGGER_NAME = 'Flask:'
    SECRET_KEY = 'v%»lÎImyÃUÑ¦8#ûïÂÓÙÛ@ræD}Ó^Ì©@÷Êñïíé÷ê«!,Ü@.qr2"hÁzKeô>¦Ô¶ïÁúlAÞ'
    BABEL_DEFAULT_LOCALE = 'zh_Hans_CN'
    SQLALCHEMY_TRACK_MODIFICATIONS = False


# 生产环境
class ProductionConfig(Base_Config):
    DATABASE_URI = 'mysql+mysqlconnector://zzcld:zzcld@mariadb/zzcld'


# 开发环境
class DevelopmentConfig(Base_Config):
    DATABASE_URI = 'mysql+mysqlconnector://zzcld:zzcld@mariadb/zzcld_test'
    DEBUG = True


# 测试环境
class TestingConfig(Base_Config):
    DATABASE_URI = 'sqlite://'
    TESTING = True


# 家庭环境
class HomeConfig(Base_Config):
    DATABASE_URI = 'mysql+mysqlconnector://zzcld:zzcld@nuc/zzcld_test'
    DEBUG = True
