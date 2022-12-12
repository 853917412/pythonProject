"""
============================
Project: py49
Author:柠檬班-海励
Time:2022/4/25 20:20
E-mail:2227092769@qq.com
Company:湖南零檬信息技术有限公司
Site: http://www.lemonban.com
Forum: http://testingpai.com 
============================
"""
"""
四、jsonpath
1、安装第三方库
pip install jsonpath

2、使用
特点：
用来匹配指定规则的json，只能处理json数据
jsonpath提取数据，数据原来是什么数据类型，提取出来就是什么数据类型，只是放在list中返回而已
语法：
[]: 子元素操作符
res1 = jsonpath(teacher_info,"$[lemon][python]")
.: 子元素
res1 = jsonpath(teacher_info,"$.lemon.python")
..: 递归查找，同一级目录不能有相同的key，如果有相同的key只会拿到最后一个key的值(相当于覆盖了)
res1 = jsonpath(teacher_info,"$..python")

按索引取值
res1 = jsonpath(teacher_info,"$..python[0]")

切片，同list的切片
res1 = jsonpath(teacher_info,"$..python[0:3]")

去指定字段的值，多个字段用逗号隔开
res1 = jsonpath(teacher_info,"$..python.[name,age]")

条件表达式
res1 = jsonpath(teacher_info,"$..python.[?(@.age>18)]")
res1 = jsonpath(teacher_info,"$..python.[?(@.sex=='女')]")

成员运算
res1 = jsonpath(teacher_info,"$..python.[?(@.name in ['木森','心蓝'])]")
res1 = jsonpath(teacher_info,"$..python.[?(@.name not in ['木森','心蓝'])]")

逻辑运算
res1 = jsonpath(teacher_info,"$..python.[?(@.age>20 && @.height>175)]")
res1 = jsonpath(teacher_info,"$..python.[?(@.age>=30 || @.height>175)]")

字段截取
res1 = jsonpath(teacher_info,"$..python.[?(@.name  in ['木森','心蓝'])].[age,height]")
"""

teacher_info = {
    "lemon":
    {
    "python": [
        {"name": "海励",
         "sex": "男",
         "age": 30,
         "height": 175,
         "info":"python自动化老师",
         },
        {"name": "木森",
         "sex": "男",
         "age": 28,
         "height": 185,
         "info":"python测开老师"
         },
        {"name": "小简",
         "sex": "女",
         "age": 18,
         "height": 170,
         "info":"python自动化老师"
         },
         {"name": "心蓝",
         "sex": "男",
         "age": 28,
         "height": 185,
          "info":"python测开老师"
         },
         {"name": "雨泽",
         "sex": "男",
         "age": 28,
         "height": 190,
         "info":"python自动化老师"
         }
    ],
    "java": {
        "name": "三宝",
        "sex": "男",
        "age": 30,
        "height": 185.5,
        "info":"java测开老师"
    }
}
}

# print(teacher_info["lemon"]["python"][0])


from jsonpath import jsonpath


# res1 = jsonpath(teacher_info,"$[lemon][python]")
# res1 = jsonpath(teacher_info,"$.lemon.python")
# res1 = jsonpath(teacher_info,"$..python[0]")
# res1 = jsonpath(teacher_info,"$..python.[name,age]")
# res1 = jsonpath(teacher_info,"$..python[0:3]")
# res1 = jsonpath(teacher_info,"$..python.[?(@.age>18)]")
# res1 = jsonpath(teacher_info,"$..python.[?(@.sex=='女')]")
# res1 = jsonpath(teacher_info,"$..python.[?(@.name not in ['木森','心蓝'])]")
res1 = jsonpath(teacher_info,"$..python.[?(@.age>20 and @.height>175)]")  # and &&
# res1 = jsonpath(teacher_info,"$..python.[?(@.age>=30 || @.height>175)]") # or ||
# res1 = jsonpath(teacher_info,"$..python.[?(@.name  in ['木森','心蓝'])].[age,height]")
print(type(res1),res1)








