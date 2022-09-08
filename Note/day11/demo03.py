"""
============================
Project: py49
Author:柠檬班-海励
Time:2022/4/1 20:46
E-mail:2227092769@qq.com
Company:湖南零檬信息技术有限公司
Site: http://www.lemonban.com
Forum: http://testingpai.com 
============================
"""

class Dog:
    def __init__(self,name,age):
        self.name = name  # 不加self命名只是init方法的局部变量
        self.age = age  #实例属性
        print("类实例属性：",name)

    def test_01(self):
        print(self.name)
        print(self.age)

    def test_02(self):
        print(self.name)
        print(self.age)


my_dog = Dog(name="小白",age=20)
# print(my_dog.name)
# print(my_dog.age)

my_dog.test_01()