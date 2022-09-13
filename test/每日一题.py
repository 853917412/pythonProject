from typing import List

if __name__ == '__main__':

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
    def p_1880(**kwargs):

        def find(dic1):
            result = 0
            for i in dic1:
                result = result *10 +(ord(i)-97)
            return int(result)
        return find(kwargs['firstWord'])+find(kwargs['secondWord'])==find(kwargs['targetWord'])

    """
    给你一个数组prices，其中prices[i]是商店里第i件商品的价格。
    商店里正在进行促销活动，如果你要买第i件商品，那么你可以得到与 prices[j] 
    相等的折扣，其中j是满足j > i且prices[j] <= prices[i]的最小下标，如果没有满足条件的j，你将没有任何折扣。
    请你返回一个数组，数组中第i个元素是折扣后你购买商品 i最终需要支付的价格。
    """  #!!!!!!!!!!!!
    def finalPrices( prices: List[int]) -> List[int]:
        n = len(prices)
        result = []
        for i in range(n):
            j = i+1
            while j<n:
                if prices[j] <= prices[i]:
                    result.append(prices[i] - prices[j])
                    break
                j += 1
            if len(result) != i+1:
                result.append(prices[i])
        return result
    print(finalPrices([4,7,1,9,4,8,8,9,4]))
    """
    给你一个大小为 rows x cols 的矩阵 mat，其中 mat[i][j] 是 0 或 1，请返回 矩阵mat 中特殊位置的数目 。
    特殊位置 定义：如果 mat[i][j] == 1 并且第 i 行和第 j 列中的所有其他元素均为 0（行和列的下标均 从 0 开始 ），则位置 (i, j) 被称为特殊位置。
    """


    def p_1582(mat):
        e = 0
        for i in range(len(mat)):
            result = 0
            if mat[i].count(1) == 1:
                for j in range(len(mat[i])):
                    if mat[i][j] == 1:
                        y = j
                        break
                for i in range(len(mat)):
                    if mat[i][y] == 1:
                        result += 1
                    if mat[i][y] == 0:
                        pass
                if result == 1:
                    e += 1
        print(e)
        return e
    """
        给你一个字符串 text ，该字符串由若干被空格包围的单词组成。每个单词由一个或者多个小写英文字母组成，
    并且两个单词之间至少存在一个空格。题目测试用例保证 text 至少包含一个单词 。
        请你重新排列空格，使每对相邻单词之间的空格数目都 相等 ，并尽可能 最大化 该数目。如果不能重新平均分配所有空格，
    请将多余的空格放置在字符串末尾 ，这也意味着返回的字符串应当与原 text 字符串的长度相等。
        返回 重新排列空格后的字符串 。
    """
    def p_1592(arr):
        numb = arr.count(' ')
        if numb == 0:
            return arr
        larr = arr.split(' ')
        for i in range(len(larr)):
            if '' in larr:
                larr.remove('')
            if '' not in larr:
                break
        if len(larr) == 1:
            return ''.join(larr) + ' ' * numb

        x = numb // (len(larr) - 1)
        y = numb % (len(larr) - 1)
        e = ' ' * x
        larr = e.join(larr)
        return larr + (' ' * y)
    """
    给定一个非负整数，你至多可以交换一次数字中的任意两位。返回你能得到的最大值。
    """
    def p_670(self, num: int) -> int:
        x = None
        num = list(str(num))
        nums = sorted(num,reverse=True)
        if num == nums:
            return int(''.join(num))
        for i in range(len(nums)):
            if num[i] != nums[i]:
                x = i
                break
        a = num[x]
        for i in range(len(num)):
            if num[i] == nums[x]:
                sub = i
        b = sub
        num[x] = nums[x]
        num[b] = a
        print(int(''.join(num)))