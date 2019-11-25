'''
flask配置使用livereload
更新模板文件，则会自动重新启动flask，并且前台页面也会自动刷新。
注意：启动模式需要切换为纯python，默认的flask启动模式会出错，因为
默认的启动是 python.exe" -m flask run
纯python的启动是 python.exe  ***.py
简单区别就是 flask默认是5000端口
livereload模式是5500端口

'''
from flask import Flask,render_template
from livereload import Server

app = Flask(__name__)
app.debug=True

@app.route('/')
def hello_world():
    return render_template('index.html')


if __name__ == '__main__':
    server = Server(app.wsgi_app)
    server.watch('**/*.*')
    server.serve(open_url=True)
    # app.run()
