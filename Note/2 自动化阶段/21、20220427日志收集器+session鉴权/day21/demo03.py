"""
============================
Project: py49
Author:柠檬班-海励
Time:2022/4/27 21:31
E-mail:2227092769@qq.com
Company:湖南零檬信息技术有限公司
Site: http://www.lemonban.com
Forum: http://testingpai.com 
============================
"""
import logging
from logging import handlers


def my_log():
    # 1、创建日志收集器
    py49 = logging.getLogger(name="py49")

    # 2、创建日志渠道
    pychacrm = logging.StreamHandler()
    # 文件渠道
    log_file = handlers.TimedRotatingFileHandler(filename="python.log", when="midnight", backupCount=10, encoding="utf-8")

    # 3、创建日志格式
    fmt = "%(name)s-%(levelname)s-%(asctime)s-%(pathname)s-%(lineno)d>>>: %(message)s"
    fmt1 = logging.Formatter(fmt=fmt)

    # 4、给输入渠道绑定日志格式
    pychacrm.setFormatter(fmt=fmt1)
    log_file.setFormatter(fmt=fmt1)

    # 5、日志级别: 设置在日志收集器上
    # 可以单独给渠道设置日志级别，但是一定小于收集器日志级别
    # debug < info < warning < error < critical
    py49.setLevel(logging.INFO)

    # 6、渠道绑定到收集器
    py49.addHandler(pychacrm)
    py49.addHandler(log_file)
    return py49

myLog = my_log()




