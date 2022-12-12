"""
============================
Project: py49Api
Author:柠檬班-海励
Time:2022/5/9 20:15
E-mail:2227092769@qq.com
Company:湖南零檬信息技术有限公司
Site: http://www.lemonban.com
Forum: http://testingpai.com 
============================
"""
"""
图片验证码
{
  "userName": "haili",
  "password": "QINHAILI",
  "captcha": "5588",
  "imgId": "5558e47da32141089ff0e4b324158282",
  "developerFlag": false,
  "needCheck": true
}

"""
import json
import requests
import base64
class ImageCode:
    def __init__(self):
        #获取图片验证码的接口地址
        self.image_url = "http://mall.lemonban.com:8108/captcha.jpg"
        #图鉴图片识别的接口地址
        self.image_code_url = "http://api.ttshitu.com/predict"

    #获取图片的二进制文件，转成b64数据
    def __get_image(self,uuid):
        data = {"uuid":uuid}
        res = requests.get(url=self.image_url,params=data)
        image_tyte = res.content
        print("图片二进制：",type(image_tyte),image_tyte)
        base64_data = base64.b64encode(image_tyte)
        print("base64编码之后：",type(base64_data),base64_data)
        b64 = base64_data.decode()
        print("base64解码之后：",type(b64),b64)
        return b64

    #请求图鉴接口，解析图片验证码
    def get_image_code(self,uuid):
        b64 = self.__get_image(uuid=uuid)
        data = {
            "username":"haili",
            "password":"QINHAILI",
            "typeid":"3",
            "image":b64
        }
        result = json.loads(requests.post(url=self.image_code_url, json=data).text)
        print(result)
        if result['success']:
            return result["data"]["result"]
        else:
            return result["message"]


