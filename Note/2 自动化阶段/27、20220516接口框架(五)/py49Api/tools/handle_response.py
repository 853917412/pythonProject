"""
============================
Project: py49Api
Author:柠檬班-海励
Time:2022/5/16 20:55
E-mail:2227092769@qq.com
Company:湖南零檬信息技术有限公司
Site: http://www.lemonban.com
Forum: http://testingpai.com 
============================
"""

"""
第一个接口返回：{"access_token":"ee55d37a-b06c-4233-8a5c-913ad818e4f8","token_type":"bearer"}
{"response_type":"json","response":{"access_token":"ee55d37a-b06c-4233-8a5c-913ad818e4f8","token_type":"bearer"}}
第二个接口返回：账号或密码不正确
{"response_type":"str","response":账号或密码不正确}

"""
import json
from jsonpath import jsonpath
from unittest import TestCase

class HandleResponse:
    def __init__(self):
        self.my_assert = TestCase()
    #响应结果统一处理
    def handle_response(self,response):
        try:
            if isinstance(response.json(),dict):
                return {"response_type":"json","response":response.json()}
        except Exception as e:
                return {"response_type": "str", "response": response.text}

    #接口断言
    def assert_response(self,expected_data ,response):
        """
        思路：
        1、获取期望结果
        2、通过期望结果的key去响应结果里面去取数据，组成新的字典
        3、期望结果的字典和实际结果的字典进行对比
        :param expected_data:
        :param response:
        :return:
        """
        actual_data = {}
        expected_data = expected_data if isinstance(expected_data,dict) else json.loads(expected_data)
        print("期望结果：", expected_data)
        for key in expected_data:
            print("通过期望结果的key，组成实际结果")
            actual_data[key]=jsonpath(response,f"$..{key}")[0]
        print("实际结果：",actual_data)
        #断言期望结果和实际结果(比对字典)
        self.my_assert.assertEqual(expected_data,actual_data)





