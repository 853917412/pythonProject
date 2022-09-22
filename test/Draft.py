# x = (2, 1, 0)
# print("".join('%s' %id for id in x))
import unittest
import warnings
import time

import numpy as np
from ddt import ddt, data, unpack, file_data
from pywin.dialogs import login
from selenium import webdriver



"""
题目4:
编写一个工具箱类和工具类
工具类：需要有工具具的名称、功能描述、价格。
工具箱类：能够添加工具、删除工具、查看工具，并且能获取工具箱中工具的总数。
实例化几个工具。并在工具箱对象当中做添加/删除/查看工具操作，获取工具箱对象中有几个工具。
工具比如锤子、斧头、螺丝刀等工具。
提示：不需要用到继承。
"""
class toolsx():
    def __init__(self,name,function,price):
        self.name = name
        self.function = function
        self.price = price
    def show(self):
        print("{},{},{}".format(self.name,self.function,self.price))

class tools_box():
    tools = []
    def add_tools(self,tools_obj: toolsx):
        if tools_obj not in self.tools:
            self.tools.append(tools_obj)
        else:
            print("已存在工具")
    def remove_tools(self,tools_obj: toolsx):
        if tools_obj in self.tools:
            self.tools.remove(tools_obj)
        else:
            print("不存在该工具")

    def show_tools(self):
        for i in range(0, len(self.tools)):
            self.tools[i].show()
def p_1640(arr,pieces):
    d = {p[0]: p for p in pieces}
    i, n = 0, len(arr)
    while i < n:
        if arr[i] not in d:
            return False
        p = d[arr[i]]
        if arr[i: i + len(p)] != p:
            return False
        i += len(p)
    return True
exploe([91,4,64,78],[[78],[4,64],[91]])
