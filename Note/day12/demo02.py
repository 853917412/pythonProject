"""
============================
Project: py49
Author:柠檬班-海励
Time:2022/4/6 20:46
E-mail:2227092769@qq.com
Company:湖南零檬信息技术有限公司
Site: http://www.lemonban.com
Forum: http://testingpai.com 
============================
"""
"""
这里是重新讲解类和对象的概念

"""
class People:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def work(self):
        print(self.name,"去工作了 ")
    def eating(self):
        print(self.name,"去吃饭了")

if __name__ == '__main__':
    # 对象
    people1=People(name="小明",age="20")
    people1.work()
    # 对象
    people2 = People(name="小红", age="18")
    people2.eating()