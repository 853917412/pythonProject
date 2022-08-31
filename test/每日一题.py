from typing import List


def p_1464(nums):  # 显示最大值下标
    nums1 = sorted(nums, reverse=True)
    if nums1[0] == nums1[1]:
        for i in range(len(nums)):
            if nums[i] == nums1[0]:
                print(str(i), end='')
    else:
        print(str(nums.index(nums1[0])) + str(nums.index((nums1[1]))))


def p_006(List, target):
    for i in List:
        for j in List:
            if i != j:
                if i + j == target:
                    print('[{},{}]'.format(List.index(i), List.index(j)))
                    return 0
                else:
                    pass
            else:
                pass


"""
1317  给你一个整数n，请你返回一个 由两个整数组成的列表 [A, B]，满足：
A 和 B都是无零整数
A + B = n
"""
def p_1317(n):
    x = len(str(n))
    x = int('1' * x)
    for i in range(1, x):
        a = n - i
        if ('0' not in str(a) and '0' not in str(i)):
            print([i, a])
            return 0
        else:
            pass

"""
最多删除一个字符，检查能否形成回文字符串
"""
def p_019(str):
    str_r = str[::-1]
    error = []
    for i in range(len(str)):
        if str_r[i] == str[i]:
            pass
        else:
            error.append(i)
    if len(error) == 2 or len(error) == 0:
        print(True)
    else:
        print(False)
    print(error)

"""
给你一个数组 nums ，数组中有 2n 个元素，按 [x1,x2,...,xn,y1,y2,...,yn] 的格式排列。
请你将数组按 [x1,y1,x2,y2,...,xn,yn] 格式重新排列，返回重排后的数组。
"""
def p_1470(nums):
    x = []
    if len(nums)%2 == 0:
        n = int(len(nums)/2)
        for i in range(0,n):
            x.append(nums[i])
            x.append(nums[i+n])
        print(x)
    else:
        print("please input 2n length nums")
        return 0
class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        nums[::2], nums[1::2] = nums[:n], nums[n:]
        return nums

"""
字母的 字母值 取决于字母在字母表中的位置，从 0 开始 计数。即，'a' -> 0、'b' -> 1、'c' -> 2，以此类推。
对某个由小写字母组成的字符串s 而言，其 数值 就等于将 s 中每个字母的 字母值 按顺序 连接 并 转换 成对应整数。

例如，s = "acb" ，依次连接每个字母的字母值可以得到 "021" ，转换为整数得到 21 。
给你三个字符串 firstWord、secondWord 和 targetWord ，每个字符串都由从 'a' 到 'j' （含'a' 和 'j' ）的小写英文字母组成。
如果firstWord 和 secondWord 的 数值之和 等于 targetWord 的数值，返回 true ；否则，返回 false 。
"""
def p_1880(FirstWord,SecondWord):
    a = []
    b = []
    word = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
    number = [0, 1, 2, 3, 4, 5, 6, 7,8,9]
    dic = dict(zip(word, number))
    print (dic)
    for i in FirstWord:
        a.append(dic[i])
    for j in SecondWord:
        b.append(dic[j])
    print(a, b)
    a = "".join('%s' %id for id in a)
    b = "".join('%s' %id for id in b)
    return int(a)+int(b)
print(p_1880(FirstWord= 'acb', SecondWord='cba'))

