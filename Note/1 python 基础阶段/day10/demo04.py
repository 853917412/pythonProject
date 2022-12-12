"""
============================
Project: py49
Author:柠檬班-海励
Time:2022/3/30 22:04
E-mail:2227092769@qq.com
Company:湖南零檬信息技术有限公司
Site: http://www.lemonban.com
Forum: http://testingpai.com 
============================
"""
"""
step into: 进入引用的函数内部去

"""

def test_01():
    print("test_01")
    print("test_01")
    print("test_01")
    print("test_01")
    print("test_01")

def test_02(num):
    if num >0:
        print("test_02")
        print("test_02")
        test_01()
        print("test_02")
    else:
        print("test")

test_02(10)