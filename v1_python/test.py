# coding=utf-8

from flask import Flask ### 到处 Flask 类

app = Flask(__name__) ### 生成一个web app对象

@app.route("/") ### 注册一个路由

def hello():
    return "Hello World! aaa"

if __name__ == '__main__':
	app.run()