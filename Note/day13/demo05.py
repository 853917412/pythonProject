"""
============================
Project: py49
Author:柠檬班-海励
Time:2022/4/8 20:56
E-mail:2227092769@qq.com
Company:湖南零檬信息技术有限公司
Site: http://www.lemonban.com
Forum: http://testingpai.com 
============================
"""
"""
四、动态设置属性
给谁设置属性就通过谁去获取属性(类、对象)
动态设置的属性，不要显式调用
1、setattr(cl,"first_name","王") # 设置属性
2、first_name = getattr(cl,"first_name","张") # 获取属性，可以设置默认值
3、delattr(cl,"last_name") 删除对应的属性，属性不存在会报错
4、res = hasattr(cl,"age") 判断属性是否存在，返回布尔值
"""
class TestDemo:
    age = 10
    def __init__(self,name):
        self.name = name

    def test_01(self):
        setattr(TestDemo, "first_name", "张")
        print(self.first_name)   # 不要显示调用

if __name__ == '__main__':
    # setattr(TestDemo,"name","张")
    print(TestDemo.__dict__)

    cl = TestDemo("张")
    cl.test_01()



    # cl = TestDemo("py49")
    # print(cl.__dict__) # 打印实例的属性
    # print(TestDemo.__dict__) #打印类的属性
    # setattr(cl,"first_name","王") # 设置属性
    # print(cl.__dict__)
    # setattr(cl,"age","李") # 设置属性
    # first_name = getattr(cl,"first_name","张") # 获取属性
    # print(first_name)
    # # delattr(cl,"last_name") #删除属性
    # res = hasattr(cl,"age")
    # print(res)
    # print(cl.__dict__)
    # print(TestDemo.__dict__)  # 打印类的属性



