"""
============================
Project: py49
Author:柠檬班-海励
Time:2022/4/18 21:37
E-mail:2227092769@qq.com
Company:湖南零檬信息技术有限公司
Site: http://www.lemonban.com
Forum: http://testingpai.com 
============================
"""
"""
查询最大连接数
SHOW VARIABLES LIKE  "%max_connections%"
修改最大连接数
SET GLOBAL max_connections = 300

数据库信息：
mysql_info = {
    "host":"47.113.180.81",
    "port":3306,
    "user":"lemon",
    "password":"lemon123",
    "db":"yami_shops",
}


一、安装pymysql
pip install pymysql
PyMySQL==1.0.2


二、使用
1、建立数据库连接
db = pymysql.connect(
                    host="47.113.180.81",
                    port=3306,
                    user="lemon",
                    password="lemon123",
                    database="yami_shops",
                    charset="utf8",
                    autocommit=True
                )
2、创建游标
cur = db.cursor()
3、执行sql语句
cur.execute("SELECT * FROM tz_brand")
4、获取sql语句查询结果：默认返回元组
   1、获取所有的数据
   result = cur.fetchall()
   2、获取指定条数的数据
   result = cur.fetchmany(3) == SELECT * FROM tz_brand ORDER BY brand_id ASC LIMIT 3
   3、获取到查询的第一条数据，然后返回
   result = cur.fetchone()
5、返回数据设置
   1、默认返回嵌套元组，一行数据为元组的一个元素
   2、cursorclass=pymysql.cursors.DictCursor 返回字典数据
"""

import pymysql


db = pymysql.connect(
                    host="47.113.180.81",
                    port=3306,
                    user="lemon",
                    password="lemon123",
                    database="yami_shops",
                    charset="utf8",
                    autocommit=True,
                    cursorclass=pymysql.cursors.DictCursor
                )
cur = db.cursor()

sql = "SELECT * FROM tz_brand"
cur.execute(sql)
# cur.execute("SELECT * FROM tz_brand")


# result = cur.fetchall()
# result = cur.fetchmany(2)
result = cur.fetchone()
# print(len(result))
print(result)
cur.close()
db.close()



















