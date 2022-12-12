"""
============================
Project: py49
Author:柠檬班-海励
Time:2022/4/20 21:21
E-mail:2227092769@qq.com
Company:湖南零檬信息技术有限公司
Site: http://www.lemonban.com
Forum: http://testingpai.com 
============================
"""
"""
http基础
http://testingpai.com/article/1621669379653

5、常用请求头
	1、Accept：`*/*`
		作用：用来告知（服务器）客户端可以处理的内容类型
		服务端选择一种客户端支持的方式，并通过响应头字段Content-Type告诉客户端
	2、Accept-Encoding
		作用：告知服务端客户端支持的编码格式，通常是某种压缩算法
		服务端选择一种客户端支持的方式，并通过响应头Content-Encoding告知客户端
	3、Accept-Language
		作用：告知服务端，客户端可以理解自然语言
		服务端选择一种客户端支持的方式，并通过响应头Content-Language告知客户端
	4、Access-Control-Request-Headers
		作用：告知服务端，真正请求过程中被使用的请求头有哪些
		content-type,token
	5、Access-Control-Request-Method
		作用：告知服务端在真正的请求采用的请求方法
		因为预检请求所使用的方法总是 OPTIONS，与实际请求所使用的方法不一样，所以这个请求头是必要的
	6、Cache-Control：no-cache
		作用：请求头里的Cache-Control是no-cache，是浏览器通知服务器：本地没有缓存数据
		服务端通过响应头Cache-Control:max-age=259200告知浏览器259200秒内不要请求服务端，客户端使用自己的缓存数据
	7、Connection：keep-alive
		作用：决定当前的事务完成后，是否会关闭网络连接
		keep-alive，持久连接，不会关闭
		close，关闭，表明客户端或服务器想要关闭该网络连接，这是HTTP/1.0请求的默认值
	8、Host：openapiv5.ketangpai.com
		作用：指明了请求将要发送到的服务器主机名和端口号
		如果没有包含端口号，会自动使用被请求服务的默认端口
	9、Origin：https://www.ketangpai.com
		指示了请求来自于哪个站点。该字段仅指示服务器名称，并不包含任何路径信息
	10、Pragma：no-cache
		作用：HTTP/1.1(Cache-Control 是否有缓存)，兼容HTTP/1.0（Pragma）的字段
		是一个在 HTTP/1.0 中规定的通用首部，它用来向后兼容只支持 HTTP/1.0 协议的缓存服务器，那时候 HTTP/1.1 协议中的 Cache-Control 还没有出来
	11、Referer：https://www.ketangpai.com/
		作用：告诉服务端当前请求页面的来源页面的地址，表示当前页面是通过此来源页面里的链接进入的
	12、User-Agent
		作用：让服务端来识别发起请求的用户代理软件的应用类型、操作系统、软件开发商以及版本号
	13、Content-Type【重点】
		application/x-www-form-urlencoded  form表单数据提交
		application/json       json数据提交
		multipart/form-data    图片，文件上传
		text/html              html数据提交

"""


"<methodcall><>{}<>></methodcall>".format("121212")

