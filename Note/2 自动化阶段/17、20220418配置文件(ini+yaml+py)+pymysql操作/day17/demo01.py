"""
============================
Project: py49
Author:柠檬班-海励
Time:2022/4/18 20:09
E-mail:2227092769@qq.com
Company:湖南零檬信息技术有限公司
Site: http://www.lemonban.com
Forum: http://testingpai.com 
============================
"""
"""
一、数据驱动unittestreport




"""
import unittest
from unittestreport import ddt,list_data

case_data = [{
	'method': 'post',
	'url': 'http://mall.lemonban.com:8108/adminLogin',
	'data': '{"t": "test1"}',

}, {
	'method': 'post',
	'url': 'http://mall.lemonban.com:8108/adminLogin',
	'data': '{"t": "test2"}',
}]


@ddt
class TestDemo(unittest.TestCase):

    @list_data(case_data)
    def test_01(self,case):
        print(case)



