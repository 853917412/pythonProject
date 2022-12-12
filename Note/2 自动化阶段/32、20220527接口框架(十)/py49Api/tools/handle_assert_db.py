"""
============================
Project: py49Api
Author:柠檬班-海励
Time:2022/5/20 20:10
E-mail:2227092769@qq.com
Company:湖南零檬信息技术有限公司
Site: http://www.lemonban.com
Forum: http://testingpai.com 
============================
"""

import json
from unittest import TestCase

from tools.handle_mysql import mysql
from tools.handle_replace import HandleReplace


class HandleAssertDb:

    def __init__(self):
        self.my_assert = TestCase()
        self.handle_replace = HandleReplace()

    #数据库断言
    def assert_db(self,assert_db):
        """
        思路：
        1、excel中新增一个字段用来存放我的期望结果和实际结果
        2、存放实际结果，期望结果
          {"expected_data":1,"actual_data":"SELECT COUNT(*)  FROM tz_attach_file WHERE file_path="}
        3、提取响应结果中的file_path值，然后替换actual_data中的sql语句
        4、替换sql语句
        5、执行sql语句获取查询结果，与期望结果进行比对

        :return:
        """
        if assert_db:
            #将excel中的assert_db转换成python对象
            assert_db = assert_db if isinstance(assert_db,dict) else json.loads(assert_db)
            #替换sql语句
            sql = self.handle_replace.replace_sql(sql=assert_db["actual_data"])
            # 执行sql语句
            sql_result = mysql.get_datas(sql=sql)
            # 断言
            self.my_assert.assertEqual(assert_db["expected_data"],sql_result[0])
            print("断言成功")
        else:
            print("excel中assert_db字段为空，不需要做数据库断言")




