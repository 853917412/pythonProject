"""
============================
Project: py49
Author:柠檬班-海励
Time:2022/4/8 21:40
E-mail:2227092769@qq.com
Company:湖南零檬信息技术有限公司
Site: http://www.lemonban.com
Forum: http://testingpai.com 
============================
"""
"""
五、路径处理
1、返回当前文件的绝对路径
	print(__file__)
2、返回当前运行文件所在【目录的绝对路径】
	os.path.dirname(__file__)
3、返回当前进程的工作目录(pycharm工作空间)
	os.getcwd()
4、获取指定文件的绝对路径
	os.path.abspath('demo01.py')
	
5、路径拼接
base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
for path in ["day01","day02","day03"]:
    res_path = os.path.join(base_dir,path,"demo01.py")
    print(res_path)
6、拓展
res_path = os.path.join("api",r"\test","demo01.py")
res_path = os.path.join("api/","test/","demo01.py")
print(res_path)
"""
import os

# print(__file__)

# dir_name = os.path.dirname(__file__)
# print(dir_name)

# 会根据你系统返回对应的路径表达式 windows:\  mac+linux: /
# abs_path = os.path.abspath(__file__)
# print(abs_path)


# work_dir = os.getcwd()
# print(work_dir)




#路径拼接
# res = os.path.join("D:","test","login.py")
# print(res)

# res = os.path.abspath(__file__)
# base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# for path in ["day01","day02","day03"]:
#     res_path = os.path.join(base_dir,path,"demo01.py")
#     print(res_path)
#

# 扩展
# res_path = os.path.join("api",r"\test","demo01.py")
res_path = os.path.join("api/","test/","demo01.py")
print(res_path)





