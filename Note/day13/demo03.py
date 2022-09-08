"""
============================
Project: py49
Author:柠檬班-海励
Time:2022/4/8 20:34
E-mail:2227092769@qq.com
Company:湖南零檬信息技术有限公司
Site: http://www.lemonban.com
Forum: http://testingpai.com 
============================
"""
"""
封装
"""
class Test:
    def __test_01(self,x,y):
        if not isinstance(x,int):
            x = int(x)
        if not isinstance(y,int):
            y = int(y)
        return x,y

    def test_02(self,x,y):
        x,y = self.__test_01(x,y)
        return x+y

    def test_03(self,x,y):
        x,y = self.__test_01(x,y)
        return x*y

if __name__ == '__main__':
    cl = Test()
    print(cl.test_02("2","3"))
    print(cl.test_03("2","3"))

