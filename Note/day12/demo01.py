"""
============================
Project: py49
Author:柠檬班-海励
Time:2022/4/6 20:26
E-mail:2227092769@qq.com
Company:湖南零檬信息技术有限公司
Site: http://www.lemonban.com
Forum: http://testingpai.com 
============================
"""
"""
类调用类方法、类属性+静态方法
实例调用所有的方法和属性
静态方法
一、特点
1、通过@staticmethod来修饰，没有任何参数，不需要传cls，self
2、不能使用类属性、实例属性、实例方法、类方法
3、不需要实例化类就能直接调用

二、访问
1、类实例.方法名称()
2、类.方法名称()

三、使用场景
1、方法内部不需要使用(通过cls,self)类属性，实例属性，类方法，实例方法的时候就定义静态方法
私有方法

"""
class TestDemo:
    age = 20
    def __init__(self,name):
        self.name = name

    #实例方法
    def test_01(self):
        print(self.name)
        print(self.age)
        self.test_02()
        TestDemo.test_02()

    #静态方法
    @staticmethod
    def test_02(test):
        print("静态方法")
        print(test)
        # print(age)
        TestDemo.test_03()

    @classmethod
    def test_03(cls):
        print("类方法")

if __name__ == '__main__':
    cl = TestDemo("小花")   # cl 实例
    cl.test_01()
    # TestDemo 类
    TestDemo.test_02("test")

