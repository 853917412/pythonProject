"""
============================
Project: py49
Author:柠檬班-海励
Time:2022/3/16 20:17
E-mail:2227092769@qq.com
Company:湖南零檬信息技术有限公司
Site: http://www.lemonban.com
Forum: http://testingpai.com 
============================
"""
"""
字符串的常用方法
一、单词大小写相关
1、字符串大写
res1 = test_str1.upper()
2、字符串小写
res2 = test_str2.lower()
3、单词首字母大写(以单词为单位，多个单词首字母都会大写)
res1 = test_str1.title()
4、大小写互换
res1 = test_str1.swapcase()

二、统计相关
1、获取字符串的长度
len(test_str)
2、统计字符串中某个字符出现的次数
res1 = test_str1.count("l",0,5 )
#sub：需要统计的字符, start=None：
# 统计范围的起始索引值, 不传默认为0
# end=None：统计范围的结束索引值，不传默认为字符串的长度
# 遵循左闭右开原则

三、判断相关
1、判断字符串是否都是大写字母，返回布尔值
res = test_str1.isupper()
2、判断字符串是否都是小写字母，返回布尔值
res2 = test_str1.islower()
3、判断字符串是不是都是空格，返回布尔值
res3 = test_str1.isspace()
4、判断是否是数字
res4 = test_str1.isdigit()
5、是否以某某开头
res5 = test_str1.startswith("http")
6、是否以某某结尾
res6 = test_str1.endswith("com")

四、字符串的拆分
res = test_str1.split()
sep:拆分字符，拆分字符会在拆分过程中会丢掉,不传值默认通过空格拆分
maxsplit：拆分次数，不填默认有多少个拆分字符就拆多少次

五、字符串连接
通过"-"将test_str字符的内容连接起来，支持各种可迭代对象
res = "-".join(test_str)

六、字符串替换
1、指定字符替换
old: 替换前的字符
new: 替换后的字符
count: 替换次数
res = test_str.replace('h','Q',1)

2、移除首尾指定的字符
默认移除首尾的空格或者换行符(\n)
res2 = test_str.strip("py")

七、字符串格式化【三选一掌握】
%：占位符
1、%s: 格式化输出字符串
只接受字符串类型
如果传入的是数值，会发生强制类型转换
phone_name = "HUAWEI"
phone_price = 1000.99
name = "this phone name is %s price is %s" % (phone_name, phone_price)
print(name)

2、%d：int类型数据
只接受数值类型，如果传小数会抹掉小数位留下整数部分，精度缺失
可以传负数
name = "this phone name is %s price is %d" % ("hauwei", -100)
3、%f
%.2f：保留2位小数，会发生四舍五入
接收小数，保留小数的精度，会发生四舍五入
phone_name = "HUAWEI"
phone_price = 1000.99
name = "this phone name is %s price is %.1f" % (phone_name, phone_price)
print(name)

format：{}作为占位符【掌握】
1、按位置取值，先到先得
phone_name = "HUAWEI"
phone_price = 1000.99
name = "this phone name is {} price is {}".format(phone_name,phone_price)
print(name)

2、按索引取值
通过索引取值从0开始，()是元组
参数可以复用，填重复的索引值即可
phone_name = "HUAWEI"
phone_price = 1000.99
name = "this phone name is {0} price is {1}".format(phone_name,phone_price)
print(name)

3、按关键字取值
参数可以复用，填重复的索引值即可
phone_name = "HUAWEI"
phone_price = 1000.99
name = "this phone name is {name} price is {price}".format(name=phone_name,price=phone_price)
print(name)


4、精度调整
price = "this phone price is {:.2f}".format(12.12521232)
print(price)



f表达式：{}作为占位符



"""
phone_name = "HUAWEI"
phone_price = 1000.99
name = f"this phone name is {phone_name} price is {phone_price}"
print(name)



"""
price = "this phone price is {:.2f}".format(12.1)
print(price)

phone_name = "HUAWEI"
phone_price = 1000.99
name = "this phone name is {name} price is {price}".format(name=phone_name,price=phone_price)
print(name)


phone_name = "HUAWEI"
phone_price = 1000.99
name = "this phone name is {} price is {}".format(phone_name,phone_price)
print(name)


phone_name = "HUAWEI"
phone_price = 1000.99
name = "this phone name is %s price is %.1f" % (phone_name, phone_price)
print(name)


phone_name = "HUAWEI"
phone_price = 1000.99
name = "this phone name is %s price is %s" % (phone_name, phone_price)
print(name)


test_str = " pythhonpy\n"
print(len(test_str))
res2 = test_str.strip()
print(len(res2),res2)
#去空格处理，项目中间用
# for i in [" ","h" ]:
#     res = test_str.replace(i,"")


test_str = "pythhon"
res = test_str.replace('h','Q',1)
print(res)


test_list = ["t1","t2"]
test_str = "python"
res = "_".join(test_str)
print(res,type(res))


test_str1 = "https://www.ketangpai.com"
res = test_str1.split("a",1000)
#sep:拆分字符，拆分字符会在拆分过程中会丢掉,不传值默认通过空格拆分
#maxsplit：拆分次数，不填默认有多少个拆分字符就拆多少次
print(res)


test_str1 = "https://www.ketangpai.com"
res = test_str1.isupper()
res2 = test_str1.islower()
res3 = test_str1.isspace()
# print(res3)
# print(len(test_str1))
res4 = test_str1.isdigit()
res5 = test_str1.startswith("http")
res6 = test_str1.endswith("com")
print(res5)
print(res6)



test_str1 = "hello"
res1 = test_str1.count("l",0,4)
#sub：需要统计的字符, start=None：
# 统计范围的起始索引值, 不传默认为0
# end=None：统计范围的结束索引值，不传默认为字符串的长度
# 遵循左闭右开原则
print(res1)


test_str1 = "PYTHON hello"
res1 = test_str1.title()
res1 = test_str1.swapcase()
print(res1)

test_str1 = "python"
test_str2 = "PYTHON"
res1 = test_str1.upper()
print(res1)
res2 = test_str2.lower()
print(res2)






"""
