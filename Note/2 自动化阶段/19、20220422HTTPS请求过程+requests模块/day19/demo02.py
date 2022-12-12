"""
============================
Project: py49
Author:柠檬班-海励
Time:2022/4/22 20:44
E-mail:2227092769@qq.com
Company:湖南零檬信息技术有限公司
Site: http://www.lemonban.com
Forum: http://testingpai.com 
============================
"""
import time

"""
requests模块
一、安装
pip install requests==2.24.0


二、HTTP请求类型
1、get 获取数据
2、post  提交数据
3、put   修改数据：全量修改   {"name":"test","age":"20"} == {"name":"test","age":"25"} 
4、patch  修改数据：部分修改  {"age":"25"}
5、delete 删除数据
6、options 查看允许的请求方式

三、get请求
1、参数传递：放在接口地址后面，通过?拼接(问号后面的是参数，多个参数通过&连接)
           http://httpbin.org/get?key1=val1&key2=val2
           通过params关键字接收请求参数，会自动将参数拼接在接口地址后面
data = {"__key1":"val1","key2":"val2",}
res = requests.get(url="http://httpbin.org/get",params=data)
res = requests.get(url="http://httpbin.org/get?key1=val1&key2=val2")

四、post请求
1、参数
data: 默认使用"Content-Type": "application/x-www-form-urlencoded"方式对请求参数进行编码
      请求参数放在form里面
      如果添加请求头字段设置Content-Type的类型，就会优先使用设置的编码方式进行传输
json: 默认使用"Content-Type": "application/json"方式对请求参数进行编码
      请求参数放在data里面
      如果添加请求头字段设置Content-Type的类型，就会优先使用设置的编码方式进行传输
  
五、get与post的区别
1、参数传递
   get: 用于从服务器获取数据，参数放在请求地址后面，通过?key=value的形式，多个参数通过&连接
   post: 用于向服务器提交数据，参数放在请求体中(body)，按照变量和值对应的方式传递

2、参数的长度限制
   get: get请求参数长度(大小)是后端限制的，协议本身并没有做限制
   post：post请求参数长度(大小)是后端限制的，但是通常情况下post请求参数大小通常会设置的比get要大一些

3、安全性
   get: 请求参数放在url地址后面，肉眼可见，不安全
   post: 请求参数放在请求体(body)里面，相对来说安全一些，需要抓包才能看到

4、幂等性
   幂等：一个接口用同样的参数去请求一次和请求无数次，接口返回的数据和处理的逻辑是一模一样的，这就叫幂等接口
   get请求的接口大部分是幂等接口
   post大部分接口是非幂等的，需要做幂等处理(重复下单、重复注册、重复提交、网络差的时候前端按钮要做防多点同时后端要做幂等处理)
"""

import requests
import pprint

#get
# data = {"__key1":"val1","key2":"val2",}
# res = requests.get(url="http://httpbin.org/get",params=data)
# # res = requests.get(url="http://httpbin.org/get?key1=val1&key2=val2")
# print(res.text)
# pprint.pprint(res.json())

#post请求
# head = {"Content-Type": "application/json"}
# data = {"key1":"val1","key2":"val2",}
# res = requests.post(url="http://httpbin.org/post",data=data,headers=head)
# print(res.text)


data = {
  "t": 1650634139709,
  "principal": "student",
  "credentials": "123456a",
  "sessionUUID": "5a0e414f-04a4-485c-83bf-6a5266a5f867",
  "imageCode": "lemon"
}
# res = requests.post(url="http://mall.lemonban.com:8108/adminLogin",json=data)
res = requests.request(method="post",url="http://mall.lemonban.com:8108/adminLogin",json=data)
print(res.json()["access_token"])
head={"Authorization":"bearer{}".format(res.json()["access_token"])}

print("*"*30)
res2 = requests.request(method="get",url="http://mall.lemonban.com:8108/sys/webConfig/getActivity",headers=head)
print(res2.json())









