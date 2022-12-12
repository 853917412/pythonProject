"""
============================
Project: py49
Author:柠檬班-海励
Time:2022/4/20 20:05
E-mail:2227092769@qq.com
Company:湖南零檬信息技术有限公司
Site: http://www.lemonban.com
Forum: http://testingpai.com 
============================
"""
"""
一、数据库封装


"""

from settings import mysql_info1,mysql_info2
import pymysql

class HandleDb:
    def __init__(self,mysql_info):
        self.db = pymysql.connect(
                            host=mysql_info["host"],
                            port=mysql_info["port"],
                            user=mysql_info["user"],
                            password=mysql_info["password"],
                            database=mysql_info["database"],
                            charset="utf8",
                            autocommit=True,
                            cursorclass=pymysql.cursors.DictCursor
                        )
        self.cur = self.db.cursor()

    # 后置
    def close_mysql(self):
        self.cur.close()
        self.db.close()

    def get_datas(self,sql):
        self.cur.execute(sql)
        result = self.cur.fetchall()
        self.close_mysql()
        return result

mysql1 = HandleDb(mysql_info1) # 数据库1
mysql2 = HandleDb(mysql_info2) # 数据库2


