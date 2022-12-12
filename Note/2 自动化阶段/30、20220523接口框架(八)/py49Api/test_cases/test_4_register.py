"""
============================
Project: py49Api
Author:柠檬班-海励
Time:2022/5/23 21:45
E-mail:2227092769@qq.com
Company:湖南零檬信息技术有限公司
Site: http://www.lemonban.com
Forum: http://testingpai.com 
============================
"""
"""
思路
1、触发短信验证码接口
通过关键字，脚本生成未注册的手机号，设置为类属性(全局变量)
2、短信校验接口
在短信校验接口参数替换之前，执行sql语句从数据库中把短信验证码拿出来，设置为类属性(全局变量)
从属性里面拿到短信验证码和手机号，替换短信校验接口的请求参数
从响应结果里面拿到短信验证码接口返回的md5值，设置为属性，用于下一个注册接口
3、注册接口
从属性中获取参数，并替换参数

"""

import unittest
from ddt import ddt,data

from tools.handle_mysql import mysql
from tools.handle_excel import HandleExcel
from tools.handle_path import data_dir
from tools.handle_replace import HandleReplace
from tools.handle_response import HandleResponse
from tools.handle_extract_data import HandleExtract
from tools.handle_requests import HandleRequests
from tools.handle_assert_db import HandleAssertDb

data_list = HandleExcel(file_name=data_dir,sheet_name="register").get_data()

@ddt
class TestRegister(unittest.TestCase):
    #前置
    @classmethod
    def setUpClass(cls) -> None:
        #请求头，设置返回数据为中文
        # cls.header = {"locale": "zh_CN"}
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

    @classmethod
    def tearDownClass(cls) -> None:
        mysql.close_mysql()


    @data(*data_list)
    def test_register(self,case):
        print(case)
        #请求参数替换
        data = self.handle_replace.replace_data(data=case["data"])
        #发请求+响应结果处理
        response = self.handle_requests.send_request(method=case["method"],url=case["url"],data=data,is_upload=case["is_upload"])
        #断言(接口返回值的断言)
        self.handle_response.assert_response(expected_data=case["expected_data"],response=response)
        #提取全局变量
        self.handle_extract.handle_extract(extract_data=case["extract_data"],response=response)
        #数据库断言
        # SELECT * FROM tz_attach_file WHERE file_path="2022/05/bc73d98c6fb944e18332add0ba80370c.jpg"
        self.handle_assert_db.assert_db(assert_db=case["assert_db"])
if __name__ == '__main__':
    unittest.main()