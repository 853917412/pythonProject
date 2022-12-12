"""
============================
Project: py49
Author:柠檬班-海励
Time:2022/4/27 20:05
E-mail:2227092769@qq.com
Company:湖南零檬信息技术有限公司
Site: http://www.lemonban.com
Forum: http://testingpai.com 
============================
"""
"""
什么是日志
1、项目运行输出数据的记录

日志的作用
1、记录程序执行的过程
2、还原用户操作
3、可以日志来定位bug

一、日志收集器
1、用来收集程序输出数据的工具

二、日志收集器收集到日志格式(包含哪些信息)
1、日志内容
2、日志级别
   debug < info < warning < error < critical
3、输出时间
4、哪一行代码输出的
5、日志格式
6、日志输出到哪里(xxx.log，控制台)
"""
import requests
import logging

# 将默认的日志收集器(root)的日志级别改成了debug
logging.basicConfig(level=logging.DEBUG)

res = requests.post(url="http://httpbin.org/post",data={"key1":"val1"})
print(res.json())


# print("日志内容1，给程序员看的：debug")
# print("日志内容2，正常记录程序执行过程：info，用来定位bug")
# print("日志内容3，警告级别,WARNING:，可能不友好，语法不规范，需要更新升级某个包")
# print("日志内容4，报错信息：error,某个功能出错了，其他功能正常可以跑",)
# print("日志内容4，报错信息：致命错误,critical,引起重视，系统不行了，不能正常运行了")




