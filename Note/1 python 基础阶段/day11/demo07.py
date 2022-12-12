"""
============================
Project: py49
Author:柠檬班-海励
Time:2022/4/1 21:37
E-mail:2227092769@qq.com
Company:湖南零檬信息技术有限公司
Site: http://www.lemonban.com
Forum: http://testingpai.com 
============================
"""
"""
类方法
1、使用装饰器@classmethod
2、第一个参数必须是当前【类本身】，该参数名一般约定为"cls"
3、类方法可以被【类】+【类实例】调用
4、类内部：self.方法名称()、类.方法名称()
5、类外部：类.方法名称()、类实例.方法名称()
6、不可以使用【实例属性】、【实例方法】
7、使用场景：方法内部不需要使用实例属性和实例方法，适合定义类方法

作者：haili
链接：http://testingpai.com/article/1646382284753


"""
class Dog:

    def __init__(self):
        self.name = "jack"  #实例属性，实例属性只能被实例调用

    #实例方法
    def test_01(self):
        # self.test_02() # 类实例调用类方法
        Dog.test_03()  # 类调用类方法

    #类方法
    @classmethod
    def test_02(cls):  # cls 是类
        print("打印cls",id(cls))
        print("类方法test_02")
        Dog.test_03()  # 类调用类方法
        cls.test_03() # 类调用类方法
        # print(cls.name)  # 不能访问实例属性

    #类方法
    @classmethod
    def test_03(cls):
        print("打印cls",id(cls))
        print("类方法test_03")

if __name__ == '__main__':
    cl = Dog()
    cl.test_01()

    # cl.test_02()
    # print(id(Dog))
    # Dog.test_02()
    # Dog.test_03()
