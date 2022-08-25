"""
============================
Project: py49
Author:柠檬班-海励
Time:2022/3/23 21:28
E-mail:2227092769@qq.com
Company:湖南零檬信息技术有限公司
Site: http://www.lemonban.com
Forum: http://testingpai.com 
============================
"""
"""
input函数
1、获取用户输入都是str类型
2、相同的数据类型才能比较

控制流
一、流程概念
1、什么叫流程：做一件事情的先后顺序
2、流程的分类：
   顺序结构: 代码重上往下执行
   选择结构：代码根据你的条件执行
   循环结构：某一段代码重复执行


二、选择结构
1、单if语句
num = 10
if num >20:
    print(num)
2、if-else
num = 10
if num >20:
    print(num)
else:
    print("num 不大于 20 ")
    
三、断点调试
step over (F8): 执行下一步
resume program(F9): 跳到下一个断点处
evaluate：打开代码执行框
stop：退出断点




"""
# print("顺序结构")
# print("选择结构")
# print("循环结构")

# input 获取用户输入都是str类型
num = input("获取用户输入：")
if num >str(20):
    print(num)
elif str(15) > num > str(10):
    print("num 不大于 10 ")
elif num >= str(15):
    print("num 不大于 15 ")
    if num == str(15):
        print("num 等于15")
    else:
        print("num 不等于15")
else:
    print("num 不大于 20 ")






