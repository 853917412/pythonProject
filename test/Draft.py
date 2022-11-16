# x = (2, 1, 0)
# print("".join('%s' %id for id in x))
# import unittest
# import warnings
# import time
# import time
# import numpy as np
# from ddt import ddt, data, unpack, file_data
# from pywin.dialogs import login
# from selenium import webdriver





# def p_764(n, mines) -> int:
#     g = [[1] * (n + 10) for _ in range(n + 10)]
#     for x, y in mines:
#         g[x + 1][y + 1] = 0
#     a, b, c, d = [[0] * (n + 10) for _ in range(n + 10)], [[0] * (n + 10) for _ in range(n + 10)], [
#         [0] * (n + 10) for _ in range(n + 10)], [[0] * (n + 10) for _ in range(n + 10)]
#     for i in range(1, n + 1):
#         for j in range(1, n + 1):
#             if g[i][j] == 1:
#                 a[i][j] = a[i - 1][j] + 1
#                 b[i][j] = b[i][j - 1] + 1
#             if g[n + 1 - i][n + 1 - j] == 1:
#                 c[n + 1 - i][n + 1 - j] = c[n + 2 - i][n + 1 - j] + 1
#                 d[n + 1 - i][n + 1 - j] = d[n + 1 - i][n + 2 - j] + 1
#     ans = 0
#     for i in range(1, n + 1):
#         for j in range(1, n + 1):
#             ans = max(ans, min(min(a[i][j], b[i][j]), min(c[i][j], d[i][j])))
#     print(ans)
#     return ans


def p_775(nums):
    n =len(nums)
    x = nums[0]
    for i in range(2,n):
        if x>nums[i]:
            return False
        x = max(x, nums[i-1])
    return True
print(p_775([3,2]))


