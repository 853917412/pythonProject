"""
============================
Project: py49
Author:柠檬班-海励
Time:2022/4/8 20:41
E-mail:2227092769@qq.com
Company:湖南零檬信息技术有限公司
Site: http://www.lemonban.com
Forum: http://testingpai.com 
============================
"""
"""
多态性: 是指一个接口，多种实现，不同功能的函数可使用相同函数名，这样就可以用一个函数名调用不同的函数实现

开发中的场景：
1、web端
2、app端
3、小程序端
class Web:
    def test_01(self):
        print("web")
        return "1"    
class App:
    def test_01(self):
        print("app")
        return "2"
class XiaoChengXu:
    def test_01(self):
        print("小程序")
        return "3"
        
def test_03(Web):
    cl = obj()
    res = cl.test_01()
    return res
    

"""
class Dog:
    def test_01(self):
        print("狗在叫")
class Cat:
    def test_01(self):
        print("猫在叫")

def test_03(obj):
    cl = obj()
    cl.test_01()

if __name__ == '__main__':
    test_03(obj=Cat)

