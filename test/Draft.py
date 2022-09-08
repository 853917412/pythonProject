# x = (2, 1, 0)
# print("".join('%s' %id for id in x))

from typing import List
import traceback
try:
    raise ValueError("hahaha")
except Exception as e:
    print(e)
    print(traceback.print_exc())




