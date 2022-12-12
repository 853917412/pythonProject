"""
============================
Project: py49Api
Author:柠檬班-海励
Time:2022/5/11 21:33
E-mail:2227092769@qq.com
Company:湖南零檬信息技术有限公司
Site: http://www.lemonban.com
Forum: http://testingpai.com 
============================
"""
"""
1、获取秒杀订单地址
2、创建订单
3、提交订单
4、支付下单
5、模拟回调

"""
import time
import requests
from test_2_login import Login
from jsonpath import jsonpath


class PlaceOrder:
    def __init__(self):
        self.header = Login().login()

    # 获取秒杀订单地址
    def order_path(self):
        url = "http://mall.lemonban.com:8107/p/seckill/orderPath"
        res = requests.get(url=url,headers=self.header)
        print(res.text)
        setattr(self,"order_path",res.text)

    # 创建订单
    def create_order(self):
        self.order_path()
        url = "http://mall.lemonban.com:8107/p/seckill/{}/confirm".format(getattr(self,"order_path"))
        data = {
                  "addrId": 0,
                  "prodCount": 1,
                  "seckillSkuId": 254
                }
        res = requests.post(url=url,json=data,headers=self.header)
        print(res.text)

    # 提交订单
    def commit_order(self):
        self.create_order()
        url = "http://mall.lemonban.com:8107/p/seckill/{}/submit".format(getattr(self,"order_path"))
        data = {
              "orderShopParam": {
                "remarks": "",
                "shopId": 1
              },
              "orderPath": "{}".format(getattr(self,"order_path"))
            }
        res = requests.post(url=url,json=data,headers=self.header)
        orderNumbers = jsonpath(res.json(),"$..orderNumbers")[0]
        setattr(self,"orderNumbers",orderNumbers)

    # 支付下单
    def pay(self):
        self.commit_order()
        url = "http://mall.lemonban.com:8107/p/order/pay"
        data = {
              "payType": 3,
              "orderNumbers": "{}".format(getattr(self,"orderNumbers"))
            }
        res = requests.post(url=url,json=data,headers=self.header)
        print(res.text)

    # 回调
    def call_back(self):
        self.pay()
        url = "http://mall.lemonban.com:8107/notice/pay/3"
        data = {
            "payNo":"{}".format(getattr(self,"orderNumbers")), #商城支付订单号
            "bizPayNo":str(int(time.time()*1000)), #微信方的订单号
            "isPaySuccess":True,#True 成功，False 失败
        }
        res = requests.post(url=url,json=data,headers=self.header)
        print('回调接口返回',res.text)

if __name__ == '__main__':
    cl = PlaceOrder()
    cl.call_back()