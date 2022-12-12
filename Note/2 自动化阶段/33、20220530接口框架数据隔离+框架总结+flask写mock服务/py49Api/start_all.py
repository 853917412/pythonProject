"""
============================
Project: py49Api
Author:柠檬班-海励
Time:2022/5/30 20:28
E-mail:2227092769@qq.com
Company:湖南零檬信息技术有限公司
Site: http://www.lemonban.com
Forum: http://testingpai.com 
============================
"""
import time
import unittest
import unittestreport

from test_cases.test_7_unittest_all import generator_case
from tools.handle_attribute import HandleAttribute
from tools.handle_excel import HandleExcel
from tools.handle_path import data_dir
from tools.handle_mysql import mysql


class Start:

    def __init__(self):
        self.excel = HandleExcel(file_name=data_dir)


    def __del_attribute(self):
        # attrs = HandleAttribute.__dict__
        # print(type(attrs))
        # setattr(HandleAttribute,"test","888")
        # print(HandleAttribute.__dict__)
        attr_names =  list(vars(HandleAttribute).keys())
        for name in attr_names:
            if not name.startswith("_"):
                delattr(HandleAttribute,name)
        # print(HandleAttribute.__dict__)

    def start(self):
        #获取excel中sheet_names = ["login","upload","create_product"]
        sheet_names = self.excel.sheet_names
        #遍历sheet_names
        for name in sheet_names:
            #每次执行之前删除调自己创建类属性
            self.__del_attribute()
            #通过name获取对应sheet的测试数据，返回[{},{},{}]，没一个{}是一个测试用例
            case_list = self.excel.get_data_cases(sheet_name=name)
            #将测试数据放到测试用例类生成函数中去，通过数据驱动生成测试用例类
            case_class = generator_case(case_list)
            #通过套件收集测试用例
            suite = unittest.defaultTestLoader.loadTestsFromTestCase(case_class)
            report_name = name + "_"+str(int(time.time()))
            runner = unittestreport.TestRunner(
                suite=suite,
                filename=report_name,
                report_dir="./reports",
                title='py49期接口测试报告',
                tester='老柠檬',
                desc="接口自动化测试报告",
                templates=1)
            runner.run()
        #所有测试用执行完后将数据库连接关闭
        mysql.close_mysql()
        # 拿到所有的sheet name
        #以类为维度收集测试用例类
        #手动清掉全局属性
        #执行用例
if __name__ == '__main__':
    cl = Start()
    cl.start()