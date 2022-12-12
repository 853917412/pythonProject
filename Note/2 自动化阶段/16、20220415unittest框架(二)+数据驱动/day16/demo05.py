"""
============================
Project: py49
Author:柠檬班-海励
Time:2022/4/15 21:44
E-mail:2227092769@qq.com
Company:湖南零檬信息技术有限公司
Site: http://www.lemonban.com
Forum: http://testingpai.com 
============================
"""
"""

数据驱动
1、执行用例的时候，业务逻辑不变，改变的只是入参的不同
2、安装ddt模块
   pip install ddt 

登陆
1、账号
2、密码

用例
1、登陆成功
   1、管理员账号
   2、普通运营账号
   3、其他账号
2、登陆失败
   1、账号不存在
   2、账号密码不匹配
同一个接口来说：变化的都只是入参
不同的接口：变化的，接口地址、参数、请求方法、请求头、业务处理流程不一样(流程控制处理)
"""
import unittest
from ddt import ddt,data,unpack

# import requests
# res = requests.request(method="", url="",json="",headers="")


case_data = [{
	'method': 'post',
	'url': 'http://mall.lemonban.com:8108/adminLogin',
	'data': '{"t": "test1"}',

}, {
	'method': 'post',
	'url': 'http://mall.lemonban.com:8108/adminLogin',
	'data': '{"t": "test2"}',
}]

# 掌握
@ddt
class TestDemo(unittest.TestCase):
    @data(*case_data)
    def test_01(self,case):
        print("测试用例数据：",case)
        print("测试用例步骤")
        print(case["url"])


# 不用，做个了解
# @ddt
# class TestDemo(unittest.TestCase):
#     @unpack
#     @data(*case_data)
#     def test_01(self,method,url,data):
#         print("测试用例数据：",method,url,data)
#         print("测试用例步骤")


if __name__ == '__main__':
    unittest.main()

# for i in case_data:
#     test_01(i)





