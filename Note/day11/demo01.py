"""
============================
Project: py49
Author:柠檬班-海励
Time:2022/4/1 19:26
E-mail:2227092769@qq.com
Company:湖南零檬信息技术有限公司
Site: http://www.lemonban.com
Forum: http://testingpai.com 
============================
"""
"""
类和对象
一、概念理解
1、类：一类事物的统称(抽象)
2、对象：类的实体(具体的东西)

二、类和对象要学哪些东西
基础
1、创建类：为这一类事物定义行为和属性
   class Dog:
2、类实例化：实例化成对象
   my_dog = Dog()
   
学习内容
1、类属性
2、实例属性
3、私有属性
4、类方法
5、实例方法
6、私有方法
7、静态方法

类的特性
1、封装
2、继承
3、多态

动态属性
"""
class Dog:
    #类属性
    name = "小白"
    color = "白色"
    __weight = 10 # 类的私有属性

    #初始化函数
    def __init__(self,age,high):
        #实例属性
        self.age = age
        self.__high = high #实例的私有属性

    # 实例方法
    def eating(self):
        print("eating")

    # 私有方法
    def __sleep(self):
        print("sleep")

    @classmethod
    def test_01(cls):
        print("类方法")

    @staticmethod
    def test_02():
        print("静态方法")

my_dog = Dog(age=2,high=10) #我的狗，我自己实例化了一个狗
my_dog.eating()


