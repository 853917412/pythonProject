"""
============================
Project: py49Api
Author:柠檬班-海励
Time:2022/5/18 20:52
E-mail:2227092769@qq.com
Company:湖南零檬信息技术有限公司
Site: http://www.lemonban.com
Forum: http://testingpai.com 
============================
"""
import requests
from requests_toolbelt import MultipartEncoder

from conf.settings import image_info
from tools.handle_attribute import HandleAttribute
from tools.handle_path import image_dir
from tools.handle_response import HandleResponse


class HandleRequests:
    def __init__(self):
        self.header = {"locale": "zh_CN"}
        self.handle_response = HandleResponse()

    #请求头处理：鉴权
    def __handle_headers(self):
        if hasattr(HandleAttribute,"access_token"):
            token = getattr(HandleAttribute,"access_token")
            self.header["Authorization"]="bearer{}".format(token)
        else:
            print("该接口不需要鉴权")

    #图片上传接口单独处理
    def __upload_image(self,method,url):
        with open(file=image_dir,mode="rb") as file:
            image = file.read()
            data = MultipartEncoder(fields={
                "file": (image_info["file_name"], image, image_info["file_type"])
            })
            #修改请求头为图片上传的类型 multipart/form-data
            self.header["Content-Type"] = data.content_type
            response = requests.request(method=method,url=url,data=data,headers=self.header)
        #图片上上传接口修改了Content-Type的值，我们要用完之后改回来变成json，方便后面的接口继续使用
        self.header["Content-Type"] ="application/json;charset=UTF-8"
        return response

    #发送请求
    def send_request(self,method,url,data,is_upload):
        #鉴权处理
        self.__handle_headers()
        #图片上传接口
        if str(is_upload) == "1":
            #图片上传接口
            response = self.__upload_image(method=method,url=url)
        else:
            #普通接口
            response = requests.request(method=method,url=url,json=data,headers=self.header)
        #响应结果处理
        response = self.handle_response.handle_response(response=response)
        print("处理后的响应结果：")
        print(response)
        return response



