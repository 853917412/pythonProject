"""
============================
Project: py49
Author:柠檬班-海励
Time:2022/3/18 20:00
E-mail:2227092769@qq.com
Company:湖南零檬信息技术有限公司
Site: http://www.lemonban.com
Forum: http://testingpai.com 
============================
"""
"""
列表
一、特性
1、有序
2、通过索引访问，索引从0开始
3、内容可重复
4、可变数据类型
5、元素数据类型可以不一致
6、列表可嵌套
7、可迭代

二、创建
test_list = ['c','b','a']
test_space = []

三、查询
1、通过索引取值
value = test_list[2]
2、通过值获取索引
index = test_list.index('a')
3、统计某个元素出现的次数
result = test_list.count("a")
4、列表长度
result = len(test_list)
5、类型查询
type(test_list)
6、切片[和字符串切片一样]
正序切片用正序索引，倒序切片用倒序索引
test = test_list[2:4]
test = test_list[-1:-4:-1]

四、修改
1、通过索引值修改元素
test_list = ['c','b','a','a',123,111,10.99,[1,2,3]]
test_list[0] = "ccc"
2、追加写入新的元素
test_list.append("vvvv")
3、指定位置插入
插入元素会占有插入的索引位,后面的元素索引位置+1
test_list.insert(1,"nnnnn")
4、合并列表(在原有列表基础上修改)
将test_list2中的元素全部追加写入到test_list
test_list.extend(test_list2)
5、合并并生成新的列表(不会修改原来的列表)
test_list3 = test_list + test_list2

五、删除
不要一边操作一边删除
1、通过索引删除
pop: 返回被删除的元素
test_list = ['c','b','a','a',123,111,10.99,[1,2,3]]
res = test_list.pop(0)
del：删除无返回
del test_list[0]
2、通过元素删除
如果元素重复，删除找到的第一个
test_list.remove("a")
3、清空列表
test_list.clear()

六、成员运算,返回布尔值
in: 是list的成员
not in: 不是list的成员


七、排序
1、在原来列表上排序
reverse=False: 升序，默认
reverse=True: 降序
test_list.sort(reverse=True)
2、不改变原列表，生成新的列表
reverse=False: 升序，默认
reverse=True: 降序
res = sorted(test_list)
3、排序原理
通过ASCII码来排序
res = ord("a") : 根据字符获取ASCII码
res2 =chr(25105): 根据ASCII码获取对应的字符
八、其他方法

"""
test_list = [12,3,66,33,9,10]

res1 = max(test_list)
res2 = min(test_list)
res3 = sum(test_list)

print(res1)
print(res2)
print(res3)

print(sum([i for i in range(101)]))







# 20013 中  25105  我   22269 国
# res = ord("a")
# print(res)

# res2 =chr(25105)
# print(res2)



# test_list = [12,3,66,33,9,10]
# print(test_list,id(test_list))
# test_list.sort(reverse=True)
# print(test_list,id(test_list))


# res = sorted(test_list,reverse=True)
# print(test_list,id(test_list))
# print(res,id(res))




# def test():
#     pass
#     return
# res = test()
# print(res)


# test_list = ['c','b','a','a',123,111,10.99,[1,2,3]]
# print(1 in test_list)


# test_list.remove("a")
# test_list.clear()
# print(test_list)


# res = test_list.pop(-1)
# print(test_list)
# del test_list[0]
# del test_list[0]
# del test_list[0]
# print(test_list)

# test_list2 = ["vv1","vv2","vv3"]
# test_list[0] = "ccc"
# print(test_list)
# test_list[-1][0] = "ccc"
# print(test_list)
# test_list.append("vvvv")
# test_list[-2].append("6688")
# print(test_list)
# test_list.insert(1,[1,2,3])
# print(test_list)
# test_list.extend("12345")
# test_list3 = test_list+test_list2
# print(test_list3)
# print(test_list)
# print(test_list2)



# for val in "12345":
#     test_list.append(val)


# print(test_list,type(test_list))
# print(test_list[2])
# print(test_list.index('a'))
# print(test_list.count("a"))
# print(len(test_list))

# test = test_list[2:4]
# test = test_list[-1:-4:-1]
# print(test)
# print(type(test_list[-1]))
# print(test_list[-1][-1])






