"""
============================
Project: py49
Author:柠檬班-海励
Time:2022/3/14 20:44
E-mail:2227092769@qq.com
Company:湖南零檬信息技术有限公司
Site: http://www.lemonban.com
Forum: http://testingpai.com 
============================
"""
"""
五、字符串(增、查、操作)
1、特性
   1、不可修改(只存在重新赋值)
   2、有序
   3、可迭代

2、字符串的访问
通过索引访问
test_str[index]
p   y   t   h  o    n
0,  1,  2,  3， 4   5   # 正序索引，从左边往右边取值
-6 -5  -4  -3  -2  -1   # 倒序索引，从右边往左边取值

test_str[-2(左):-5(右):-1]
res= "oht"

获取指定字符的索引值
test_str.index("h")
参数：
sub：需要获取索引的字符
start=None：开始查找的索引位置，如果不传默认为0
end=None：结束查找的索引位置，如果不传默认为字符串的长度
获取字符串的长度
len(test_str)

3、字符串切片
正序切片
test_str[起始索引(左):结束索引(右):步长]
倒序切片
test_str[-起始索引(左):-结束索引(右):-步长]
字符串反转
res = test_str[::-1]
注意点
1、取值是左闭右开(包含左边索引的值，不包含右边索引的值)
2、步长不写默认为1
3、起始索引：不传默认从0开始
4、结束索引：不传默认为字符串的长度
5、空格也属于字符串的组成部分，占一个索引位置
6、步长前面加-，表示倒序切片，倒序切片建议用倒序索引
7、正序切片用正序索引，倒序切片用倒序索引

4、字符串运算
+：字符串的拼接
test_str1 = "hello"
test_str2 = "python"
print(test_str1+test_str2)
*：重复输出
print("="*20)
成员运算
in: 判断是字符串的成员，返回True
not in : 判断不是字符串的成员，返回False


5、字符串转义
使用场景：路径处理，字符串中的转义处理
\n,\t,
\: 取消转义
r：取消转义
"""

# hello\npython
print(r"hello\npython")
print("\\n")
test_path = r"D:\GitDir\files\VIPPPT课件\vip课件.pptx"
print(test_path)




"""
test_str1 = "hello"
print("h" not in test_str1)


字符串运算
test_str1 = "hello"
test_str2 = "python"
print(test_str1+test_str2)
print("="*20)
print(test_str1 * 10)







test_str = "python"
res = test_str[-2:-5:-1]
# test_str[-2(左):-5(右):-1]
# res= "oht"
print(res)

# 正序切片
# res = test_str[0:len(test_str):2]
# print(res)


index 正序索引从0开始
倒序索引：-1开始
print(test_str[5])
print(test_str[-1])
print(test_str.index("h",4))
print(len(test_str))


#变量 指向 的是一个内存地址
test_str = "hello"
print(id(test_str),test_str)

#重新赋值
test_str = "python"
print(id(test_str),test_str)

#了解
for val in test_str:
    print(val)

"""

