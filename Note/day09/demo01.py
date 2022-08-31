"""
============================
Project: py49
Author:柠檬班-海励
Time:2022/3/28 20:27
E-mail:2227092769@qq.com
Company:湖南零檬信息技术有限公司
Site: http://www.lemonban.com
Forum: http://testingpai.com 
============================
"""
"""
函数的参数
一、概念
1、形参：形式参数，占个坑，表示这里有值，具体是什么值，不知道。
2、实参：函数运行过程中的实际参数。

二、参数分类
1、必须参数: 调用函数的时候必须要传的参数，不传会报错
多个参数必须按顺序传递，否则参数会错位
def test_01(name,age):
    print("test_01的参数",name,age)
test_01("老王",20)

2、关键字参数
通过赋值的方式传参
def test_01(name,age):
    print("test_01的参数",name,age)
test_01(age=20,name="老王")

3、默认参数: 定义参数的时候给个默认值
必须写在必须参数的后面
默认参数可以不传参数，如果传参就使用传入的参数，如果不传参，默认使用默认值
def test_01(name,age=18):
    print("test_01的参数",name,age)
test_01(name="老王",age=24)

4、不定长参数
*args: 接收多个必须参数，会收集到元组当中
def test_01(*args):
    print("test_01的参数",args)
test_01("老王",24,175)

**kwargs：接收多个关键字参数，会收集到字典当中
def test_01(**kwargs):
    print("test_01的参数",kwargs)
test_01(name="张三",age=24,high=175)

def test_01(*args,**kwargs):
    print("args参数：",args)
    print("test_01的参数",kwargs)
test_01("a","b","c",name="张三",age=24,high=175)



"""
def test_01(*args,**kwargs):
    print("args参数：",args)
    print("test_01的参数",kwargs)
test_01("a","b","c",name="张三",age=24,high=175)






