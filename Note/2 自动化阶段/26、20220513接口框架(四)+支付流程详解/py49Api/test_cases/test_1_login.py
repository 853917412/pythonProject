"""
============================
Project: py49Api
Author:柠檬班-海励
Time:2022/5/13 21:18
E-mail:2227092769@qq.com
Company:湖南零檬信息技术有限公司
Site: http://www.lemonban.com
Forum: http://testingpai.com 
============================
"""
"""
后端登陆接口
"""

import unittest
from ddt import ddt,data

from tools.handle_excel import HandleExcel
from tools.handle_path import data_dir

data_list = HandleExcel(file_name=data_dir,sheet_name="login").get_data()

@ddt
class TestLogin(unittest.TestCase):
    #前置

    #后置
    @data(*data_list)
    def test_login(self,case):
        #请求参数替换
        #发请求
        #响应结果统一处理
        #断言(接口返回值的断言)
        #提取全局变量
        #数据库断言
        print(case)



if __name__ == '__main__':
    unittest.main()