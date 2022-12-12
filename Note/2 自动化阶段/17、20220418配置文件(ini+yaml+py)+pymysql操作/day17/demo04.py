"""
============================
Project: py49
Author:柠檬班-海励
Time:2022/4/18 21:17
E-mail:2227092769@qq.com
Company:湖南零檬信息技术有限公司
Site: http://www.lemonban.com
Forum: http://testingpai.com 
============================
"""
"""
yaml文件
一、安装第三方库
pip install pyyaml
PyYAML==5.3.1

二、写yaml文件的语法
1、通过key: value来表示键值对(冒号后面必须有空格)
2、通过-: 来表示列表(冒号后面必须有空格)
3、整个yaml对外只能有一个数据类型
4、支持嵌套，只支持dict嵌套列表字典
"""

import yaml


with open(file="test.yaml",encoding="utf-8") as file:
    values = yaml.load(stream=file,Loader=yaml.FullLoader)
    print(values,type(values))










