"""
============================
Project: py49
Author:柠檬班-海励
Time:2022/3/28 20:58
E-mail:2227092769@qq.com
Company:湖南零檬信息技术有限公司
Site: http://www.lemonban.com
Forum: http://testingpai.com 
============================
"""
"""
二、拆包
1、赋值
num1,num2 = (10,20)
print(num1,num2)

2、*解包(list、tuple、set)
def test_01(name,age):
    print("test_01的参数",name,age)
test_list = ["张三",20] 
test_01(*test_list) #test_01(*test_list) == test_01("张三",20)

3、**解包字典
def test_01(**kwargs):
    print("test_01的参数",kwargs)
test_dict = {"name":"张三","age":"23"}
test_01(**test_dict) #test_01(**test_dict) == test_01(name="张三",age="20")

def test_01(name,age):
    print("test_01的参数",name,age)
test_dict = {"name":"张三","age":"23"}
test_01(**test_dict) #test_01(**test_dict) == test_01(name="张三",age="20")
"""

def test_01(name,age):
    print("test_01的参数",name,age)
test_dict = {"name":"张三","age":"23"}
test_01(**test_dict) #test_01(**test_dict) == test_01(name="张三",age="20")


