# !/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2019/12/17 11:44
# @Author  : Jackadam
# @Email   :
# @File    : middleware.py
# @Software: PyCharm
from authz.middleware import CasbinMiddleware


class Middleware(CasbinMiddleware):
    def check_permission( self, request ):
        print('这里处理验证')
        user = request.remote_user  # subject
        if user is None:
            user = 'anonymous'
        path = request.path  # object
        method = request.method  # action
        return self.enforcer.enforce(user, path, method)
