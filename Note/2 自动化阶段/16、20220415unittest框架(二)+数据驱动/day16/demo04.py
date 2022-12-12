"""
============================
Project: py49
Author:柠檬班-海励
Time:2022/4/15 21:12
E-mail:2227092769@qq.com
Company:湖南零檬信息技术有限公司
Site: http://www.lemonban.com
Forum: http://testingpai.com 
============================
"""
"""
测试报告收集
1、unittes自带的测试报告，没啥用
2、BeautifulReport==0.1.3
   pip install BeautifulReport==0.1.3
3、unittestreport
   pip install unittestreport==1.3.2

4、发送邮件
QQ邮箱--设置--账户--POP3/IMAP/SMTP/Exchange/CardDAV/CalDAV服务
开启服务：
POP3/SMTP服务 (如何使用 Foxmail 等软件收发邮件？) 发送邮件
"""


import unittest
from BeautifulReport import BeautifulReport
from unittestreport import TestRunner

suite = unittest.defaultTestLoader.discover(start_dir=".",pattern="demo05.py")

# 测试报告：BeautifulReport
# br = BeautifulReport(suites=suite)
# br.report(description="测试报告",filename="my_test.html")

#unittestreport
runner = TestRunner(
                 suite=suite,
                 filename="my_report.html",
                 report_dir="./reports",
                 title='测试报告',
                 tester='海励',
                 desc="接口自动化测试报告",
                 templates=2
)

runner.run()
# 邮件发送
runner.send_email(host='smtp.qq.com',
                  port=465,
                  user='1605118090@qq.com',
                  password='oyukpnrnjirebahb',
                  to_addrs=['772152841@qq.com','1432825846@qq.com','56878458@qq.com','2366320081@qq.com']
)


