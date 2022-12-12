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
py49期专属秒杀商品
create_order 创建订单接口请求参数：
{
  "addrId": 0,
  "prodCount": 1,
  "seckillSkuId": 348
}

1、获取秒杀订单地址
2、创建订单
3、提交订单
4、支付下单
5、模拟回调


下单支付流程
1、获取秒杀订单的接口地址
2、创建订单：客户端提交给后端
3、提交订单信息
4、支付下单
5、扫码支付：手机微信扫码向微信后端发起请求
6、微信后端回调我们后端的通知接口，告知订单支付状态
7、后端根据微信的回调信息更新订单状态
8、前端查询接口，查询到订单的状态，跳转到对应的页面展示给客户看
9、订单号：
   我们后端：下单的时候有一个订单号
   微信手机端：扫码支付的时候，带上我们系统的订单号去请求微信的后端，也会生成一个订单号(微信的订单号)
   回调：带上微信的订单号+我们系统的订单号+支付状态+支付金额
   查询：我们系统去主动查询订单的状态(我们系统的订单号)
10、模拟回调：因为我们不会去真实支付，所以通过后端另外写一个接口来模拟微信的回调

11、了解
退款和支付都统称为交易，支付和退款属于不同的交易方式
扫码的过程就是获取商家的微信账号B
支付：客户 ----> 商家（微信支付要收手续费1,平台分钱1+100收1块钱，商家拿到98）
     微信账号A(虚拟账户) ---> 支付--> 微信账号B(虚拟账户)  ---> 提交支付信息给银联网联(结算，银行卡里面100 提现 到微信钱包(微信的企业银行账户))
退款：商家 ----> 客户  
     退款也会创建订单号
     退款手续费平台承担
     微信账号B(虚拟账户) -->  支付（退款）  微信账号A(虚拟账户)
清分(资本家分钱的过程)  --->  对账(支付金额对不对，清分的对不对)

手续费计算
兜底算法：微信0.3+美团(1-0.3-0.3)+把商家拉到美团来的人0.3+商家(99)
银行家算法：四舍六⼊五考虑，五后⾮零就进⼀，五后为零看奇偶，五前为偶应舍去，五前为奇要进⼀
四舍五入：


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
                  "seckillSkuId": 348
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