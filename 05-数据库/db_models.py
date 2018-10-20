# !/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2017-12-30 10:32
# @Author  : Jackadam
# @Email   :
# @File    : db_models.py
# @Software: PyCharm

from sqlalchemy import Column,Integer,String,DateTime,func


from .settings import Base
class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    name = Column(String(32))  # 真实姓名
    username = Column(String(32))  # 登录名
    password = Column(String(32))  # 登陆密码
    gongzhong = Column(Integer)  # 工种编号
    group = Column(Integer)  # 上班分组
    lastedit = Column(DateTime, default=func.now(), nullable=False)
    lastanswer = Column(DateTime, default=func.now(), nullable=False)  # 最后一次答题日期



'''
常见的SQLALCHEMY列类型.配置选项和关系选项

类型名称    python类型    描述
Integer int 常规整形，通常为32位
SmallInteger    int 短整形，通常为16位
BigInteger  int或long    精度不受限整形
Float   float   浮点数
Numeric decimal.Decimal 定点数
String  str 可变长度字符串
Text    str 可变长度字符串，适合大量文本
Unicode unicode 可变长度Unicode字符串
Boolean bool    布尔型
Date    datetime.date   日期类型
Time    datetime.time   时间类型
Interval    datetime.timedelta  时间间隔
Enum    str 字符列表
PickleType  任意Python对象  自动Pickle序列化
LargeBinary str 二进制

常见的SQLALCHEMY列选项
可选参数    描述
primary_key 如果设置为True，则为该列表的主键
unique  如果设置为True，该列不允许相同值
index   如果设置为True，为该列创建索引，查询效率会更高
nullable    如果设置为True，该列允许为空。如果设置为False，该列不允许空值
default 定义该列的默认值
'''