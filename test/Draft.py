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
    def add_tools(self,toolsx_obj: toolsx):
        if toolsx_obj not in self.tools:
            self.tools.append(toolsx_obj)
        else:
            print("已存在工具")
    def remove_tools(self,toolsx_obj: toolsx):
        if toolsx_obj in self.tools:
            self.tools.remove(toolsx_obj)
        else:
            print("不存在该工具")
    def __x1(self):
        print("这是私有方法")
    def show_tools(self):
        if self.tools == []:
            print("箱子内没有工具")
        for i in range(0, len(self.tools)):
            self.tools[i].show()

def p_1678(command):
    dic = {'G':'G','()': 'o','(al)': 'al'}

p_1678("G()(al)")




