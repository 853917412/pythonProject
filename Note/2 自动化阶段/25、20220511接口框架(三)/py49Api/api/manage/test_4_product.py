"""
============================
Project: py49Api
Author:柠檬班-海励
Time:2022/5/9 21:36
E-mail:2227092769@qq.com
Company:湖南零檬信息技术有限公司
Site: http://www.lemonban.com
Forum: http://testingpai.com 
============================
"""
import time

"""

"""
import requests
import random
from test_1_login import Login

class Product:
    def __init__(self):
        self.login = Login()
        self.url = "http://mall.lemonban.com:8108/prod/prod"

    def add_product(self):
        headers = self.login.login()
        product_num = random.randint(100,10000)
        data = {
              "t": int(time.time()*1000),
              "prodName": f"商品名称py49{product_num}",
              "brief": "",
              "video": "",
              "prodNameEn": f"商品名称py49{product_num}",
              "prodNameCn": f"商品名称py49{product_num}",
              "contentEn": "",
              "contentCn": "<p><img src=\"https://img30.360buyimg.com/sku/jfs/t1/51598/2/16782/164845/613eb44dEbe9800e1/273975123599ebc0.jpg\" alt=\"详情1\" width=\"750\" height=\"1145\" /><img src=\"https://img30.360buyimg.com/sku/jfs/t1/209381/22/380/184497/613eb44dE1c31bab3/0d4c92c0154359dc.jpg\" alt=\"详情2\" width=\"750\" height=\"1138\" /></p>",
              "briefEn": "",
              "briefCn": "产品卖点py49",
              "pic": "2022/05/fa09e969866345e3bfbb42da5aa6a34e.jpg",
              "imgs": "2022/05/fa09e969866345e3bfbb42da5aa6a34e.jpg",
              "preSellStatus": 0,
              "preSellTime": None,
              "categoryId": 280,
              "skuList": [
                {
                  "price": 0.01,
                  "oriPrice": 0.01,
                  "stocks": 10000,
                  "skuScore": 1,
                  "properties": "",
                  "skuName": "",
                  "prodName": "",
                  "weight": 10,
                  "volume": 10,
                  "status": 1,
                  "partyCode": f"{int(time.time()*1000)}", #不能重复
                  "prodNameCn": f"商品名称py49{product_num}",
                  "prodNameEn": f"商品名称py49{product_num}",
                }
              ],
              "tagList": [
                1
              ],
              "content": "",
              "deliveryTemplateId": 1,
              "totalStocks": 10000,
              "price": 0.01,
              "oriPrice": 0.01,
              "deliveryModeVo": {
                "hasShopDelivery": True,
                "hasUserPickUp": False,
                "hasCityDelivery": False
              }
            }
        res = requests.post(url=self.url,json=data,headers=headers)
        print(res.text)

if __name__ == '__main__':
    cl = Product()
    cl.add_product()