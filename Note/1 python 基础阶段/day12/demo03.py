"""
============================
Project: py49
Author:柠檬班-海励
Time:2022/4/6 20:54
E-mail:2227092769@qq.com
Company:湖南零檬信息技术有限公司
Site: http://www.lemonban.com
Forum: http://testingpai.com 
============================
"""
"""
私有方法
类方法、实例方法、静态方法都可以写成私有方法
调用方式不变，只是改变了它的作用域
一、创建
1、双下划线创建
def __test_03(self)
2、访问
只能在类的内部访问
单下划线命名的私有方法虽然可以在类外面访问，但是不建议去访问，潜规则
强行访问
"""
class TestDemo:

    def test_01(self):
        print("test_01")

    def test_02(self):
        print("test_02")
        self.__test_03()
        self.__test_04()

    def __test_03(self):
        print("__test_03私有方法")

    @classmethod
    def __test_04(cls):
        print("__test_04私有方法")

if __name__ == '__main__':
    cl = TestDemo()
    cl.test_02()
    # cl.__test_03()  #不能在外部访问
    # cl._TestDemo__test_03() # 强行访问
    print(TestDemo.__dict__) # 查看属性名称