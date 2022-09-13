# x = (2, 1, 0)
# print("".join('%s' %id for id in x))

from typing import List
import traceback
import numpy as np

def xxx(m,n):
    res = []
    nump = list((str(m)))
    nump = list(map(int, nump))
    print(min(nump))
    for i in range(n):
        nump.remove(min(nump))
    nump = list(map(str,nump))
    return (''.join(nump))


xxx(98368,2)



