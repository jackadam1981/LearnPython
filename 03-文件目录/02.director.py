#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2017/10/31 20:42
# @Author  : Jackadam
# @Email   : 
# @File    : 02.director.py
# @Software: PyCharm
'''
三、目录操作方法大全
1.创建目录
os.mkdir("file")
2.复制文件：
shutil.copyfile("oldfile","newfile")        #oldfile和newfile都只能是文件
shutil.copy("oldfile","newfile")            #oldfile只能是文件夹，newfile可以是文件，也可以是目标目录
3.复制文件夹：
4.shutil.copytree("olddir","newdir")        #olddir和newdir都只能是目录，且newdir必须不存在
5.重命名文件（目录）
os.rename("oldname","newname")              #文件或目录都是使用这条命令
6.移动文件（目录）
shutil.move("oldpos","newpos")
7.删除文件
os.remove("file")
8.删除目录
os.rmdir("dir")                             #只能删除空目录
shutil.rmtree("dir")                        #空目录、有内容的目录都可以删
9.转换目录
os.chdir("path")                            #换路径
'''
