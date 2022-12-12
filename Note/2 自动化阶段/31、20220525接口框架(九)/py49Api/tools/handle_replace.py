"""
============================
Project: py49Api
Author:柠檬班-海励
Time:2022/5/16 20:10
E-mail:2227092769@qq.com
Company:湖南零檬信息技术有限公司
Site: http://www.lemonban.com
Forum: http://testingpai.com 
============================
"""
import ast



"""

{
"t": "#times#",
"principal": "student",
"credentials": "123456a",
"sessionUUID": "#sessionUUID#",
"imageCode": "lemon"
}

"""
import re
import time
import uuid
import json


from tools.handle_attribute import HandleAttribute
from tools.handle_mysql import mysql
from tools.handle_phone import HandlePhone

class HandleReplace:
    def __init__(self):
        self.handle_phone = HandlePhone()

    #执行前置sql语句，查询数据，设置为类属性
    def setup_sql(self,setup_sql):
        """
        思路：
        1、判断excel中setup_sql字段不为空，说明需要执行sql去数据库查询数据并设置为属性，给当前接口使用
        2、替换sql语句(在sql替换的方法中判断是否需要替换sql，不需要替换就不替换)
        3、获取到替换后的sql语句并执行，拿到sql执行结果([{}])
        4、双重for循环遍历得到的list结果，再遍历每一个list元素({}),将字典的key和value设置为属性
        :param setup_sql:
        :return:
        """
        # setup_sql =  ["SELECT mobile_code FROM tz_sms_log WHERE user_phone='#mobile#'"]
        if setup_sql:
            #只有当setup_sql有值的时候才做这个事情
            for sql in json.loads(setup_sql):
                # 替换sql语句
                new_sql = self.replace_sql(sql=sql)
                # 执行sql语句
                # sql语句查询出来的数据，设置为属性(字典key就是属性的key，value就是属性的values)
                # [{'id': 8, 'mobile_code': '845508'}]
                result = mysql.get_dict_data(sql=new_sql)
                if len(result) >0:
                    # dict_data = {'id': 8, 'mobile_code': '845508'}
                    for dict_data in result:
                        #遍历字典，设置类属性
                        for key,value in dict_data.items():
                            setattr(HandleAttribute,key,str(value))
                else:
                    print("前置sql语句查询无数据，不需要设置全局属性")
        else:
            print("excel中setup_sql字段为空，不需要设置全局属性")


    #根据替换数据的来源，获取数据，再设置为类属性(全局变量)  ["times","file_path","partyCode"]
    def get_data_and_set_attr(self,key):
        if key == "sessionUUID":
            print(f"需要替换key={key}")
            if hasattr(HandleAttribute,key):
                #为了兼容图片验证码的识别，登陆接口和图片识别的接口sessionUUID必须一致
                pass
            else:
                sessionUUID = str(uuid.uuid4())
                setattr(HandleAttribute, key, sessionUUID)
        elif key == "times":
            #这里的times要覆盖掉，因为每次接口请求都是不一样的时间
            print(f"需要替换key={key}")
            times = int(time.time() * 1000)
            setattr(HandleAttribute, key, times)
        elif key == "partyCode":
            if hasattr(HandleAttribute, key):
                pass
            else:
                #partyCode字段是产品唯一标识，每个产品都不能一样，通过这个字段可以进行数据库的断言
                setattr(HandleAttribute, key, str(int(time.time() * 1000)))
        elif key == "mobile":
            if hasattr(HandleAttribute, key):
                pass
            else:
                # 生成一个未注册的手机号，设置为全局变量
                phone = self.handle_phone.get_phone()
                setattr(HandleAttribute,key,str(phone))
        else:
            print("暂不支持该类型参数替换")

    #参数替换
    def replace_data(self,data:str):
        """
        思路：
        1、首先要知道需要替换那个参数
           通过正则表达式获取需要替换的参数的值
        2、用来替换参数的数据从哪里来的
           脚本生成、其他接口响应提取、数据库查询获取、写到配置文件
        3、如何替换参数
           字符串替换数据
        :return:
        """
        # data: str
        if data:
            #拿到需要替换的key   ["times","file_path","partyCode"]
            key_list = re.findall("#(\w.+?)#",data)
            if len(key_list)>0:
                #将需要替换的数据设置为类属性，用来替换
                for key in key_list:
                    #获取数据并设置为类属性
                    self.get_data_and_set_attr(key=key)
                    # if key == "sessionUUID":
                    #     print(f"需要替换key={key}")
                    #     sessionUUID = str(uuid.uuid4())
                    #     setattr(HandleAttribute,key,sessionUUID)
                    # elif key == "times":
                    #     print(f"需要替换key={key}")
                    #     times = int(time.time() * 1000)
                    #     setattr(HandleAttribute,key,times)
                    # else:
                    #     print("暂不支持该类型参数替换")
                #替换数据
                for key in key_list:
                    data = data.replace(f"#{key}#",str(getattr(HandleAttribute,key)))
                data = json.loads(data)
                print("转换数据：",type(data),data)
                return data
            else:
                print("不需要替换参数")
                data = json.loads(data)
                return data
        else:
            print("请求参数为空，不需要进行参数替换")
            return {}

    #替换sql语句
    def replace_sql(self,sql:str):
        #1、响应结果中提取出来的，设置的类属性中
        #2、配置文件
        #3、
        # 拿到需要替换的key
        key_list = re.findall("#(\w.+?)#",sql)
        if len(key_list) > 0:
            # 将需要替换的数据设置为类属性，用来替换
            for key in key_list:
                # 获取数据并设置为类属性
                self.get_data_and_set_attr(key=key)
            #2、替换sql语句
            for key in key_list:
                sql = sql.replace(f"#{key}#",str(getattr(HandleAttribute,key)))
        else:
            print("不需要替换sql语句直接返回")
        return sql




