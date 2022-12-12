"""
============================
Project: py49
Author:柠檬班-海励
Time:2022/3/25 20:10
E-mail:2227092769@qq.com
Company:湖南零檬信息技术有限公司
Site: http://www.lemonban.com
Forum: http://testingpai.com 
============================
"""
"""
一、循环
1、循环概念：重复做一件事情就叫循环
2、循环分类
   1、for循环
   2、while循环
   3、嵌套循环

3、for循环
使用场景：当知道循环次数的时候，就用for循环
for val in test_list:
    print(val)


4、判断是否是可迭代对象
from collections.abc import Iterable
test_list = ['a','b','c']
res = isinstance(test_list,Iterable)
print(res)


5、while循环
使用场景：不明确循环次数的时候就用while循环
注意点：要设置退出条件，不设置退出条件就会变成死循环


6、range函数
作用：生成一个整数序列
遵循左闭右开原则
list(range(1, 10))
list(range(1, 10, 2))
list(range(-1, -10, -2))
for index in range(len(test_list)): # ==  for index in [0,1,2,3,4]:
# for index in (0,1,2,3,4):
    print('索引值：',index)
    print(test_list[index])
    
    
7、循环控制
break: 结束整个循环
for val in range(10):
    if val == 5:
        break
    else:
        print(val)
continue: 结束本次循环，继续下一次循环
for val in range(10):
    if val == 5:
        continue
    print(val)


8、嵌套循环: 尽量不要超过3层循环
双重for循环
1、外层循环执行一次，内层循环执行一遍
# 外层循环，执行2次
for val in range(2):
    #print(val)
    # 内层循环，执行2次
    for val2 in range(2):
        print("py49期")
        
双重循环while + for
while num <=5:
    for i in range(2):
        print("py49")
    num +=1
    
双重循环while + while 
while num <=10:
    while num <=5:
        print("py49")
        num += 1
    num += 1
    print(num)

课堂练习：
*
**
***
****
行是内层循环,次数固定
列是外层循环，次数不固定
关键：要找到内层循环和外层循环的关系

end参数
end=""：打印不换行
print(""):打印换行
"""

for i in range(4):
    # 第一次循环i = 0 ,内层循环 1次
    # 第一次循环i = 1 ,内层循环 2次
    # 第一次循环i = 2 ,内层循环 3次
    # 第一次循环i = 3 ,内层循环 4次
    for k in range(i+1):
        print("*",end="")
    print("")



# num = 0
# while num <=5:
#     for i in range(2):
#         print("py49")
#     num +=1

# while num <=10:
#     while num <=5:
#         print("py49")
#         num += 1
#     num += 1
#     print(num)


# while num <= 5:
#     if num == 3:
#         for i  in range(3):
#             pass
#     elif num > 2:
#         print("py49")
#         if num == 4:
#             print("py49")






"""
# 双重for循环
# 外层循环，执行2次
for val in range(2):
    #print(val)
    # 内层循环，执行2次
    for val2 in range(2):
        print("py49期")


# continue
for val in range(10):
    if val == 5:
        continue
    print(val)


test_dict = {"key1":"val1","key2":"val2","key3":"val3",}

#遍历字典默认遍历Key
for key in test_dict:
    print(key)
for key in test_dict.keys():
    print(key)
print(test_dict.keys())

# 遍历value
for value in test_dict.values():
    print(value)
print(test_dict.values())

# 同时遍历key和values
for key,value in test_dict.items():
    print(key,value)
print(test_dict.items())

num1,num2 = ('key1', 'val1')
print(num1)
print(num2)


test_str = "python"
for val in test_str:
    print(val)


for val in range(10):
    print(val)



test_list = ['a','b','c','d','e']
for val in test_list:
    print(val,type(val))
print("="*30)

for index in range(len(test_list)): # for index in [0,1,2,3,4]:
# for index in (0,1,2,3,4):
    print('索引值：',index)
    print(test_list[index])


import time
num = 0
while num <=10:
    # time.sleep(2)
    print("对不起，我错了")
    num += 1
    print(num)
print(num)




from collections.abc import Iterable
test_list = ['a','b','c']
res = isinstance(test_list,Iterable)
print(res)
for val in test_list:
    print(val)

"""







