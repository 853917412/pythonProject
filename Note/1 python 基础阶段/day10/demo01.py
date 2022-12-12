"""
============================
Project: py49
Author:柠檬班-海励
Time:2022/3/30 20:21
E-mail:2227092769@qq.com
Company:湖南零檬信息技术有限公司
Site: http://www.lemonban.com
Forum: http://testingpai.com 
============================
"""
import time


from day10.day101.demo02 import test_demo1
"""
模块导入
一、概念理解
1、模块：.py文件就是模块
2、包：目录下有一个__init__.py文件的就叫包，包是用来管理模块的
      如果包下面没有__init__.py，那么包下面的模块无法被导入使用
3、包和目录的区别：包有一个__init__.py文件，目录没有这个文件

二、包管理/模块管理/python库管理
1、pip 管理工具：用来管理python包
2、为什么要用pip：解决安装包依赖问题A,B,C,A,相当于centos的yum, mac：brewHome
3、基本操作
   1、安装：pip install -i http://pypi.douban.com/simple/ package_name
   2、卸载：pip uninstall package_name
   3、更新：pip install -U package_name
   4、查询：pip list  
           pip3.8 list | findstr req  模糊过滤搜索包(win)
           pip3.8 list | grep req  模糊过滤搜索包(mac、linux)
   5、升级pip：python -m pip3.8 install --upgrade pip
   6、虚拟环境相关
      pip  freeze > test.txt   导出依赖包名称和版本号
      pip install -r test.txt  根据文件安装包

三、模块导入(包的导入)
1、模块导入分类
   1、python自带模块
   2、第三方模块
   3、自定义的模块
2、导入场景
   1、导入同一个包下面的模块
      1.1、import demo02  导入对应的模块
           import day10.day101.demo02 as test
           test.test_demo1()
      1.2、from day10.demo02 import test_demo  导入目标函数或者变量
   2、不同包下导入模块
      from day10.demo02 import test_demo 
   3、自动导入包
      鼠标聚焦到包名称上  alt + 回车键 
   4、跨项目导包
      from project_name.day10.demo02 import test_demo 
3、可能遇到的错误
   1、导入包有波浪线：选择解释器并没有安装对应的包，解释器选择错了
   2、标识符命名和包名称重复了
   3、pycharm识别不到你的包,make directory as SourcesRoot
"""


import sys

print(sys.path)




# import demo02

# from day10.day101.demo02 import test_demo

# import day10.day101.demo02 as test
# test.test_demo1()

# from .day101.demo02 import test_demo
# test_demo()

# test.test_demo1()




















