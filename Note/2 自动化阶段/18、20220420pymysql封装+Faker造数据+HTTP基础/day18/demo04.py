
"""
============================
Project: py49
Author:柠檬班-海励
Time:2022/4/20 21:02
E-mail:2227092769@qq.com
Company:湖南零檬信息技术有限公司
Site: http://www.lemonban.com
Forum: http://testingpai.com 
============================
"""

from faker import Faker

class TestDemo:
    def __init__(self):
        self.fk = Faker(locale="zh-cn")

    def test_01(self):
        Faker.seed(1)
        print(self.fk.name())

    def test_02(self):
        Faker.seed(1)
        print(self.fk.name())

if __name__ == '__main__':
    cl = TestDemo()
    cl.test_01()
    cl.test_02()