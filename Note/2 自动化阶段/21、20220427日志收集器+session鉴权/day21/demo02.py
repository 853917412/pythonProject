"""
============================
Project: py49
Author:柠檬班-海励
Time:2022/4/27 20:29
E-mail:2227092769@qq.com
Company:湖南零檬信息技术有限公司
Site: http://www.lemonban.com
Forum: http://testingpai.com 
============================
"""
"""
自定义日志收集器
1、创建一个日志收集器
py49 = logging.getLogger(name="py49")

2、日志格式
"%(name)s-%(levelname)s-%(asctime)s-%(pathname)s-%(lineno)d>>>: %(message)s"
%(name)s : 日志渠道的名称
%(levelno)s：日志级别对应的数字编号
%(levelname)s：日志级别文字版
%(pathname)s ：输出日志的py文件的绝对路径
%(filename)s：py文件的名称(名称.py)
%(module)s ：py文件的名称(名称没有后缀)
%(lineno)d ：日志输出的行数
%(funcName)s ：输出日志的函数的名称，不是函数输出的日志就是模块名称
%(created)f：日志输出的时间，格式为时间戳
%(asctime)s ：日志输出的时间，格式年-月-日 时:分:秒,毫秒
%(msecs)d : 日志输出时间毫秒
%(relativeCreated)d：日志输出的相对时间，毫秒
%(thread)d：线程id
%(threadName)s：线程名称
%(process)d：进程id，进程--线程：一个进程可以启动多个线程
%(message)s：日志信息

3、日志级别
py49.setLevel(logging.DEBUG)

4、日志收集到哪里去：渠道
   1、控制台
   2、日志文件
"""

import logging
from logging import handlers

#1、创建日志收集器
py49 = logging.getLogger(name="py49")

#2、创建日志渠道
pychacrm = logging.StreamHandler()
# 文件渠道
log_file = handlers.TimedRotatingFileHandler(filename="python.log",when="midnight",backupCount=10,encoding="utf-8")

#3、创建日志格式
fmt="%(name)s-%(levelname)s-%(asctime)s-%(pathname)s-%(lineno)d>>>: %(message)s"
fmt1 = logging.Formatter(fmt=fmt)

#4、给输入渠道绑定日志格式
pychacrm.setFormatter(fmt=fmt1)
log_file.setFormatter(fmt=fmt1)

#5、日志级别: 设置在日志收集器上
# 可以单独给渠道设置日志级别，但是一定小于收集器日志级别
# debug < info < warning < error < critical
py49.setLevel(logging.INFO)

#6、渠道绑定到收集器
py49.addHandler(pychacrm)
py49.addHandler(log_file)

py49.debug(msg="测试日志，debug级别")
py49.info(msg="info级别的日志")

print('info级别的日志')