"""
============================
Project: py49
Author:柠檬班-海励
Time:2022/3/28 21:25
E-mail:2227092769@qq.com
Company:湖南零檬信息技术有限公司
Site: http://www.lemonban.com
Forum: http://testingpai.com 
============================
"""
"""
三、变量的作用域
局部变量：写在函数里面，只在当前函数起作用
全局变量：写在函数外面，对整个模块或者类起作用
name = "张三" #全局变量
def test_01():
    # name = "张三" # 局部变量
    print(name)
def test_02():
    print(name)
test_01()
test_02()

global关键字：将局部变量定义为全局变量
1、先声明为全局变量，再赋值


"""




def test_01():
    global name
    name = "张三"
    print(name)
def test_02():
    print(name)
test_01()
test_02()