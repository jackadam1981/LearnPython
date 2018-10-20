#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2017/11/22 0:32
# @Author  : Jackadam
# @Email   : 
# @File    : 04.异常处理.py
# @Software: PyCharm
#搞太复杂的也没什么用。简单处理一下，任何异常都保存到文件里吧，当然还有一个错误时间
#不明白的，可以去看http://www.cnblogs.com/jackadam/p/7845625.html
import traceback,time
name = ['jack','rose']
try:
    1/0
except Exception as e:
    now_time = time.strftime('%Y-%m-%d--%H:%M:%S')
    f = open('errorlog.txt', 'a', encoding='utf-8')
    f.write(now_time+'\n')
    traceback.print_exc(file=f)
    f.flush()
    f.close()
finally:
    print('over')

print('例子一')
try:
    1/0
except Exception as e:   #出现异常，则执行
    print('error')
    print(e)
else:                    #没有异常，则执行
    print('OK')
finally:                 #始终执行
    print('end')

print('例子二')
try:
    1/0
except Exception as e:
    print('error')
    print(e)
else:
    print('OK')
finally:
    print('end')