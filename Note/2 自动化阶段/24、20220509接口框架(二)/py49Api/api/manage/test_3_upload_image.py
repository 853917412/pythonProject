"""
============================
Project: py49Api
Author:柠檬班-海励
Time:2022/5/9 21:08
E-mail:2227092769@qq.com
Company:湖南零檬信息技术有限公司
Site: http://www.lemonban.com
Forum: http://testingpai.com 
============================
"""
"""
2、图片上传接口
Request Method: POST
http://mall.lemonban.com:8108/admin/file/upload/img
Content-Type: multipart/form-data; boundary=----WebKitFormBoundaryepH1XOlUCSwOCpYf
------WebKitFormBoundaryepH1XOlUCSwOCpYf
Content-Disposition: form-data; name="file"; filename="haoche.jpg"
Content-Type: image/jpeg
------WebKitFormBoundaryepH1XOlUCSwOCpYf--


安装第三方包
pip install requests-toolbelt
"""
import requests
from requests_toolbelt import MultipartEncoder

from test_1_login import Login

class UploadImage:
    def __init__(self):
        #实例化
        self.login = Login()
        self.url = "http://mall.lemonban.com:8108/admin/file/upload/img"

    def upload_image(self):
        #调用登陆接口，获取鉴权信息
        headers = self.login.login()
        with open(file=r"D:\haoche.jpg",mode="rb") as file:
            image = file.read()
            data = MultipartEncoder(fields={
                # file为接口抓包的name值
                # file的参数(“图片名称”,"图片二进制","图片的类型")
                "file":("haoche.jpg",image,"image/jpeg")
            })
            # {"Content-Type":'multipart/form-data; boundary={0}'}
            # {"Content-Type":"multipart/form-data; boundary={0}",'locale': 'zh_CN', 'Authorization': 'bearerf697fa8e-3ce7-45b2-b403-6a2025eed4d6'}
            headers["Content-Type"]=data.content_type
            print(headers)
            res = requests.post(url=self.url,data=data,headers=headers)
            print(res.text)
if __name__ == '__main__':
    cl = UploadImage()
    cl.upload_image()