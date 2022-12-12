"""
============================
Project: py49
Author:柠檬班-海励
Time:2022/5/6 15:43
E-mail:2227092769@qq.com
Company:湖南零檬信息技术有限公司
Site: http://www.lemonban.com
Forum: http://testingpai.com 
============================
"""
# import requests
# from requests import utils
# session = requests.session()
# res1 = requests.utils.dict_from_cookiejar(session.cookies)
# print("创建session之后cookies是空的：",res1)
# data = {"email":"1605118090@qq.com",
#        "password":"Aa123456",
#         "remember":0}
# response = session.post(url="https://v4.ketangpai.com/UserApi/login",data=data)
# res2 = requests.utils.dict_from_cookiejar(response.cookies)
# print("请求第一个接口后自动添加cookies信息:",res2)
# res = session.get(url="https://v4.ketangpai.com/UserApi/getUserInfo")
# res3 = requests.utils.dict_from_cookiejar(response.cookies)
# print("后面的接口cookies信息一样：",res3)



# import requests
# url = 'https://v4.ketangpai.com/UserApi/login'
# data = {'email':'1605118090@qq.com',
#        'password':'Aa123456',
#        'remember':0}
# res1 = requests.post(url=url,data=data)
# cookie = res1.headers['Set-Cookie']
# print("res1请求头信息：",res1.request.headers)
# url2 = 'https://v4.ketangpai.com/UserApi/getUserInfo'
# res2 = requests.get(url=url2,headers = {'cookie':cookie})
# print("res2请求头信息：",res2.request.headers)



# import requests
# url = 'https://v4.ketangpai.com/UserApi/login'
# data = {'email':'1605118090@qq.com',
#        'password':'Aa123456',
#        'remember':0}
# res1 = requests.post(url=url,data=data)
# print("res1请求头信息：",res1.request.headers)
# url2 = 'https://v4.ketangpai.com/UserApi/getUserInfo'
# res2 = requests.get(url=url2,cookies = res1.cookies)
# print("res2请求头信息：",res2.request.headers)

