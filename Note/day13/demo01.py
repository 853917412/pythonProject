"""
============================
Project: py49
Author:柠檬班-海励
Time:2022/4/8 19:20
E-mail:2227092769@qq.com
Company:湖南零檬信息技术有限公司
Site: http://www.lemonban.com
Forum: http://testingpai.com 
============================
"""
"""
一、多继承
1、语法：class Son(父类名称1,父类名称2):
2、多继承与单继承的区别
   1、多继承函数的查找顺序，会从左往右从父类去找，找到了就执行
   2、继承的父子关系不能乱继承，MRO表会错乱(记录类之间的继承关系的)
3、继承的使用场景
   1、重写父类的方法
class Test01:
    def test_01(self):
        print("Test01 的 test_01")

class Test02(Test01):
    def test_01(self):
        print("Test02 的 test_01")

if __name__ == '__main__':
    cl = Test02()
    cl.test_01()
    2、修改父类方法的功能
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
    
二、封装
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

三、多态
定义：多态性是指一个接口，多种实现，不同功能的函数可使用相同函数名，
     这样就可以用一个函数名调用不同的函数实现。
     
四、动态设置属性
给谁设置属性就通过谁去获取属性(类、对象)
动态设置的属性，不要显式调用
1、setattr(cl,"first_name","王") # 设置属性
2、first_name = getattr(cl,"first_name","张") # 获取属性，可以设置默认值
3、delattr(cl,"last_name") 删除对应的属性，属性不存在会报错
4、res = hasattr(cl,"age") 判断属性是否存在，返回布尔值

五、路径处理
1、返回当前文件的绝对路径
	print(__file__)
2、返回当前运行文件所在【目录的绝对路径】
	os.path.dirname(__file__)
3、返回当前进程的工作目录(pycharm工作空间)
	os.getcwd()
4、获取指定文件的绝对路径
	os.path.abspath('demo01.py')
	
5、路径拼接
base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
for path in ["day01","day02","day03"]:
    res_path = os.path.join(base_dir,path,"demo01.py")
    print(res_path)
6、拓展
res_path = os.path.join("api",r"\test","demo01.py")
res_path = os.path.join("api/","test/","demo01.py")
print(res_path)

"""
class Test01: # 父  父
    def __init__(self):
        print("Test01  的 __init__")

    def test_01(self):
        print("Test01 的 test_01")

class Test02: # 子   父
    def __init__(self):
        print("Test02  的 __init__")

    def test_01(self):
        print("Test02 的 test_01")

    def test_02(self):
        print("Test02 的 test_02")

class Test03(Test01,Test02):# 子  子
    def __init__(self):
        super().__init__()
        print("Test03  的 __init__")
        super().test_02() #调父类的方法
        Test02().__init__() # 调Test02的初始化方法

if __name__ == '__main__':
    cl = Test03()
    # cl.test_01()
    # cl.test_02()