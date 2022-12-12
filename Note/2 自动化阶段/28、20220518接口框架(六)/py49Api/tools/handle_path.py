"""
============================
Project: py49Api
Author:柠檬班-海励
Time:2022/5/13 21:35
E-mail:2227092769@qq.com
Company:湖南零檬信息技术有限公司
Site: http://www.lemonban.com
Forum: http://testingpai.com 
============================
"""
import os

#项目根路径
base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

#测试数据目录
data_dir = os.path.join(base_dir,"test_datas","data.xlsx")

#image路径
image_dir = os.path.join(base_dir,"images","haoche.jpg")
print(image_dir)