"""
============================
Project: py49
Author:柠檬班-海励
Time:2022/3/23 20:43
E-mail:2227092769@qq.com
Company:湖南零檬信息技术有限公司
Site: http://www.lemonban.com
Forum: http://testingpai.com 
============================
"""
"""
集合
一、特性
1、元素不可重复
2、无序的
3、不支持索引操作
4、可迭代

二、创建
test_set = {1,2,3}

三、修改
1、追加
test_set.add(3333)
2、更新课迭代对象到集合（元组、列表）
test_set.update([1,2,3,4,5,6])

四、去重(对列表去重)
test_list = (1,1,2,2,3,3,4,4)
new_set = set(test_list)
print(type(new_set),new_set)
new_list = tuple(new_set)
print(type(new_list),new_list)

"""

test_list = (1,1,2,2,3,3,4,4)
new_set = set(test_list)
print(type(new_set),new_set)
new_list = tuple(new_set)
print(type(new_list),new_list)


# {33, 1, 2, 3, 'cc', 'b', 'aaa'}
# {33, 1, 2, 3, 'aaa', 'cc', 'b'}
# {33, 1, 2, 3, 'cc', 'aaa', 'b'}
# test_set = {'aaa',33,'b',1,'cc',2,3}
# print(test_set)



# test_set = {1,2,3}
# test_set.add(3333)
# print(test_set)

# test_set.update([1,2,3,4,5,6])
# print(test_set)

# for i in test_set:
#     print(i)
# test_set = set({})
# print(test_set,type(test_set))



