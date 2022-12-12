"""
============================
Project: py49Api
Author:柠檬班-海励
Time:2022/5/6 21:36
E-mail:2227092769@qq.com
Company:湖南零檬信息技术有限公司
Site: http://www.lemonban.com
Forum: http://testingpai.com 
============================
"""
"""
框架执行入口
"""


import requests

res = requests.post(url="http://127.0.0.1:5000/test3")
print(res.json())










