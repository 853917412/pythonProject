"""
============================
Project: py49
Author:柠檬班-海励
Time:2022/4/20 20:22
E-mail:2227092769@qq.com
Company:湖南零檬信息技术有限公司
Site: http://www.lemonban.com
Forum: http://testingpai.com 
============================
"""
"""
Faker造数据
安装库
pip install Faker==8.11.0


四要素
1、姓名
	name = fk.name()
2、身份证
	id_card = fk.ssn()
3、手机号
	phone = fk.phone_number()
4、银行卡(信用卡)
	card = fk.credit_card_number()


1、地址(带邮编)
	addr = fk.address()
2、邮箱
	email = fk.email()
	company_email = fk.company_email()
3、公司名称
	company_name = fk.company()
4、工作岗位
	job = fk.job()
5、邮编
	post_code = fk.postcode()
6、国家名称
	country = fk.country()
7、省
	city = fk.province()
8、城市
	city = fk.city()
	
1、生成复杂人物信息
	fk.profile(fields=None, sex=None)
2、生成简单人物信息
	fk.simple_profile(sex=None)


随机数
	num = fk.random_int(min=1000,max=9999)
	
	
1、随机字符串
	test_str = fk.pystr()
2、随机生成一句话
	sentence = fk.sentence()
3、随机生成一篇文章
	text = fk.text()
	
	
不指定时间范围
	1、随机年: 1970 -- 现在
		year = fk.year()
	2、当前年
		date = fk.date_this_year()
	3、随机月
		month = fk.month()
	4、当前月
		date = fk.date_this_month()
	5、随机年-月-日
		date = fk.date()
	6、年-月-日 时:分:秒
		date_time = fk.date_time()

指定时间范围
	年-月-日
		date = fk.date_between(start_date='-1y',end_date='today')
		参数
			start_date='-1y'
				-1y：一年前
				-1m：一个月前
			end_date='today'
				today：今天
				-1y：一年前
				-1m：一个月前
	年-月-日 时:分:秒
		date_time = fk.date_time_between(start_date='-3y',end_date='now')
		参数
			start_date='-1y'
				-1y：一年前
				-1m：一个月前
			end_date='now'
				now：今天
				-1y：一年前
				-1m：一个月前
				
未来时间
	年-月-日
		future_data = fk.future_date()
	年-月-日 时:分:秒
		future_date_time = fk.future_datetime()
		
数据唯一性
	fk.unique.方法名() 
	[fk.unique.name() for i in range(10)]
"""

from faker import Faker
fk = Faker(locale="zh-cn")
year = fk.year()
print(year)

date = fk.date_this_year()

print(date)

month = fk.month()
print(month)


date = fk.date()
print(date)

date_time = fk.date_time()
print(date_time)

date2 = fk.date_between(start_date='-1y',end_date='today')
print(date2)
date_time = fk.date_time_between(start_date='-1y',end_date='now')
print(date_time)


future_data = fk.future_date()
print(future_data)

future_date_time = fk.future_datetime()
print(future_date_time)

result= [fk.unique.name() for i in range(50)]
print(result)

#改服务器时间：对账的时候用  日切24点

# name = fk.name()
# print(name)
# id_card = fk.ssn()
# print(id_card)
# # 测试环境记得关闭短信验证码的功能
# phone = fk.phone_number()
# print(phone)
# card = fk.credit_card_number()
# print(card)
# addr = fk.address()
# print(addr)
# email = fk.email()
# print(email)
# city1 = fk.province()
# city2 = fk.city()
# print(city1)
# print(city2)
# country = fk.country()
# print(country)
# man = fk.profile()
# print(man)
# men = fk.simple_profile(sex=None)
# print(men)
# num = fk.random_int(min=1000,max=9999)
# print(num)
# text = fk.text()
# print(text)
# print("+++")
# sentence = fk.sentence()
# print(sentence)

