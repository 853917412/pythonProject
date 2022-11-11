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

def p_1704(s):
    cnt, n = 0, len(s) >> 1
    vowels = set('aeiouAEIOU')
    for i in range(n):
        cnt += s[i] in vowels
        cnt -= s[i + n] in vowels
    return cnt == 0
p_1704("textbook")



