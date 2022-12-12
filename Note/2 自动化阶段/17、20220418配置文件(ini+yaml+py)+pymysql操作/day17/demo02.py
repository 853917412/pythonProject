"""
============================
Project: py49
Author:柠檬班-海励
Time:2022/4/18 20:16
E-mail:2227092769@qq.com
Company:湖南零檬信息技术有限公司
Site: http://www.lemonban.com
Forum: http://testingpai.com 
============================
"""
"""
二、配置文件
分类
1、xxx.ini   了解
2、xxx.yaml  了解
3、settings.py
{
{“section1”:{"key1":"val1","key2":"val2"}},
{“section2”:{"key1":"val1","key2":"val2"}}
}
语法：
1、[section1]不能重复
2、同一个[section1]的key(options)不能重复
3、默认的数据类型为字符串


查询操作
1、查询所有的sections
sections_list = conf.sections()
result = conf.keys() 返回的是sections对象，需要另外转换之后才能使用

2、获取options
res = conf.options(section="mysql")

3、获取指定options的值
res2 = conf.getfloat(section="docker", option="port")
res2 = conf.getboolean(section="docker", option="is_true")
res2 = conf.getint(section="docker", option="port")
res2 = conf.get(section="docker", option="port")

4、获取指定session的options和value
res3 = conf.items(section="session")


写操作
写的逻辑：读取ini文件的数据，读在内存里面，通过各种方法去获取，从内存里面去拿的。
写的类型：
       1、写进内存里面去
          
       2、写到内存，再写入文件



"""

from configparser import ConfigParser
conf = ConfigParser()
conf.read(filenames="test.ini", encoding="utf-8")

# ===================================================================
#扩展知识，可以不看，做了解
conf.add_section(section="mytestadd")
sections_list = conf.sections()
print(sections_list)

# with open(file="test.ini",mode="w") as file:
#     conf.write(fp=file)

# ===================================================================
# res2 = conf.getfloat(section="docker", option="port")
# res2 = conf.getboolean(section="docker", option="is_true")
# res2 = conf.getint(section="docker", option="port")
# res2 = conf.get(section="docker", option="port")
# print(res2,type(res2))

# res = conf.options(section="mysql")
# print(res)

# res3 = conf.items(section="docker")
# print(list(res3))





# sections_list = conf.sections()
# print(sections_list)

# result = conf.keys()
# print(list(result))
# for i  in result:
#     print(i)






