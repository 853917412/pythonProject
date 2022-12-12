"""
============================
Project: py49
Author:柠檬班-海励
Time:2022/3/25 21:42
E-mail:2227092769@qq.com
Company:湖南零檬信息技术有限公司
Site: http://www.lemonban.com
Forum: http://testingpai.com 
============================
"""
"""
一、函数
1、什么是函数：可以被其他程序引用的程序或者代码
2、python内置函数，能直接使用：print()  str()   list()   tuple()  type()  id()  del()  set()  input()  max()  min()   sum()
3、自定义函数
语法：
def test_01():
print("这里是自定义函数") #代码块
return "success"   #返回值
调用：test_01()
    自定义的函数需要调用才会执行
函数返回值：
    return 是函数返回值的关键字，可以写，也可以不写
    需要函数返回数据的时候，就写return
    如果写了return 后面不跟参数，默认返回None
    如果不写return 默认返回None
    return 可以返回多个值，用逗号隔开(可以是变量，也可以是具体的值)
函数和方法作用都是一样的


拓展：函数与方法区别
通过类名调用的实例方法就叫函数
通过实例对象调用的实例方法就叫方法
调用自动传self或者cls 这个就是方法
调用手动显式传self或者cls 这个就是函数
class Test:
    def test(self):
        pass
"""


# def test_01():
#     print("这里是自定义函数")
#     test_list = [1,2,3]
#     return test_list,23
# result,num = test_01()
# print(result)
# print(num)


def test_02(x,y):
    return x+y
res = test_02(1,2)
print(res)

# 通过类名调用的实例方法就叫函数
# 通过实例对象调用的实例方法就叫方法
# 调用自动传self或者cls 这个就是方法
# 调用手动显式传self或者cls 这个就是函数
# class Test:
#     def test(self):
#         pass
