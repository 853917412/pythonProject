# x = (2, 1, 0)
# print("".join('%s' %id for id in x))

from typing import List
import traceback
import numpy as np

def p_1567(arr):
    nums = len(arr)
    res = 0
    fres = 0
    ze = 0
    for i in arr:
        if i > 0 :
            res +=1
        elif i < 0 :
            fres +=1
        elif i == 0:
            ze +=1
    if res%2 == 0:
        print(res + fres )
        return res + fres
    else:
        print(res + fres - 1)
        return res + fres - 1


p_1567([-1,-2,-3,0,1])






