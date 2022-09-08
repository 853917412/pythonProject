"""
============================
Project: py49
Author:柠檬班-海励
Time:2022/4/6 21:17
E-mail:2227092769@qq.com
Company:湖南零檬信息技术有限公司
Site: http://www.lemonban.com
Forum: http://testingpai.com 
============================
"""
"""
类的特性
1、属性
2、方法

一、概念理解
1、继承：子类继承父类的方法和属性(私有方法和属性不能被继承)
        理解：子承父业，儿子继承爸爸的财产
2、封装：
3、多态：

二、继承
单继承
1、语法：class Son(父类名称):
2、子类调用父类的方法和属性
   1、子类自己没有实现对应的方法和属性
      调用父类的方法和属性
   2、子类自己实现了对应的方法和属性
      调用自己的方法和属性
   3、self 和 super的区别
      self.money()   调用顺序，先从自己的类里面找money方法，如果找到了就执行，不去父类找
      super().money()调用顺序，直接从父类找money方法
   4、调用父类的初始化方法(__init__)
      self.__init__() #不用
      super().__init__()
      
3、类实例化过程
   1、执行__new__方法创建对象
   2、自动执行__init__方法
   
多继承
1、语法：class Son(父类名称1,父类名称2):
三、封装

四、多态

"""
# 爸爸类
class Dad(object):

    def __init__(self,name):
        self.name = name
        print("爸爸的初始化方法",name)

    def money(self):
        print("爸爸这有10个亿")

class Son(Dad):
    def __init__(self,name):
        self.name = name
        print("儿子的初始化方法")
        super().__init__(name)

    def money(self):
        print("儿子这有1个亿")

    def get_money(self):
        self.money() # 调用顺序，先从自己的类里面找money方法，如果找到了就执行，不去父类找
        # Dad(name="test").money() # 不要这样用
        # super().money() #调用顺序，直接从父类找money方法

if __name__ == '__main__':
    cl = Son("王")
    # print(cl.name)
    # cl.money()
    cl.get_money()


