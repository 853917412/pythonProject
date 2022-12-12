"""
============================
Project: py49
Author:柠檬班-海励
Time:2022/4/20 20:18
E-mail:2227092769@qq.com
Company:湖南零檬信息技术有限公司
Site: http://www.lemonban.com
Forum: http://testingpai.com 
============================
"""

import pymysql
from settings import mysql_info1

with pymysql.connect(
                    host=mysql_info1["host"],
                    port=mysql_info1["port"],
                    user=mysql_info1["user"],
                    password=mysql_info1["password"],
                    database=mysql_info1["database"],
                    charset="utf8",
                    autocommit=True,
                    cursorclass=pymysql.cursors.DictCursor
                    ) as db:
    cur = db.cursor()
    cur.execute(sql="")

with open() as file:
    pass