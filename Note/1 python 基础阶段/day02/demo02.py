"""
============================
Project: py49
Author:柠檬班-海励
Time:2022/3/11 21:30
E-mail:2227092769@qq.com
Company:湖南零檬信息技术有限公司
Site: http://www.lemonban.com
Forum: http://testingpai.com 
============================
"""
"""
一、python数据类型
1、数值(int、float、bool)
2、字符串(str)
3、布尔类型(bool)
4、元组(tuple)
5、列表(list)
6、集合(set)
7、字典(dict){"key1":"val1"}
8、None

二、数据类型的识别
1、查询数据类型
type(obj)
type(test_str)

2、判断数据类型：
isinstance(obj, type)
isinstance(test_str, list)

三、python包管理
pip是用来管理python包的工具
1、查询安装了哪些包
pip list
2、安装
前提：使用的国内源要收录了对应的包才能下载安装
pip install -i https://pypi.tuna.tsinghua.edu.cn/simple 包名称
pip install -i https://pypi.tuna.tsinghua.edu.cn/simple 包名称==版本号
3、卸载
pip uninstall 包名称
4、更新
pip install -U 包名称
5、虚拟环境相关(docker)
pip  freeze > test.txt   导出依赖包名称和版本号
pip install -r test.txt  根据文件安装包
6、升级pip
python -m pip install --upgrade pip
为什么用pip安装
1、安装包的时候会有依赖，通过pip会自动给你安装依赖
2、2个包相互以依赖，通过pip 安装会自动解决相互依赖的问题
pip install requests 
urllib3
"""

test_str="hello"
print(type(test_str))
print(isinstance(test_str, list))


