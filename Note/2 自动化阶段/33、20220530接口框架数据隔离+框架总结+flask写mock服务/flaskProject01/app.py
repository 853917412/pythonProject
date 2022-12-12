from flask import Flask,jsonify
from flask import request
#django
app = Flask(__name__)
@app.route('/test_demo')
def hello_world():
    #获取get请求的参数
    name = request.args.get("name")
    #获取post请求的数据
    name2 = request.form.get("name")
    # return 'Hello World!' 返回字符串
    return jsonify({"key1":"value"}) #返回字典

if __name__ == '__main__':
    app.run()
