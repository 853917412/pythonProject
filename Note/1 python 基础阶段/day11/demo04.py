"""
============================
Project: py49
Author:柠檬班-海励
Time:2022/4/1 20:59
E-mail:2227092769@qq.com
Company:湖南零檬信息技术有限公司
Site: http://www.lemonban.com
Forum: http://testingpai.com 
============================
"""


class Dog:
    name = "小白"
    __color = "白色"
    def __init__(self,weight,age):
        self.weight = weight
        self.__age = age

    def test_01(self):
        print(self.name)
        print(self.__color)
        print(self.weight)
        print(self.__age)

if __name__ == '__main__':
    my_dog = Dog(weight=20,age=10)
    # my_dog.test_01()
    print(my_dog._Dog__age) #强行访问
    print(my_dog._Dog__color)
    print(Dog.__dict__) # 输出对象的属性



