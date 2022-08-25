"""
============================
Project: py49
Author:柠檬班-海励
Time:2022/3/18 21:50
E-mail:2227092769@qq.com
Company:湖南零檬信息技术有限公司
Site: http://www.lemonban.com
Forum: http://testingpai.com 
============================
"""
"""
元组
一、特性
1、元组的内容可以重复
2、元组本身不可修改
3、只有一个元素，一定要加逗号
4、可迭代
5、元素类型可以不一致
6、支持嵌套其他数据类型

二、创建
如果只有一个元素，一定要加逗号
test_tuple = (1,2,3,4)
三、查询
1、索引获取
res = test_tuple[0]
2、切片
字符串、列表、元组切片一样
res = test_tuple[0:3]
res = test_tuple[-1:-3:-1]

四、元组的运算
test_tuple1=(1,2,3)
test_tuple2=('a','b','c')
tuple3 = test_tuple1+test_tuple2

五、元组的可变与不可变
1、元组内部嵌套了可变数据类型，可以修改可变数据类型
"""
test_tuple1=(1,2,3,['a','b','c'])

# test_tuple1[-1][0]="aaaaa"
# print(test_tuple1)

# test_tuple1[0]=100  不可以修改

print(test_tuple1)

test_str = "fff"

# test_tuple2=('a','b','c')
# tuple3 = test_tuple1+test_tuple2
# print(tuple3)
# print(test_tuple1)
# print(test_tuple2)

# test_tuple = ("aaaaa",1,2,2,3,4)
# print(test_tuple,type(test_tuple))
# print(test_tuple[0])
# print(test_tuple[0:3])
# print(test_tuple[-1:-3:-1])

# for i in test_tuple:
#     print(i)
