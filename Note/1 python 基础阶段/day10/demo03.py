"""
============================
Project: py49
Author:柠檬班-海励
Time:2022/3/30 21:23
E-mail:2227092769@qq.com
Company:湖南零檬信息技术有限公司
Site: http://www.lemonban.com
Forum: http://testingpai.com 
============================
"""
"""
异常处理
一、概念理解
1、什么是异常：程序运行过程中出现了错误，无法继续执行代码了


二、异常的类型
1、导包错误
ImportError

2、参数传递错误
TypeError: test_demo() missing 1 required positional argument: 'name'

3、找不到变量
NameError: name 'first_name' is not defined

4、下标越界
IndexError: list index out of range

5、字典的key不存在
KeyError: 'key3'

6、属性错误
AttributeError: type object 'Test' has no attribute 'name'

三、异常捕获(处理异常)
1、try......except
try:
    执行中可能会报错的代码
except Exception as e:
    报错后会执行的代码
    代码报错之后怎么处理的代码
    获取到错误的类型print(e)
    
2、try......except......else
try:
    print("执行可能会报错的代码")
except Exception as e:
    print("如果执行报错了会执行的代码")
else:
    print("如果执行没有报错会执行的代码")

3、try......except......else......finally
    try:
        print("执行可能会报错的代码")
    except Exception as e:
        print("如果执行报错了会执行的代码")
    else:
        print("如果执行没有报错会执行的代码")
    finally:
        print("不管是否报错都会执行的代码")
        
4、手动抛出异常
raise TypeError("手动抛出异常")
unittest框架断言
"""


import traceback

def test_01(name,age):
    try:
        print("执行可能会报错的代码")
        print(name)
        raise TypeError("手动抛出异常")
    except Exception as e:
        print(e)
        # print(traceback.print_exc()) # 只是把错误信息展示出来，对代码执行没有影响
test_01(name="老王",age=20)






# def test_01(name,age):
#     try:
#         print("执行可能会报错的代码")
#         print(name)
#         # print(age1)
#     except Exception as e:
#         print("如果执行报错了会执行的代码")
#         print(e)
#     else:
#         print("如果执行没有报错会执行的代码")
#     finally:
#         print("不管是否报错都会执行的代码")
# test_01(name="老王",age=20)




# def test_01(name,age):
#     try:
#         print("执行可能会报错的代码")
#         print(name)
#         print(age1)
#     except Exception as e:
#         print("如果执行报错了会执行的代码")
#         print(e)
#     else:
#         print("如果执行没有报错会执行的代码")
# test_01(name="老王",age=20)



# def test_01(name,age):
#     try:
#         print(name)
#         try:
#             print(test_naem)
#         except Exception as e:
#             print("pass")
#         print(age)
#     except Exception as e:
#         print(e)
# test_01(name="老王",age=20)


# class Test:
#     name="test"
# print(Test.name)



# test_dict = {"key1":"val1","key2":"val2"}
# print(test_dict["key3"])


# from day10.demo02 import test_demo
# first_name="王"


# test_list = ['a','b','c']
# print(test_list[10])


