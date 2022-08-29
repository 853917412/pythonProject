# import copy
# dict1 = {'key1':'a','key2':'b','key3':['1','2','3']}
# new_dict1 = copy.deepcopy(dict1)
# print(dict1)
# print(new_dict1)
# dict1['key1'] = '666'
# dict1['key3'][0] = '888'
# print(id(dict1),id(new_dict1))
# print(id(dict['key3']),id(new_dict1['key3']))
# print(dict1)
# print(new_dict1)
from typing import List


# def xxx(nums,n):
#     x = []
#     if len(nums) % 2 == 0:
#         for i in range(0, n):
#             x.append(nums[i])
#             x.append(nums[i + n])
#         return x
#     else:
#         print("please input 2n length nums")
#         return 0
# xxx([1,2,5,3,1,5],3)
# x = 2.2
# y = 2
# print("x:{} y:{}".format(type(x), type(y)))
# print(x>y)
# from collections.abc import Iterable
# print(list(range(-1,-10,-2)))
# for i in range(1,10):
#     for j in range(1,i+1):
#         print('{} * {} = {}\t'.format(j,i,i*j),end='')
#     print("")
import copy
# def pop(lis1):
#     for i in range(1,len(lis1)+1):
#         for j in range(len(lis1)-i):
#             if lis1[j]>lis1[j+1]:
#                 lis1[j],lis1[j+1] = lis1[j+1],lis1[j]
#     return lis1
# print(pop([1,2,5,3,3,2]))
def p_4(nums):
    if nums <= 150:
        x = nums * 0.4463
        print('{:.1f}'.format(x))
    elif 150 < nums <= 400:
        x = 150 * 0.4463 + (nums - 150) * 0.4663
        print('{:.1f}'.format(x))
        return x
    else:
        x = 150 * 0.4463 + 250 * 0.4663 + (nums - 400) * 0.5663
        print('{:.1f}'.format(x))
        return x
round()

p_4(267)




