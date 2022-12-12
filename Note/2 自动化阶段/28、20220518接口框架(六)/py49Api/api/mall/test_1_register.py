"""
============================
Project: py49Api
Author:柠檬班-海励
Time:2022/5/9 21:50
E-mail:2227092769@qq.com
Company:湖南零檬信息技术有限公司
Site: http://www.lemonban.com
Forum: http://testingpai.com 
============================
"""
"""
有些接口需要鉴权，有些接口不需要鉴权

"""

import requests
import pymysql
from faker import Faker

class Register:
    def __init__(self):
        self.header={"locale":"zh_CN"}
        self.fk = Faker(locale="zh_CN")
        self.phone = self.fk.phone_number()
        print("手机号：",self.phone)
        self.db = pymysql.connect(
            host="47.113.180.81",
            port=3306,
            user="lemon",
            password="lemon123",
            db="yami_shops",
            autocommit=True,
            cursorclass=pymysql.cursors.DictCursor

        )
        self.cur = self.db.cursor()

    # 发送短信验证码
    def send_msg(self):
        url = "http://mall.lemonban.com:8107/user/sendRegisterSms"
        #随机生成手机号，然后去数据库查询是否已注册，
        data = {"mobile": self.phone}
        res = requests.put(url=url,json=data,headers=self.header)
        print("发送短信验证码：",res.text)

    #校验短信验证码
    def check_msg_code(self):
        url = "http://mall.lemonban.com:8107/user/checkRegisterSms"
        sql = "SELECT mobile_code FROM tz_sms_log WHERE user_phone='{}'".format(self.phone)
        self.cur.execute(sql)
        msg_code = self.cur.fetchall()[0]["mobile_code"]
        print(msg_code)
        data = {
                  "mobile": self.phone,
                  "validCode":msg_code
                    }
        res = requests.put(url=url,json=data,headers=self.header)
        print(res.text)
        self.close_db()
        setattr(self,"checkRegisterSmsFlag",res.text)
        print('属性：',self.__dict__)
        return res.text

    #用户注册
    def user_register(self):
        self.send_msg()
        sms_flag = self.check_msg_code()
        url="http://mall.lemonban.com:8107/user/registerOrBindUser"
        data = {
            "appType": 3, # 1 小程序   2 公众号   3 pc端    4 h5 页面   5 安卓      6 ios
            #"checkRegisterSmsFlag": getattr(self,"checkRegisterSmsFlag"),
            "checkRegisterSmsFlag": sms_flag,
            "mobile": self.phone,
            "userName": self.phone,
            "password": "123456",
            "registerOrBind": 1,
            "validateType": 1
        }
        res = requests.put(url=url,json=data,headers=self.header)
        print(res.text)

    #关闭数据库连接
    def close_db(self):
        self.cur.close()
        self.db.close()

if __name__ == '__main__':
    cl = Register()
    cl.user_register()



