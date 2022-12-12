"""
============================
Project: py49
Author:柠檬班-海励
Time:2022/4/15 20:08
E-mail:2227092769@qq.com
Company:湖南零檬信息技术有限公司
Site: http://www.lemonban.com
Forum: http://testingpai.com 
============================
"""
"""
一、前置处理
1、类级别的前置
    @classmethod
    def setUpClass(cls) -> None:
        print("类级别的前置，整个测试用例类只执行一次")
2、函数级别的前置
    def setUp(self) -> None:
        print("函数级别的前置，每个测试用例执行之前都执行一遍")
二、后置处理
1、类级别后置
    @classmethod
    def tearDownClass(cls) -> None:
        print("类级别的后置，整个测试用例类执行结束的时候，只执行一次")
2、函数级别后置
    def tearDown(self) -> None:
        print("函数级别的后置，每个测试用例执行之后都执行一遍")
"""

import unittest

class TestDemo02(unittest.TestCase):
    # 类级别的前置
    @classmethod
    def setUpClass(cls) -> None:
        print("类级别的前置，整个测试用例执行之前，只执行一次")

    @classmethod
    def tearDownClass(cls) -> None:
        print("类级别的后置，整个测试用例类执行结束的时候，只执行一次")

    def setUp(self) -> None:
        print("函数级别的前置，每个测试用例执行之前都执行一遍")

    def tearDown(self) -> None:
        print("函数级别的后置，每个测试用例执行之后都执行一遍")

    def test_01(self):
        print("测试用例1")

    def test_02(self):
        print("测试用例2")

if __name__ == '__main__':
    unittest.main()


