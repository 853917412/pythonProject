"""
============================
Project: py49Api
Author:柠檬班-海励
Time:2022/5/30 20:19
E-mail:2227092769@qq.com
Company:湖南零檬信息技术有限公司
Site: http://www.lemonban.com
Forum: http://testingpai.com 
============================
"""
"""
思路：
1、测试用例在excel中的，一个sheet一个测试类
2、写一个for循环，遍历excel中所有sheet里面的测试用例数据，放到测试类里面去生成测试用例类
3、通过unittest收集动态生成的测试类的测试用例到测试套件
4、运行测试套件


备选方案：
测试数据
data_list = [login:[{},{},{}],upload:[{},{},{}],create_product:[{},{},{}]]

"""


import unittest

from unittestreport import ddt,list_data
from tools.handle_replace import HandleReplace
from tools.handle_response import HandleResponse
from tools.handle_extract_data import HandleExtract
from tools.handle_requests import HandleRequests
from tools.handle_assert_db import HandleAssertDb


def generator_case(data_list):
    @ddt
    class TestPlaceOrder(unittest.TestCase):
        #前置
        @classmethod
        def setUpClass(cls) -> None:
            #参数替换
            cls.handle_replace = HandleReplace()
            #响应结果处理
            cls.handle_response = HandleResponse()
            # 数据提取
            cls.handle_extract = HandleExtract()
            #请求封装
            cls.handle_requests = HandleRequests()
            #数据库断言
            cls.handle_assert_db = HandleAssertDb()

        @list_data(data_list)
        def test_place_order(self,case):
            #执行前置sql语句
            self.handle_replace.setup_sql(setup_sql=case["setup_sql"])
            #请求参数替换
            data = self.handle_replace.replace_data(data=case["data"])
            #发请求+响应结果处理
            response = self.handle_requests.send_request(method=case["method"],url=case["url"],data=data,is_upload=case["is_upload"],port=case["port"])
            #断言(接口返回值的断言)
            self.handle_response.assert_response(expected_data=case["expected_data"],response=response)
            #提取全局变量
            self.handle_extract.handle_extract(extract_data=case["extract_data"],response=response)
            #数据库断言
            self.handle_assert_db.assert_db(assert_db=case["assert_db"])
    return TestPlaceOrder
