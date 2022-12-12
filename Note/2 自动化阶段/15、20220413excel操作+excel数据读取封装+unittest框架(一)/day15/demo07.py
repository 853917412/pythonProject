"""
============================
Project: py49
Author:柠檬班-海励
Time:2022/4/13 21:39
E-mail:2227092769@qq.com
Company:湖南零檬信息技术有限公司
Site: http://www.lemonban.com
Forum: http://testingpai.com 
============================
"""
"""
unittest
一、四大核心组件
1、TestCase：测试用例类，用来定义测试用例
2、TestSuite：测试套件，用来收集测试用例的
3、TestRunner：执行器，用来执行测试用例的
4、TestFixture：测试脚手架，夹具前后置

二、工作原理
1、通过TestFixture去设置前置条件，后置清理
2、通过TestCase写测试用例
3、通过TestSuite来收集测试用例
4、将TestSuite套件送给TestRunner去执行
5、收集测试结果，生成测试报告

三、测试用例编写
1、导入unittest
2、写一个测试用例类，继承unittest.TestCase(建议类名称以Test开头)
3、在测试类里面写测试用例（以test_开头的方法）
4、自动收集用例，函数执行入口unittest.main()
5、配置默认执行器: File --- setting -- tools --python intergratred tools -- testing---default test runner --选择unittest

四、测试用例有哪些东西
1、前置条件
2、测试步骤(业务逻辑)
3、断言(返回数据断言、数据库断言)
4、后置处理
5、测试报告，邮件发送


"""
import unittest

class TestDemo(unittest.TestCase):
    def test_01(self):
        print("测试用例")

if __name__ == '__main__':
    unittest.main()







