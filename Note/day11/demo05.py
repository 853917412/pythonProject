"""
============================
Project: py49
Author:柠檬班-海励
Time:2022/4/1 21:24
E-mail:2227092769@qq.com
Company:湖南零檬信息技术有限公司
Site: http://www.lemonban.com
Forum: http://testingpai.com 
============================
"""


class Dog01:
    name = "大黄"
    def __init__(self,age):
        self.age = age
class Dog02:
    name = "大白"
    def __init__(self,age):
        self.my_dog = Dog01(age=age)
        print(self.my_dog.name)
        print(self.my_dog.age)
        print(Dog01.name)
        print(Dog02.name)
Dog02(20)



# name="小黑"
# print(__name__) # day11.demo05
#
# if __name__ == '__main__':
#     print(__name__)
#     print(name)
