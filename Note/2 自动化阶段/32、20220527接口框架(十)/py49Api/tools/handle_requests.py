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
import re
import requests
from requests_toolbelt import MultipartEncoder

from conf.settings import image_info, host_info
from tools.handle_attribute import HandleAttribute
from tools.handle_path import image_dir
from tools.handle_response import HandleResponse


class HandleRequests:
    def __init__(self):
        self.header = {"locale": "zh_CN"}
        self.handle_response = HandleResponse()


    def __hanle_url(self,url:str,port):
        #拼接url地址(域名+端口+接口地址)
        if url.startswith("http") or url.startswith("https"):
            pass
        else:
            url = host_info["host"]+str(port)+url
        #获取需要替换的key
        key_list = re.findall("#(\w.+?)#",url)
        if len(key_list) >0:
            for key in key_list:
                if hasattr(HandleAttribute,key):
                    url = url.replace(f"#{key}#",str(getattr(HandleAttribute,key)))
                else:
                    print(f"{key}属性名称不存在，请检查一下全局属性设置是否错误")
            return url
        else:
            print("url地址不需要替换")
            return url


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
    def send_request(self,method,url,data,is_upload,port):
        #请求地址处理，接口地址的数据是从响应结果提取出来的
        new_url = self.__hanle_url(url=url,port=port)
        #鉴权处理
        self.__handle_headers()
        #图片上传接口
        if str(is_upload) == "1":
            #图片上传接口
            response = self.__upload_image(method=method,url=new_url)
        else:
            #普通接口
            response = requests.request(method=method,url=new_url,json=data,headers=self.header)
        #响应结果处理
        response = self.handle_response.handle_response(response=response)
        print("处理后的响应结果：")
        print(response)
        return response



