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

class HandleReplace:

    #根据替换数据的来源，获取数据，再设置为类属性(全局变量)
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
            print(f"需要替换key={key}")
            times = int(time.time() * 1000)
            setattr(HandleAttribute, key, times)
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
            # 拿到需要替换的key
            key_list = re.findall("#(\w.+?)#",data)
            if len(key_list)>0:
                #将需要替换的数据设置为类属性，用来替换
                for key in key_list:
                    # 获取数据并设置为类属性
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




