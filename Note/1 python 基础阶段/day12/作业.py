"""
============================
Project: py49
Author:柠檬班-海励
Time:2022/4/6 20:12
E-mail:2227092769@qq.com
Company:湖南零檬信息技术有限公司
Site: http://www.lemonban.com
Forum: http://testingpai.com 
============================
"""
"""
题目1：封装一个学员类StudentStudy
属性：姓名，年龄、所在城市、期望薪资
方法一：打印学员正在学习的课程，课程作为参数传递。  XXX学员正在学习XXX课程
方法二：打印学员的期望薪资。XXX学员学完后的期望薪资为XXX
实例化2个学员，分别调用方法一和方法二  


题目2:
封装一个员工类Employee:
属性：员工姓名、工作年限、户籍城市、薪资、岗位名称
方法一：计算员工的一年薪资总额(不用含年终奖)
方法二：打印员工的姓名和工作年限： 员工XXX 工作年限为 XX
             (通过self访问员工名字和员工工作年限)
实例化2个员工，分别调用方法一(打印员工的年度薪资总额)和方法二  


题目3:
封装一个学生类Student， -
属性：姓名，年龄，性别，英语成绩，数学成绩，语文成绩，
方法一：计算总分，
方法二：计算三科平均分
方法三：打印学生的个人信息：我的名字叫XXX，年龄：xxx,性别：xxx。
请定义此类，并实例化2个学生,并打印每个学生的个人信息，计算总分、计算平均分！

题目4:
编写一个工具箱类和工具类
工具类：需要有工具具的名称、功能描述、价格。
工具箱类：能够添加工具、删除工具、查看工具，并且能获取工具箱中工具的总数。
实例化几个工具。并在工具箱对象当中做添加/删除/查看工具操作，获取工具箱对象中有几个工具。
工具比如锤子、斧头、螺丝刀等工具。
提示：不需要用到继承。
============================================================
作业参考答案：
题目1：
class StudentStudy:

    def init_attr(self,name,sex,city,want_salary):
        self.name = name
        self.sex = sex
        self.city = city
        self.want_salary = want_salary

    def print_studing_course(self,course_name):
        print("{}学员正在学习{}课程".format(self.name, course_name))

    def print_wanted_salary(self):
        print("{}学员学习完后的期望薪资为{}".format(self.name, self.want_salary))

xj = StudentStudy()
xj.init_attr("xjj", "女", "长沙", 14000)
xj.print_studing_course("python自动化")
xj.print_wanted_salary()

xh = StudentStudy()
xh.init_attr("xhh", "女", "深圳", 40000)
xh.print_studing_course("python测开")
xh.print_wanted_salary()


题目2：
class Employee:

    def init_attr(self,name,work_years,city,salary, job_name):
        self.name = name
        self.work_years = work_years
        self.city = city
        self.salary = salary
        self.job_name = job_name

    def print_a_year_salary(self):
        print("{}员工一年薪资总计为{}".format(self.name, self.salary * 12))

    def print_employee_info(self):
        print("员工{} 工作年限为 {}".format(self.name, self.work_years))

e1 = Employee()
e1.init_attr("xww", 3, "北京", 18000, "高级测试工程师")
e1.print_a_year_salary()
e1.print_employee_info()

e2 = Employee()
e2.init_attr("xff", 7, "上海", 50000, "测试经理")
e2.print_a_year_salary()
e2.print_employee_info()


题目3:
class Student:

    def init_attr(self,name,age, sex, en_score, math_score, cn_score):
        self.name = name
        self.age = age
        self.sex = sex
        self.en_score = en_score
        self.math_score = math_score
        self.cn_score = cn_score

    def get_all_scores(self):
        sum = self.en_score + self.math_score + self.cn_score
        return sum

    def get_avarage_scores(self):
        print("平均分为：{}".format(self.get_all_scores() / 3))

    def print_stu_info(self):
        print(f"我的名字叫{self.name}，年龄：{self.age}, 性别：{self.sex}。")

stu1 = Student()
stu1.init_attr("雨泽", 30, "男", 100, 130, 120)
print(stu1.get_all_scores())
stu1.get_avarage_scores()
stu1.print_stu_info()

stu2 = Student()
stu2.init_attr("海励", 30, "男", 80, 130, 100)
print(stu2.get_all_scores())
stu2.get_avarage_scores()
stu2.print_stu_info()

题目4:
class Tool:

    def __init__(self,name,price,func_desc):
        self.name = name
        self.price = price
        self.func_desc = func_desc

    def print_tool_info(self):
        print(f"工具名称：{self.name}\n工具的价格: {self.price}\n工具的功能: {self.func_desc}\n")

class ToolBox:
    def __init__(self):
        self.tools = []     # 工具类对象

    def add_tool(self,tool_obj): # Tool类的对象作为方法的参数
        if tool_obj not in self.tools:
            self.tools.append(tool_obj)
        else:
            print("工具箱里已有！")

    def del_tool(self,tool_obj):
        if tool_obj in self.tools:
            self.tools.remove(tool_obj)
        else:
            print("工具箱里无此工具！")

    # 函数的参数  变量名: 数据类型/类    给形参一个注释 ，表示期望传入的类型。但是调用的时候可以传别的类型。
    # tool_obj: Tool
    def get_tool(self,tool_obj: Tool):
        if tool_obj in self.tools:
            tool_obj.print_tool_info()
        else:
            print("工具箱里无此工具！")

    def get_count_of_tools(self):
        count = len(self.tools)
        print("工具个数为：{}".format(count))


tool1 = Tool("锤子",50, "刨根")
tool2 = Tool("螺丝刀",10, "拧螺丝")
tool3 = Tool("锄头",100, "挖墙角")

# 实例化一个工具箱
tm = ToolBox()
# 添加一个工具
tm.add_tool(tool1)
tm.add_tool(tool2)
tm.add_tool(tool3)
tm.get_count_of_tools()
tm.get_tool(tool2)


题目4:
编写一个工具箱类和工具类
工具类：需要有工具具的名称、功能描述、价格。
工具箱类：能够添加工具、删除工具、查看工具，并且能获取工具箱中工具的总数。
实例化几个工具。并在工具箱对象当中做添加/删除/查看工具操作，获取工具箱对象中有几个工具。
工具比如锤子、斧头、螺丝刀等工具。
提示：不需要用到继承。

tm = ToolBox()
self.tools = [tool1,tool2,tool3] 
"""