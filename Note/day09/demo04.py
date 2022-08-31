"""
============================
Project: py49
Author:柠檬班-海励
Time:2022/3/28 21:35
E-mail:2227092769@qq.com
Company:湖南零檬信息技术有限公司
Site: http://www.lemonban.com
Forum: http://testingpai.com 
============================
"""
"""
四、内置函数
1、print
2、id
3、type
4、range
5、input
6、int
7、str
8、list
9、dict
10、max
11、min
12、bool
13、sum
14、count
15、sorted
16、sort
17、len
18、float
19、set
import builtins
print(dir(builtins))

五、高阶函数
1、zip
压缩
test_list = [("key1","val1"),("key2","val2")]
print(dict(test_list))

list1 = ["key1","val1"]
list2 = ["key2","val2"]

res = list(zip(list1,list2))
print(dict(res))

list3= {'key1': 'key2', 'val1': 'val2'}
print(list(list3.items()))

解压缩
list1 = ["key1","val1"]
list2 = ["key2","val2"]
res = list(zip(list1,list2))
print(res)
result = zip(*res)
print(list(result))

2、enumerate
test_list = [1,'a','b','c',True,True,False,'d']
for index,val in list(enumerate(test_list)):
    if isinstance(val,type(True)) and val == True:
        print(index)

"""
index,val= (0, 1)
test_list = [1,'a','b','c',True,True,False,'d']
for index,val in list(enumerate(test_list)):
    if isinstance(val,type(True)) and val == True:
        print(index)

# res = test_list.index(True)
# print(res)


# [(0,1),(1,"a"),(2,"b")]
result = enumerate(test_list,3)
print(list(result))

# test_list = [("key1","val1"),("key2","val2")]
# print(dict(test_list))
# list1 = ["key1","val1"]
# list2 = ["key2","val2"]
# res = list(zip(list1,list2))
# print(res)
# result = zip(*res)
# print(list(result))








