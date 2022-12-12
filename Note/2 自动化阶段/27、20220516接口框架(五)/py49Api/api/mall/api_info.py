"""
============================
Project: py49Api
Author:柠檬班-海励
Time:2022/5/11 20:48
E-mail:2227092769@qq.com
Company:湖南零檬信息技术有限公司
Site: http://www.lemonban.com
Forum: http://testingpai.com 
============================
"""
"""
商城后台
	http://mall.lemonban.com/admin/#/login
	账号：student
	密码：123456a
商城前端
	http://mall.lemonban.com:3344/
数据库
	IP地址：47.113.180.81
	端口：3306
	账号：lemon
	密码：lemon123
	数据库：yami_shops

预期效果
1、拿到一个项目，在没有接口文档的情况下要能做自动化测试，搭建自动化框架;
2、能用到所学框架知识，进行二次封装，举一反三;

你们需要做什么
1、每次上课讲的内容要自己动手去做
2、接口文档尽量自己去抓包获取
3、上课先听懂，下课有不懂的继续问
4、听懂思路，做笔记


一、梳理核心业务流程
后端：添加产品
1、后端登陆接口
2、图片验证码
3、图片上传接口
4、详情图片处理
前端：购买产品
1、前端注册接口
2、注册短信验证码处理
3、前端登陆接口
4、购买商品: 下单、支付流程、回调、支付接口怎么测试

二、核心业务接口抓包
后端：
1、登陆接口
Request Method: POST
http://mall.lemonban.com:8108/adminLogin
Content-Type: application/json; charset=UTF-8
{
  "t": 1651840225337,
  "principal": "student",
  "credentials": "123456a",
  "sessionUUID": "f18cfd1e-b79e-49a9-8ab3-70bf04ea8965",
  "imageCode": "lemon"
}
2、图片上传接口
Request Method: POST
http://mall.lemonban.com:8108/admin/file/upload/img
Content-Type: multipart/form-data; boundary=----WebKitFormBoundaryepH1XOlUCSwOCpYf
------WebKitFormBoundaryepH1XOlUCSwOCpYf
Content-Disposition: form-data; name="file"; filename="haoche.jpg"
Content-Type: image/jpeg
------WebKitFormBoundaryepH1XOlUCSwOCpYf--
3、添加产品
Request Method: POST
http://mall.lemonban.com:8108/prod/prod
Content-Type: application/json; charset=UTF-8
{
  "t": 1651841071530,
  "prodName": "商品名称py49",
  "brief": "",
  "video": "",
  "prodNameEn": "商品名称py49",
  "prodNameCn": "商品名称py49",
  "contentEn": "",
  "contentCn": "<p><img src=\"https://img30.360buyimg.com/sku/jfs/t1/51598/2/16782/164845/613eb44dEbe9800e1/273975123599ebc0.jpg\" alt=\"详情1\" width=\"750\" height=\"1145\" /><img src=\"https://img30.360buyimg.com/sku/jfs/t1/209381/22/380/184497/613eb44dE1c31bab3/0d4c92c0154359dc.jpg\" alt=\"详情2\" width=\"750\" height=\"1138\" /></p>",
  "briefEn": "",
  "briefCn": "产品卖点py49",
  "pic": "2022/05/fa09e969866345e3bfbb42da5aa6a34e.jpg",
  "imgs": "2022/05/fa09e969866345e3bfbb42da5aa6a34e.jpg",
  "preSellStatus": 0,
  "preSellTime": null,
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
      "partyCode": "202205062039",
      "prodNameCn": "商品名称py49",
      "prodNameEn": "商品名称py49"
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
    "hasShopDelivery": true,
    "hasUserPickUp": false,
    "hasCityDelivery": false
  }
}


前端
注册接口
1、发送短信验证码
Request URL: http://mall.lemonban.com:8107/user/sendRegisterSms
Request Method: PUT
Content-Type: application/json; charset=UTF-8
{
  "mobile": "18820992555"
}
2、校验短信验证码
SELECT mobile_code FROM tz_sms_log WHERE user_phone="18820992555";
Request URL: http://mall.lemonban.com:8107/user/checkRegisterSms
Request Method: PUT
Content-Type: application/json; charset=UTF-8
{
  "mobile": "18820992555",
  "validCode": "244712"
}
3、注册
Request URL: http://mall.lemonban.com:8107/user/registerOrBindUser
Request Method: PUT
Content-Type: application/json; charset=UTF-8
{
  "appType": 3,
  "checkRegisterSmsFlag": "b04d54de5e384608bdf87f1ccdcd2743",
  "mobile": "18820992555",
  "userName": "18820992555",
  "password": "123456",
  "registerOrBind": 1,
  "validateType": 1
}

4、登陆
Request URL: http://mall.lemonban.com:8107/login
Request Method: POST
Content-Type: application/json; charset=UTF-8
{
  "principal": "18820992515",
  "credentials": "123456",
  "appType": 3,
  "loginType": 0
}

5、购买商品
a、获取秒杀商品的秒杀地址
Request URL: http://mall.lemonban.com:8107/p/seckill/orderPath
Request Method: GET
无请求参数
返回秒杀地址用于创建订单接口

b、创建订单
Request URL: http://mall.lemonban.com:8107/p/seckill/3wZaNWt1hXe/confirm
Request Method: POST
Content-Type: application/json; charset=UTF-8
{
  "addrId": 0,
  "prodCount": 1,
  "seckillSkuId": 254
}

c、提交订单
Request URL: http://mall.lemonban.com:8107/p/seckill/3wZaNWt1hXe/submit
Request Method: POST
Content-Type: application/json; charset=UTF-8
{
  "orderShopParam": {
    "remarks": "",
    "shopId": 1
  },
  "orderPath": "3wZaNWt1hXe"
}

d、下单
Request URL: http://mall.lemonban.com:8107/p/order/pay
Request Method: POST
Content-Type: application/json; charset=UTF-8
{
  "payType": 3,
  "orderNumbers": "1522567004576550912"
}

e、模拟回调
开发写一个模拟微信回调我们系统的接口


常用接口：
图片上传/文件上传
短信验证码
图片验证码
支付流程
滑块验证码：去领木森老师的公开课视频
普通接口
接口参数关联

三、设计自动化框架
1、分层设计
   对所有的功能进行分类管理，有助于维护框架
2、数据驱动


分层设计
1、测试用例数据放在excel ： test_datas
   1、设计excel表字段
   2、测试用例数据
2、测试用例：test_cases
   1、unittest写测试用例类(数据驱动、参数替换、参数关联、鉴权、接口断言、数据库断言)
3、封装的工具类：tools
   1、操作excel获取测试数据
   2、参数替换的逻辑
   3、请求发送的逻辑(鉴权)
   4、接口断言封装
   5、数据库断言的封装
   6、响应结果要二次封装
   7、日志收集器
   8、路径处理
   9、数据库操作
4、测试报告：reports
   1、收集框架执行过程中生成的测试报告文件
5、日志收集：logs
   1、收集框架执行过程中产生的日志信息
6、配置文件：conf
   1、python配置文件

四、接口测试用例设计
1、有效等价类
2、无效等价类
3、如何做好接口测试
   1、技术是为业务服务的
   2、了解业务熟悉业务逻辑/接口交互过程/数据落库
   3、抓包看接口的请求参数、请求方式、地址、鉴权方式
   4、写python代码，挨个请求一遍核心业务的接口
   5、数据库基础知识
   6、接口测试框架
   7、部署到服务器上
   8、jenkins持续集成(docker+jenkins+python+git)


"""





