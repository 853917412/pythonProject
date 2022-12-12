"""
============================
Project: py49
Author:柠檬班-海励
Time:2022/4/15 20:22
E-mail:2227092769@qq.com
Company:湖南零檬信息技术有限公司
Site: http://www.lemonban.com
Forum: http://testingpai.com 
============================
"""
"""
二、测试用例执行顺序
1、通过ascii码来区分执行先后顺序，ascii码小的先执行
2、对比逻辑是逐位对比
3、ascii吗顺序：0--9 < A--Z < a--z
4、数据驱动ddt使用的时候，执行顺序就按ddt 数据传递的先后顺序


三、断言
self.assertEqual(1,1)
self.assertNotEqual("期望结果","实际结果")
self.assertNotIn()
self.assertIn()
self.assertTrue()
self.assertFalse()
self.assertIs()
self.assertIsNot()
unittest以用例运行过程中是否抛出异常来判断用例是否执行成功，
当我们做了异常处理，一定要手动抛出异常给unittest捕获，这样才会将测试用例标记为失败

"""


import unittest

class TestDemo(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        #初始化数据，token 处理
        print("类级别的前置")

    @classmethod
    def tearDownClass(cls) -> None:
        # 数据库关闭操作
        print("类级别的后置")

    def test_01(self):
        # 业务处理
        print("测试用例1")

    def test_02(self):
        # 业务处理
        print("测试用例2")

    def test_03(self):
        # 业务处理
        print("测试用例3")
        try:
            self.assertEqual(1,2)
        except Exception as e:
            print("抛异常了但是unittest收不到")
            raise AssertionError("断言错误",e)
if __name__ == '__main__':
    unittest.main()
