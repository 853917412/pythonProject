"""
============================
Project: py49
Author:柠檬班-海励
Time:2022/4/25 21:15
E-mail:2227092769@qq.com
Company:湖南零檬信息技术有限公司
Site: http://www.lemonban.com
Forum: http://testingpai.com 
============================
"""
"""
正则提取
1、特点
正则表达式：匹配指定规则的字符串
只能处理字符串

2、使用



"""

import re
# test_demo = "www.baidu.com.baidu"
# result = re.findall("baidu",test_demo)
# print(result)


#. 匹配任意一个字符
# test_demo = "www.baidu.com.bidu"
# result = re.findall("b.",test_demo)
# print(result)


# [] 匹配[]里面每一个字符
# test_demo = "www.baidu.com.bidu"
# result = re.findall("[bi]",test_demo)
# print(result)

# \d 单字符匹配，匹配所有的数字
# test_demo = "www.341234baidu.co324234m.bid34234u"
# result = re.findall("\d",test_demo)
# print(result)

# \D匹配非数字
# test_demo = "hello 521 python"
# result = re.findall("\D",test_demo)
# print(result)



# \s 匹配空格,一个TAB 代表2个空格
# test_demo = "hello 521 python"
# result = re.findall("\s",test_demo)
# print(result)

# \S 匹配非空格，可以用来给字符串去空格
# test_demo = "hello 521 python"
# result = re.findall("\S",test_demo)
# result = ''.join(result)
# print(result)


# 小写w 匹配非特殊字符
# test_demo = "hello&*)中国($#@!521_python"
# result = re.findall("\w",test_demo)
# print(result)

# 大写w 匹配特殊字符
# test_demo = "hello&*)中.。国($#@!521=_python"
# result = re.findall("\W",test_demo)
# print(result)


# * 匹配前一个字符出现0次或者无限次，每个字符都去匹配一次，有就返回字符串，没有就返回空
# test_demo = "hello python"
# result = re.findall("h*",test_demo)
# print(result)


# +： 匹配出现一次或者无限次
# test_demo = "got  goot  gooot  goootoo"
# result = re.findall("g.+t",test_demo)
# print(result)


# ? 非贪婪模式
# test_demo = "got  goot  gooot  goootoo"
# result = re.findall("go?",test_demo)
# print(result)

# {n}
# test_demo = "gogot goot gooot goootoo"
# result = re.findall("go{2}",test_demo)
# print(result)


# {m,n}
# test_demo = "gogot goot gooot goootoo"
# result = re.findall("go{1,3}",test_demo)
# print(result)


# 逻辑运算 or
# test_demo = "hello python"
# result = re.findall("he|py",test_demo)
# print(result)


# django 路由 ,^ 以某某开头
# test_demo = "hello python"
# result = re.findall("^he",test_demo)
# print(result)

# 以某某结尾  $
# test_demo = "hello python"
# result = re.findall("on$",test_demo)
# print(result)


#字符串数据替换
# 数据存在excel中，excel中数据都是字符串
# 请求参数：{user:"#user_name#",token:"#access_token#"}
# 响应结果：{user_name:"root",access_token:"hfakjsdhfkajkhdkjfhakjd"}


# 重点
# {user:"#user_name#",token:"#access_token#"}
test_demo = '{"user":"#user_name#","token":"#access_token#"}'
result = re.findall("#(\w.+?)#",test_demo)
print(result)

test_dict = {"user":"#user_name#","token":"#access_token#"}
for key,val in test_dict.items():
    if val.startswith("#") and val.endswith("#"):
        #删掉val中的#，再添加到list中，返回
        pass




