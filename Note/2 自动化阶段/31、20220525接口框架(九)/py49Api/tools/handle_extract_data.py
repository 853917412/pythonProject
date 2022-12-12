"""
============================
Project: py49Api
Author:柠檬班-海励
Time:2022/5/16 21:44
E-mail:2227092769@qq.com
Company:湖南零檬信息技术有限公司
Site: http://www.lemonban.com
Forum: http://testingpai.com 
============================
"""
import json
from jsonpath import jsonpath

from tools.handle_attribute import HandleAttribute

class HandleExtract:
    """
    目标是从响应结果中提取参数(access_token)
    1、要提取谁
    2、怎么提取

    思路：
    1、在excel中增加字段extract_data，用来存放需要提取的key和提取表达式
       {"access_token":"$..access_token","key2":"$..key2"}
    2、获取到extract_data，转成python对象
    3、遍历extract_data的key,value，拿value(提取表达式)去响应结果中去获取数据
    4、拿到数据之后，key作为全局变量的key，value(提取表达式)拿到的数据做为value，设置为全局属性
    """
    def handle_extract(self,extract_data:str,response:dict):
        if extract_data:
            #将excel中的extract_data转换成python对象
            extract_data = extract_data if isinstance(extract_data,dict) else json.loads(extract_data)
            for key,value in extract_data.items():
                val = jsonpath(response,value)[0]
                setattr(HandleAttribute,key,val)
        else:
            print("excel中extract_data为空，不需要提取全局变量")






























