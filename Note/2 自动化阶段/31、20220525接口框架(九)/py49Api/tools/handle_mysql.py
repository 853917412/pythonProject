"""
============================
Project: py49Api
Author:柠檬班-海励
Time:2022/5/20 20:44
E-mail:2227092769@qq.com
Company:湖南零檬信息技术有限公司
Site: http://www.lemonban.com
Forum: http://testingpai.com 
============================
"""


import pymysql

from conf.settings import mysql_info

class HandleMysql:
    def __init__(self):
        self.db = pymysql.connect(
                            host=mysql_info["host"],
                            port=mysql_info["port"],
                            user=mysql_info["user"],
                            password=mysql_info["password"],
                            database=mysql_info["database"],
                            charset="utf8",
                            autocommit=True,# 必须增加自动提交，否则数据库断言会失败
                            cursorclass=pymysql.cursors.DictCursor
                            # 返回字典
                        )
        self.cur = self.db.cursor()

    # 后置
    def close_mysql(self):
        self.cur.close()
        self.db.close()

    #获取数据库数据，添加到list中返回
    def get_datas(self,sql):
        value_list = []
        self.cur.execute(sql)
        result = self.cur.fetchall()
        print(result)
        for val in result:
            #[{},{}]
            for i in val.values():
                #{}
                value_list.append(i)
        return value_list


    def get_dict_data(self,sql):
        self.cur.execute(sql)
        result = self.cur.fetchall()
        print(result,type(result))
        return result



mysql = HandleMysql() # 数据库1
# sql = "SELECT count(*) as file_path FROM tz_attach_file WHERE file_path='2022/05/bc73d98c6fb944e18332add0ba80370c.jpg'"
# res = mysql.get_datas(sql=sql)
# print(res)

# mysql.get_dict_data(sql="SELECT id,mobile_code FROM tz_sms_log   ORDER BY id LIMIT 1")
# mysql.close_mysql()