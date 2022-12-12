"""
============================
Project: py49
Author:柠檬班-海励
Time:2022/3/28 19:25
E-mail:2227092769@qq.com
Company:湖南零檬信息技术有限公司
Site: http://www.lemonban.com
Forum: http://testingpai.com 
============================
"""
"""
题目1：冒泡排序

题目2、输出99乘法表(双重for循环)
格式如下：（每项数据之间空一个Tab键，可以使用"\t"）
1 * 1 = 1   
1 * 2 = 2    2 * 2 = 4  
1 * 3 = 3    2 * 3 = 6     3 * 3 = 9    
1 * 4 = 4    2 * 4 = 8     3 * 4 = 12   4 * 4 = 16  
1 * 5 = 5    2 * 5 = 10    3 * 5 = 15    4 * 5 = 20    5 * 5 = 25   
1 * 6 = 6    2 * 6 = 12    3 * 6 = 18    4 * 6 = 24    5 * 6 = 30    6 * 6 = 36 
1 * 7 = 7    2 * 7 = 14    3 * 7 = 21    4 * 7 = 28    5 * 7 = 35    6 * 7 = 42    7 * 7 = 49   
1 * 8 = 8    2 * 8 = 16    3 * 8 = 24    4 * 8 = 32    5 * 8 = 40    6 * 8 = 48    7 * 8 = 56    8 * 8 = 64 
1 * 9 = 9    2 * 9 = 18    3 * 9 = 27    4 * 9 = 36    5 * 9 = 45    6 * 9 = 54    7 * 9 = 63    8 * 9 = 72    9 * 9 = 81

题目3：用户输入月份,判断这个月是哪个季节(for循环实现)
=========================================================
参考答案
题目1：
未考虑时间复杂度
def demo01(test):
    n = len(test)
    for k in range(1,len(test)):
        print("外层循环次数:",k)
        for j in range(n-k):
            print("数据比较次数：",j)
            if test[j] > test[j+1] :
                test[j], test[j+1] = test[j+1], test[j]
    return test

考虑时间复杂度
def demo02(order_list):
    n = len(order_list)
    for k in range(1,len(order_list)):
        is_change = False
        for j in range(n-k):
            if order_list[j] > order_list[j+1] :
                order_list[j], order_list[j+1] = order_list[j+1], order_list[j]
                is_change = True
        if not is_change:
            return order_list
    return order_list

题目2：
for i in range(1, 10):
    for j in range(1, i+1):
        print('{}x{}={}\t'.format(j, i, i*j), end='')
    print()


题目3：
num = int(input('输入：'))
list1=[[12,1,2,'冬季'],[3,4,5,'春季'],[6,7,8,'夏季'],[9,10,11,'秋季']]
if num in range(1,13):
    for i in range(len(list1)):
        if num in list1[i]:
            print(list1[i][-1])
else:
    print('输入有误')


"""


# def demo01(test):
#     n = len(test)
#     for k in range(1,len(test)):
#         print("外层循环次数:",k)
#         for j in range(n-k):
#             print("数据比较次数：",j)
#             if test[j] > test[j+1] :
#                 test[j], test[j+1] = test[j+1], test[j]
#     return test
# # test_list = [90,50,2,47,21,12,45]
# test_list = [1,2,3,4,5]
# # [2,47,21,12,45,50,90]
# result = demo01(test_list)
# print(result)


test_list = [1,2,3,4,5]
# test_list = [90,50,2,47,21,12,45]
def demo02(order_list):
    n = len(order_list)
    for k in range(1,len(order_list)):
        is_change = False
        for j in range(n-k):
            if order_list[j] > order_list[j+1] :
                order_list[j], order_list[j+1] = order_list[j+1], order_list[j]
                is_change = True
        if not is_change:
            return order_list
    return order_list

result = demo02(test_list)
print(result)