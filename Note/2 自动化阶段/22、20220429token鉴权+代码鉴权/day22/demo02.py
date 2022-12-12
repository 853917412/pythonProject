"""
============================
Project: py49
Author:柠檬班-海励
Time:2022/4/29 20:25
E-mail:2227092769@qq.com
Company:湖南零檬信息技术有限公司
Site: http://www.lemonban.com
Forum: http://testingpai.com 
============================
"""
"""
session鉴权
一、第一种方式
import requests
data = {"email":"1605118090@qq.com",
       "password":"Aa123456",
        "remember":0}
response = requests.post(url="https://v4.ketangpai.com/UserApi/login",data=data)
print(response.json())
cookie = response.headers["set-cookie"]
res = requests.get(url="https://v4.ketangpai.com/UserApi/getUserInfo",headers={"cookie":cookie})
print(res.json())


二、常用信息获取
请求头信息
head = response.request.headers

获取cookie信息
head = response.cookies

请求的url地址
url1 = response.request.url

获取请求参数
body = response.request.body

请求方式
method = response.request.method

获取响应头信息
response.headers

获取响应结果
text = response.text
jsonstr = response.json()

获取响应码
status_code = response.status_code

代码：
url1 = response.request.url
print(url1)

body = response.request.body
print(body)

method = response.request.method
print(method)

resp_head = response.headers
print(resp_head)

text = response.text
jsonstr = response.json()

status_code = response.status_code
print(status_code)
"""
# 第一种方式
# import requests
# data = {"email":"1605118090@qq.com",
#        "password":"Aa123456",
#         "remember":0}
# response = requests.post(url="https://v4.ketangpai.com/UserApi/login",data=data)
# print(response.json())
# cookie = response.headers["set-cookie"]
# res = requests.get(url="https://v4.ketangpai.com/UserApi/getUserInfo",headers={"cookie":cookie})
# print(res.json())



# 第二种方式
# import requests
# session = requests.session()
# print("会话：",session)
# data = {"email":"1605118090@qq.com",
#        "password":"Aa123456",
#         "remember":0}
# response = session.post(url="https://v4.ketangpai.com/UserApi/login",data=data)
# head = response.cookies
# print(head)
# print(response.json())
# res = session.get(url="https://v4.ketangpai.com/UserApi/getUserInfo")
# print(res.json())
# head2 = res.cookies
# print(head2)

# 第三种方式
import requests
data = {"email":"1605118090@qq.com",
       "password":"Aa123456",
        "remember":0}
response = requests.post(url="https://v4.ketangpai.com/UserApi/login",data=data)
print(response.json())
# requests.utils.dict_from_cookiejar()
print(response.cookies)
res = requests.get(url="https://v4.ketangpai.com/UserApi/getUserInfo",cookies=response.cookies)
print(res.json())
