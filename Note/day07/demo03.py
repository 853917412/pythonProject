"""
============================
Project: py49
Author:柠檬班-海励
Time:2022/3/23 21:12
E-mail:2227092769@qq.com
Company:湖南零檬信息技术有限公司
Site: http://www.lemonban.com
Forum: http://testingpai.com 
============================
"""
"""
一、数据类型转换
1、可以直接相互转换
int >> str
str >> int
num = 123
print(type(num),num)
new_num = str(num)
print(type(new_num),new_num)


list >> tuple
tuple >> list
test_list = ['a','b','c']
print(type(test_list),test_list)
new_tuple = tuple(test_list)
print(type(new_tuple),new_tuple)
new_list = list(new_tuple)
print(type(new_list),new_list)


list >> set
set >> list 
会去重处理
顺序会改变
test_list = ['a','b','c']
print(type(test_list),test_list)
new_set = set(test_list)
print(type(new_set),new_set)
new_list = list(new_set)
print(type(new_list),new_list)


tuple >> set
set >> tuple
会去重处理
顺序会改变
test_list = ('a','b','c')
print(type(test_list),test_list)
new_set = set(test_list)
print(type(new_set),new_set)
new_list = tuple(new_set)
print(type(new_list),new_list)


2、不能直接相互转换的
str >> tuple
str >> list
str >> set

"""

test_str = "hello"

new_tuple = set(test_str)
print(new_tuple,type(new_tuple))
new_str = str(new_tuple)
print(new_str,type(new_str))


# num = 123
# print(type(num),num)
# new_num = str(num)
# print(type(new_num),new_num)
# new_num2 = int(new_num)
# print(type(new_num2),new_num2)

# test_list = ('a','b','c')
# print(type(test_list),test_list)
# new_set = set(test_list)
# print(type(new_set),new_set)
# new_list = tuple(new_set)
# print(type(new_list),new_list)
