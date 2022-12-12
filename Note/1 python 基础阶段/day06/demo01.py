"""
============================
Project: py49
Author:柠檬班-海励
Time:2022/3/21 19:57
E-mail:2227092769@qq.com
Company:湖南零檬信息技术有限公司
Site: http://www.lemonban.com
Forum: http://testingpai.com 
============================
"""
"""
字典
一、字典特性
1、通过键值对来表示字典
2、key不能重复
3、字典是无序的
4、可变数据类型

二、字典创建
1、手动创建【掌握】
test_dict = {"key1":"val1","key2":"val2"}
2、键值对创建
test_tuple = dict(a=1,b=2,c=3)
3、print(dict.fromkeys(list1,list2))
list1的元素为key，list2整体为value
4、print(dict(zip(list1, list2)))【掌握】
list1中的元素为key，list2中的元素为value，一一对应(索引位置)组成字典
如果list长度不一致，以最短的list为准组成字典
5、嵌套元组
test_demo = [('name', '小明'), ('age', '20')]
res_demo = dict(test_demo)

三、字典查询
1、通过key获取value
key不存在会报错
test_dict["name"]
2、通过get方法获取
如果key不存在，不会报错，会返回设置的默认值，不写默认值返回None
res = test_dict.get("first_name","小红")
3、获取所有的key
keys = test_dict.keys()
返回类型为dict_keys类型，需要转换后才能使用
4、获取所有的values类型,需要转换后才能使用
values = test_dict.values()
返回类型为dict_values
5、同时获取key和value
result = test_dict.items()
返回类型为dict_items类型，需要转换后才能使用
6、迭代【结合for循环讲】

四、字典修改
1、通过key修改对应的value【掌握】
test_dict["name"]="小红"
2、添加键值对【掌握】
key存在则什么都不做
key不存在，会添加键值对
test_dict.setdefault("first_name","小红")
3、合并字典
key不同相当于将test_dict2的键值对追加写入到test_dict1中
key相同，会更新test_dict1的值
test_dict1 = {"first_name": "小明", "sex": "20"}
test_dict2 = {"first_name": "小红", "sex": "man"}
test_dict1.update(test_dict2)

五、字典删除
1、del : 无返回
del test_dict1["first_name"]
2、pop()：返回被删除key对应的value
res = test_dict1.pop("first_name")
3、popitem(): 返回被删除的键值对
res = test_dict1.popitem()
4、清空
test_dict1.clear()

六、字典排序
1、operator库排序
2、key=operator.itemgetter(0)
0：通过key排序
1：通过value排序
3、代码演示
import operator
test_dict1 = {"first_name": "10", "sex": "30","age":"20"}
# [("first_name", "10"),("sex","30"),("age","20")]
res = sorted(test_dict1.items(),key=operator.itemgetter(0))
print(res,type(res))
print(dict(res))
2、使用场景
加密的时候：排字典序，把字典排序后的值进行RSA加密处理(公钥)，得到一个字符串，
          带着字符串去调接口，调接口传数据给后端，后端拿到数据通过私钥解密

"""
#{键1：值，键2：值}
import operator
test_dict1 = {"first_name": "10", "sex": "30","age":"20"}
# [("first_name", "10"),("sex","30"),("age","20")]
res = sorted(test_dict1.items(),key=operator.itemgetter(0))
print(res,type(res))
print(dict(res))





# del test_dict1["first_name"]
# res = test_dict1.pop("first_name")
# print(res)
# print(test_dict1)

# test_dict1.popitem()
# print(test_dict1)
# res = test_dict1.popitem()
# print(res)

#根据进出栈的顺序，后进先出，每次都删除后进栈的那个键值对
# print(test_dict1)

#清空
# test_dict1.clear()
# print(test_dict1)



# test_dict1 = {"first_name": "小明", "sex": "20"}
# test_dict2 = {"first_name": "小红", "sex": "man"}
# test_dict1.update(test_dict2)
# print(test_dict1)


# test_dict["name"]="小红"
# result = test_dict["name"]
# print(result)

# test_dict.setdefault("name","小红")
# test_dict.setdefault("first_name","小红")
# result = test_dict["name"]
# print(test_dict)







# test_dict = {"name": "小明", "age": "20"}
# test = test_dict["name"]
# print(test)
# result = test_dict.items()  #  ==  [("name","小明"),("age","20")]
# dict_items    list([("name","小明"),("age","20")])
# print(result,type(result))
# res_list = list(result)
# print(res_list,type(res_list))

# test_demo = [('name', '小明'), ('age', '20')]
# res_demo = dict(test_demo)
# print(res_demo)

# keys = test_dict.keys()
# print(keys,type(keys))
# val_list = list(keys)
# print(keys)
# print(val_list)



# values = test_dict.values()
# print(type(values),values)
# print(type(list(values)),list(values))

# 进出栈的顺序 后进先出
# test_dict = {"key1": "val1", "key2": "val2"}
# print(test_dict)

# 键值对创建
# test_tuple = dict(a=1, b=2, c=3)
# print(test_tuple)

# 通过字典的fromkeys()
# list1 = ['a', 'b', 'c','d']
# list2 = [1,2,3]
# test_str = "hello"
# print(dict.fromkeys(list1,test_str))
# print(dict.fromkeys(list1,list2))
# print(dict(zip(list1,list2)))

# test_dict = {"name": "小明", "age": "20"}
# print(test_dict["first_name"])
# print(test_dict["age"])

# res = test_dict.get("first_name","小红")
# print(res)






