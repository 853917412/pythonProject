# 创建一个UnitTest类对象，用于操作所有的UnitTest的相关知识
# 导入UnitTest
import time
import unittest
import warnings

from ddt import ddt, data, unpack, file_data
from selenium import webdriver

# 创建UnitTest对象，必须继承于unittest.TestCase
# @ddt
class CaseDemo(unittest.TestCase):
    # 前置条件,每个用例执行前都会执行一次setUp，只需要定义一次即可
    def setUp(self) -> None:  # -> None表示该函数没有返回值
        # 不关闭浏览器
        option = webdriver.ChromeOptions()
        option.add_experimental_option('detach', True)
        # 创建webdriver对象
        self.driver = webdriver.Chrome(chrome_options=option)
        # 访问指定url
        self.driver.get('https://www.baidu.com')

    # 后置条件,每个用例执行后都会执行一次tearDown
    def tearDown(self) -> None:

        self.driver.quit()
        warnings.simplefilter('ignore', ResourceWarning)
    # @classmethod
    # def setUpClass(cls) -> None:
    #     cls.driver = webdriver.Chrome()
    #     cls.driver.get("https://www.baidu.com")

    # 测试用例的执行
    '''
    @data装饰器：将传入的值基于,进行分割
    @data('x','2')
        1.'x'
        2.'2'
    基于分割数据的数量决定测试用例的执行次数，将数据依次传入测试用例中进行执行
    @unpack用于数据的二次分割
    '''

    # @data(['kw', 'lol'], ['kw', '衡泰'], ['kw', '陕西'])
    # @unpack
    # @file_data('../data/user.yaml')
    # def test_1(self, **kwargs):
    #     input1 = kwargs['input']
    #     button = kwargs['button']
    #     # 执行搜索流程
    #     self.driver.find_element(input1['name'], input1['value']).send_keys(input1['text'])
    #     self.driver.find_element(button['name'], button['value']).click()
    #     time.sleep(4)

    # def loop(self):
    #     listx = ['x','衡x','陕xx']
    #     for text in listx:
    #         self.test_1(text)

    # def test_2(self):
    #     self.driver.find_element('id', 'kw').send_keys('lllllllllllllllllll')
    #     self.driver.find_element('id', 'su').click()
    #     time.sleep(4)

    #
    # def test_3(self):
    #     self.driver.find_element('id', 'kw').clear()
    #     self.driver.find_element('id', 'kw').send_keys('A1s我')
    #     self.driver.find_element('id', 'su').click()
    #     time.sleep(4)


# 运行UnitTest中的测试用例 通过MAIN函数运行
# if __name__ == '__main__':
#     unittest.main()
