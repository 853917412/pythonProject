"""
============================
Project: py49
Author:柠檬班-海励
Time:2022/4/15 20:43
E-mail:2227092769@qq.com
Company:湖南零檬信息技术有限公司
Site: http://www.lemonban.com
Forum: http://testingpai.com 
============================
"""
"""
测试用例收集
创建测试套件
suite = unittest.TestSuite()

一、用例维度收集
1、suite.addTest(类名称("函数名称"))
  suite.addTest(TestDemo("test_01"))
2、suite.addTests(测试用例集合)
case_list = [TestDemo("test_01"),TestDemo("test_02")]
suite.addTests(case_list)

二、测试类的维度
suite.addTest(unittest.makeSuite(TestDemo))
suite.addTest(unittest.makeSuite(TestDemo02))

三、模块维度
suite = unittest.defaultTestLoader.discover(start_dir=".",pattern="demo02.py")
start_dir: 测试用例文件的目录(test.py文件),点代表当前目录
pattern='test*.py': 测试用例文件名称，默认收集测试目录下以test开头的py文件
"""
from day16.demo02 import TestDemo
from day16.demo01 import TestDemo02

import unittest

# 创建测试套件
# suite = unittest.TestSuite()

# ============================================================
# 测试用例维度
# 添加测试用例到测试套件
# suite.addTest(TestDemo("test_01"))
# suite.addTest(TestDemo("test_02"))
# 添加多个测试用例，测试用例集合
# case_list = [TestDemo("test_01"),TestDemo("test_02")]
# suite.addTests(case_list)
# ============================================================

# ============================================================
# 测试类维度
# suite.addTest(unittest.makeSuite(TestDemo))
# suite.addTest(unittest.makeSuite(TestDemo02))
# ============================================================

# ============================================================
# 模块维度
# start_dir: 测试用例文件的目录(test.py文件),点代表当前目录
# pattern='test*.py': 测试用例文件名称，默认收集测试目录下以test开头的py文件,可以自己指定
# *表示通配
suite = unittest.defaultTestLoader.discover(start_dir=".",pattern="demo02.py")
# ============================================================

# 创建执行器
runner = unittest.TextTestRunner()

# 执行用例
runner.run(suite)