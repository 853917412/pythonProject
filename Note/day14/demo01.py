"""
============================
Project: py49
Author:柠檬班-海励
Time:2022/4/11 19:48
E-mail:2227092769@qq.com
Company:湖南零檬信息技术有限公司
Site: http://www.lemonban.com
Forum: http://testingpai.com 
============================
"""
import time

"""
文件操作【了解，自动化用不着，面试可能会问到】
一、打开文件
1、open()
file：文件名称(路径)
mode='r'：操作模式
encoding：编码方式(避免中文乱码)

2、操作模式
r(read): 只读
   1、文件要存在
   2、默认只是模式
w(write): 只写(覆盖写入)
   1、文件可以不存在，如果不存在会自动创建文件
   2、文件目录要存在，如果没有就会报错
   3、只能写文件，不能读
   4、覆盖写入，先删除之前的数据，再写数据
a(append): 追加写入
   1、文件可以不存在，如果不存在会自动创建文件
   2、文件目录要存在，如果没有就会报错
   3、在文件末尾追加写入
   4、追加写入，不能读数据
+: 可以组合所有的模式
   r+：可读可写，覆盖写
   w+: 可读可写，覆盖写
   a+：可读可写，追加写

二、读取文件数据
必须手动关闭
file = open(file="test.txt",mode="r",encoding="utf-8")
1、读取所有文件
my_str = file.read()
2、读取第一行(通过换行符确认是否是第一行)
my_str = file.readline()
3、按行读取所有数据(包含换行符\n)，返回list，list中的每一个元素就是一行数据，
my_str = file.readlines()
4、with语法(会自动关闭文件流)
with open(file="test.txt",mode="r",encoding="utf-8") as file:
    my_str = file.readlines()
    print(my_str)

三、写文件
1、覆盖写入：mode="w"
with open(file="test.txt",mode="w",encoding="utf-8") as file:
    file.write("py49期")
2、追加写入,如果要换行需要手动添加换行符进去(\n)：mode="a"
with open(file="test.txt",mode="a",encoding="utf-8") as file:
    file.write("py49期")
    
四、保存
1、文件保存机制，先写入到缓存区域，在程序执行结束的时候一次性写入到文件并保存
2、file.flush()
with open(file="test.txt",mode="a",encoding="utf-8") as file:
    while True:
        time.sleep(2)
        file.write("\npy49期")
        file.flush()

五、光标操作
1、不要一边写一边读数据
2、file.seek(0)
offset: 偏移量，从多少个字节的位置开始
whence：0：文件开头的位置,
        1：光标所在的，当前位置,
        2：文件默认位置

六、二进制的操作
rb(了解): 二进制的方式读取文件（操作图片），其他的一样的
wb(了解): 二进制的方式写文件（操作图片），其他的一样的
ab(了解): 二进制的方式追加文件（操作图片），其他的一样的
with open(file="test.txt",mode="rb",encoding="utf-8") as file:
    my_str = file.read()
    print(my_str)
"""
# num = 1
# with open(file="test.txt",mode="a+",encoding="utf-8") as file:
#     time.sleep(2)
#     file.write(f"\npy49期{num}")
#     file.flush()
#     num += 1
#     print("num的值：",num)
#     file.seek(0)
#     test_str = file.read()
#     print(test_str)






# file = open(file="test.txt",mode="r",encoding="utf-8")
# my_str = file.read()
# my_str = file.readline()
# my_str = file.readlines()
# print(my_str)
# file.close()

#with语法
# with open(file="test.txt",mode="r",encoding="utf-8") as file:
#     my_str = file.readlines()
#     print(my_str)




# with open(file="haoche.jpg",mode="rb") as file:
#     my_str = file.read()
#     print(my_str)

# 开辟一个内存空间  10   1110
# a = 10   #  1110
# b = 10  #  1110

# print(id(a))
# print(id(b))
# print(a is b )


# def test(x,y):
#     return x+y
# test_str = f"你的薪资是{test(10,20)}k"
# print(test_str)

a = 10
b = 20
max = a if a>b else b
print(max)


def test(a,b):
    if a > b :
        return a
    else:
        return b





