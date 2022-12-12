"""
============================
Project: py49Api
Author:柠檬班-海励
Time:2022/5/23 21:53
E-mail:2227092769@qq.com
Company:湖南零檬信息技术有限公司
Site: http://www.lemonban.com
Forum: http://testingpai.com 
============================
"""

from faker import Faker

from tools.handle_mysql import mysql



class HandlePhone:
    def __init__(self):
        self.fk = Faker(locale="zh-cn")


    def __check_phone(self,phone):
        sql = "SELECT * FROM  `tz_user` WHERE  user_mobile ='{}'".format(phone)
        print("sql语句：",sql)
        result = mysql.get_datas(sql=sql)
        print("数据库返回",result)
        return result

    def get_phone(self):
        #生成手机号
        #校验手机号是否注册了，如果注册了，就重新生成，未注册就返回
        while True:
            phone = self.fk.phone_number()
            print(phone)
            result = self.__check_phone(phone=phone)
            if len(result) >0:
                #查询结果长度大于0那就说明数据库已经存在这个数据，就继续循环
                continue
            else:
                #手机号没有注册过，直接返回手机号，循环就退出了
                print("这个手机号未注册",phone)
                return phone




if __name__ == '__main__':
    cl = HandlePhone()
    cl.get_phone()


