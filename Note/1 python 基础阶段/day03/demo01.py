"""
============================
Project: py49
Author:柠檬班-海励
Time:2022/3/14 20:16
E-mail:2227092769@qq.com
Company:湖南零檬信息技术有限公司
Site: http://www.lemonban.com
Forum: http://testingpai.com 
============================
"""
"""
数值类型(运算符)
一、算术运算
1、加、减、乘(*: 数字8上面的符号shift+8)
2、除
得到浮点数(float)
print(10/3)
取整(去掉小数部分)
print(10//3)
3、幂运算
print(2**3)
4、取余/取模(%)
print(10%3)

二、赋值运算
num = 10
num += 1  # num = num + 1
num /= 2
num **= 2
num *= 2

三、比较运算
> 、 < 、 >=   <=、==(等于) 、 !=(不等于)
条件成立返回True
条件不成立返回False

四、逻辑运算
1、与(and): 多个条件，同时为真返回True，否则返回False
2、或(or): 多个条件，只要任意一个为真返回True，否则返回False
3、非(not)：为真则返回False，为假则返回True





"""

num1 = 10
num2 = 20

# 真  真  返回真
# 真  假  返回假
# 多个条件都为真，返回True
# print(num1 > 1 and num2 >100)

#多个条件只要一个为真，就返回True
# print(num1 > 1 or num2 >100)


# not 为真就返回假，假就返回真
# print( not num1 == num2)
print( not (num1 >=10 and  num2 >10))



#比较运算
num1 = 10
print(num1 != 10)


# 赋值运算
num = 10
num /= 2  # num = num + 1
print(num)


#取余
print(9%2)

#幂运算
print(2**3)


#得到浮点数
print(10/3)

#取整(去掉小数部分)
print(10//3)

num1 = 10
num2 = 20
print(num1+num2)
print(num1-num2)
print(num1*num2)






