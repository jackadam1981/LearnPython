#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2017/10/30 10:19
# @Author  : Jackadam
# @Email   : 
# @File    : 01.file.py
# @Software: PyCharm
'''
一、python中对文件、文件夹操作时经常用到的os模块和shutil模块常用方法。
1.得到当前工作目录，即当前Python脚本工作的目录路径: os.getcwd()
2.返回指定目录下的所有文件和目录名:os.listdir()
3.函数用来删除一个文件:os.remove()
4.删除多个目录：os.removedirs（r“c：\python”）
5.检验给出的路径是否是一个文件：os.path.isfile()
6.检验给出的路径是否是一个目录：os.path.isdir()
7.判断是否是绝对路径：os.path.isabs()
8.检验给出的路径是否真地存:os.path.exists()
9.返回一个路径的目录名和文件名:os.path.split()     eg os.path.split('/home/swaroop/byte/code/poem.txt') 结果：('/home/swaroop/byte/code', 'poem.txt')
10.分离扩展名：os.path.splitext()
11.获取路径名：os.path.dirname()
12.获取文件名：os.path.basename()
13.运行shell命令: os.system()
14.读取和设置环境变量:os.getenv() 与os.putenv()
15.给出当前平台使用的行终止符:os.linesep    Windows使用'\r\n'，Linux使用'\n'而Mac使用'\r'
16.指示你正在使用的平台：os.name       对于Windows，它是'nt'，而对于Linux/Unix用户，它是'posix'
17.重命名：os.rename（old， new）
18.创建多级目录：os.makedirs（r“c：\python\test”）
19.创建单个目录：os.mkdir（“test”）
20.获取文件属性：os.stat（file）
21.修改文件权限与时间戳：os.chmod（file）
22.终止当前进程：os.exit（）
23.获取文件大小：os.path.getsize（filename）

'''
import os

os.getcwd()  # 获取当前工作目录，即当前python脚本工作的目录路径
#os.chdir("dirname")  # 改变当前脚本工作目录；相当于shell下cd
os.chdir('c:/')
os.curdir  # 返回当前目录: ('.')
os.pardir  # 获取当前目录的父目录字符串名：('..')
os.makedirs('dirname1/dirname2')  # 可生成多层递归目录
os.removedirs('dirname1')  # 若目录为空，则删除，并递归到上一级目录，如若也为空，则删除，依此类推
os.mkdir('dirname')  # 生成单级目录；相当于shell中mkdir dirname
os.rmdir('dirname')  # 删除单级空目录，若目录不为空则无法删除，报错；相当于shell中rmdir dirname
os.listdir('dirname')  # 列出指定目录下的所有文件和子目录，包括隐藏文件，并以列表方式打印
os.remove()  # 删除一个文件
os.rename("oldname", "newname")  # 重命名文件/目录
os.stat('path/filename')  # 获取文件/目录信息
os.sep  # 输出操作系统特定的路径分隔符，win下为"\\",Linux下为"/"
os.linesep  # 输出当前平台使用的行终止符，win下为"\t\n",Linux下为"\n"
os.pathsep  # 输出用于分割文件路径的字符串
os.name  # 输出字符串指示当前使用平台。win->'nt'; Linux->'posix'
os.system("bash command")  # 运行shell命令，直接显示
os.environ  # 获取系统环境变量
path = 'c:\a\b\c\d\e.txt'
# os.path.abspath(path)  #返回path规范化的绝对路径
os.path.split(path)  # 将path分割成目录和文件名二元组返回
os.path.dirname(path)  # 返回path的目录。其实就是os.path.split(path)的第一个元素
os.path.basename(path)  # 返回path最后的文件名。如何path以／或\结尾，那么就会返回空值。即os.path.split(path)的第二个元素
os.path.exists(path)  # 如果path存在，返回True；如果path不存在，返回False
os.path.isabs(path)  # 如果path是绝对路径，返回True
os.path.isfile(path)  # 如果path是一个存在的文件，返回True。否则返回False
os.path.isdir(path)  # 如果path是一个存在的目录，则返回True。否则返回False
# os.path.join(path1[, path2[, ...]])  #将多个路径组合后返回，第一个绝对路径之前的参数将被忽略
os.path.getatime(path)  # 返回path所指向的文件或者目录的最后存取时间
os.path.getmtime(path)  # 返回path所指向的文件或者目录的最后修改时间
