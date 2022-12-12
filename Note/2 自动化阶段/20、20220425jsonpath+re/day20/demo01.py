"""
============================
Project: py49
Author:柠檬班-海励
Time:2022/4/25 20:05
E-mail:2227092769@qq.com
Company:湖南零檬信息技术有限公司
Site: http://www.lemonban.com
Forum: http://testingpai.com 
============================
"""
"""
一、数据提取
1、jsonpath：从json数据(dict)里面提取数据
2、re：从字符串提取数据

二、使用场景
1、参数依赖问题：A接口返回值需要用到B接口作为请求参数
2、技术是为业务服务的

三、python中的json数据处理
将json数据转换成json字符串类型
dict_str = json.dumps(test_dict)
将jsonstr转成dict(json)
res = json.loads(dict_str)



"""
import json
# null == None   true == True
test_dict = {"key1":False,"key2":None,"key3":True}
print(type(test_dict))

#jsonstr
# 将json数据转换成json字符串类型
dict_str = json.dumps(test_dict)
print(type(dict_str))
print(dict_str)

# 将jsonstr转成dict(json)
res = json.loads(dict_str)
print(res)










