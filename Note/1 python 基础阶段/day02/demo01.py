"""
============================
Project: py49
Author:柠檬班-海励
Time:2022/3/11 19:51
E-mail:2227092769@qq.com
Company:湖南零檬信息技术有限公司
Site: http://www.lemonban.com
Forum: http://testingpai.com 
============================
"""
"""
基础阶段上课顺序
1、python3基础语法
2、python变量与标识符
3、基本数据类型
4、运算符
5、字符串
6、列表
7、元组
8、集合
9、字典
10、数据类型转换
11、控制流
12、函数
13、文件操作
14、模块导入
15、路径处理
16、异常处理
17、debug技能
18、类和对象
19、类方法、实例方法、静态方法、私有方法使用
20、类的特性
21、动态设置属性
22、阶段考试


一、pycharm工具功能区分
1、导航栏
2、代码管理区域
3、控制台
4、写代码区域

二、pycharm运行py文件
1、在需要运行的文件内，右键Run(ctrl + shift +F10)
2、工具栏上的绿色小三角形，点三角形就能运行(工作空间目录要与运行代码的py文件是同一个目录)
3、控制台的重运行按钮，小三角形(工作空间目录要与运行代码的py文件是同一个目录)

三、python3语法
语法
1、缩进：不同一个代码块的代码要进行缩进
2、换行: 不同层级的代码块要换行写
3、对齐： 同一个层级的代码块要左对齐

其他用法
1、注释代码
   #: ctrl + ？/(英文模式下)
   一对三单引号：默认
   一对三双引号：兼容

2、格式化代码：让代码更好看，不影响代码功能
   ctrl + alt + L
   
3、输出(输出到控制台)
  单行输出：print("hello python")
          续行符(\)：通过\进行续行
  分多行输出：一对三单引号、一对三双引号

4、输入(获取外部用户输入)
   price = input("请输入价格：")
   
python变量
1、变量定义：在计算机语言中存储结果或者值的抽象概念
2、变量创建: 变量名 = 值
3、变量使用：通过变量名使用
4、变量的命名规范
   1、可以由字母、数字、下划线组成
   2、不能以数字开头
   3、不建议使用中文命名(虽然可以)
   4、区分大小写
   5、不能使用关键字命名
      import keyword
      print(keyword.kwlist)
   6、见文知意

快捷键
快速复制代码：ctrl + d(复制鼠标聚焦行的代码)
快速换行：shift + 回车


标识符
1、标识符定义：用来标识某个实体(具体的某个东西)的符号
2、常见的标识符：变量、项目名称、包名称、文件名称、函数名称、类的名称、属性名称
3、标识符命名规范：同变量
4、标识符的命名风格：
  大驼峰: 每个单词的首字母都大写其他的小写（FirstName="jack")
  小驼峰：第一个单词都小写，其他后面的单词首字符都大写，非首字母小写(firstName="jack")
  下划线连接：通过下划线连接各个单词(first_name="jack") 推荐
5、建议命名风格：
   类名称：大驼峰
   函数名称：下划线连接
   变量名称：下划线连接（可读性强）
   
"""
FirstName="jack"
firstName="jack"
first_name="jack"


import time









"""

Num = 100
num = 101
name = "jack"
print(Num)
print(num)

import keyword
print(keyword.kwlist)


"""










"""
str_test = hello 
python
test


print(str_test)


# price = input("请输入价格：")
# print(price)


str_test = "hello " \
           "python"

print(str_test)

print("hello python")
print("hello java")

a1 = 100
a2 = 200
a3 = 120




print("hello python")


def test_01():
    print("test1")
    print("test2")
    print("test3")
    print("test4")

def test_02():
    print("test1")
    print("test2")
    print("test3")
    print("test4")

"""
