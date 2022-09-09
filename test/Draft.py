# x = (2, 1, 0)
# print("".join('%s' %id for id in x))

from typing import List
import traceback
class DOG:
    name1 = 'XX'
    def __init__(self):
        self.name = 123
    def eat(self,x):
        print("吃{}".format(x))
x = DOG()
print(x.name,x.name1)
x.eat("shit")


