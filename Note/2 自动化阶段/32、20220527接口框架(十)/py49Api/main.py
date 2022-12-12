"""
============================
Project: py49Api
Author:柠檬班-海励
Time:2022/5/6 21:36
E-mail:2227092769@qq.com
Company:湖南零檬信息技术有限公司
Site: http://www.lemonban.com
Forum: http://testingpai.com 
============================
"""


"""
框架执行入口
"""
import unittestreport
import unittest

from tools.handle_path import case_dir, report_name


suite = unittest.defaultTestLoader.discover(start_dir=case_dir,pattern="test_6_place_order.py")



runner = unittestreport.TestRunner(
                 suite=suite,
                 filename=report_name,
                 report_dir="./reports",
                 title='py49期接口测试报告',
                 tester='老柠檬',
                 desc="接口自动化测试报告",
                 templates=1)

runner.run()

runner.send_email(
                  host='smtp.qq.com',
                  port=465,
                  user='1605118090@qq.com',
                  password='oyukpnrnjirebahb',
                  to_addrs=['1605118090@qq.com','2538859969@qq.com','1351164168@qq.com']
)





