"""
============================
Project: py49
Author:柠檬班-海励
Time:2022/3/21 19:58
E-mail:2227092769@qq.com
Company:湖南零檬信息技术有限公司
Site: http://www.lemonban.com
Forum: http://testingpai.com 
============================
"""
"""
七、深浅拷贝【了解】

# 通过字典一次取值能拿到的数据，叫第一层数据，也叫父目录
# 通过多次取值才能取到的数据，叫子目录
# print(test_dict2["key3"][0])


#嵌套
test_dict2 = {"key1":"val1","key2":"val2","key3":['a','b','c']}
#浅拷贝
new_dict = test_dict2.copy()
print("浅拷贝后的id：")
print(id(test_dict2))
print(id(new_dict))
print("="*20)
print("修改前test_dict2：",test_dict2)
print("修改前new_dict：",new_dict)
test_dict2["key3"][0]="888"
print("修改后test_dict2：",test_dict2)
print("修改后new_dict：",new_dict)

#深拷贝
new_dict = copy.deepcopy(test_dict2)
print("修改前test_dict2:",test_dict2,id(test_dict2))
print("修改前new_dict  :",new_dict,id(new_dict))
test_dict2["key3"][0]=888
print("修改后test_dict2:",test_dict2,id(test_dict2))
print("修改后new_dict  :",new_dict,id(new_dict))


总结：
1、浅拷贝：拷贝父目录，子目录是引用
2、深拷贝：拷贝所有的目录
3、深浅拷贝值对嵌套才有意义
"""


import copy

#未嵌套
#test_dict1 = {"key1":"val1","key2":"val2","key3":"val3"}
#嵌套
test_dict2 = {"key1":"val1","key2":"val2","key3":['a','b','c']}
#深拷贝
# new_dict = copy.deepcopy(test_dict2)
# print("修改前test_dict2:",test_dict2,id(test_dict2))
# print("修改前new_dict  :",new_dict,id(new_dict))
# test_dict2["key3"][0]="888"
# print("修改后test_dict2:",test_dict2,id(test_dict2))
# print("修改后new_dict  :",new_dict,id(new_dict))


num = "aaaa"  # 00001
print(id(num))
num = "bbbb"
print(id(num))




