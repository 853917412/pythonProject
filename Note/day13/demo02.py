"""
============================
Project: py49
Author:柠檬班-海励
Time:2022/4/8 20:25
E-mail:2227092769@qq.com
Company:湖南零檬信息技术有限公司
Site: http://www.lemonban.com
Forum: http://testingpai.com 
============================
"""
import time

class Test01:
    def test_01(self):
        time.sleep(2)
        print("Test01 的 test_01")
        return "success"

class Test02(Test01):
    def test_01(self):
        start = time.time()
        res = super().test_01()
        end = time.time()
        result = end - start
        print("函数执行耗时：",result)
        print("Test02 的 test_01")
        return res,result

if __name__ == '__main__':
    cl = Test02()
    res,result = cl.test_01()
    print(res,result)