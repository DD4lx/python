## 1.flask
>Flask是一个基于Python实现的web开发的'微'框架;

[中文文档地址](http://docs.jinkan.org/docs/flask/)

>flask的优点：（小巧灵活）
- 有非常齐全的文档介绍，易于上手；
- 有非常好的拓展机制和第三方的拓展环境，工作中常见的软件都有对应的拓展，自己动手实现拓展也很容易
- 微型框架的形式给了开发者更大的选择空间
## 2.安装flask
1. 安装虚拟环境
```
virtual --no-site-packages <envname>
```
2. 安装flask
```
进入虚拟环境，激活
pip install flask
```
## 3.基于flask的最小应用
在pycharm中创建一个py文件
```
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'hello world!'

if __name__ == '__main__':
    app.run()
```
运行：py文件，便可看见效果；
解析：
1. 初始化
```
from flask import Flask

app = Flask(__name__)
```
>Flask类构造函数唯一需要的参数就是应用程序的主模块或包。对于大多数应用程序，Python的```__name__```变量就是那个正确的、你需要传递的值。Flask使用这个参数来确定应用程序的根目录，这样以后可以相对这个路径来找到资源文件。
2. 路由
```
@app.route('/')
```
>客户端例如web浏览器发送 请求 给web服务，进而将它们发送给Flask应用程序实例。应用程序实例需要知道对于各个URL请求需要运行哪些代码，所以它给Python函数建立了一个URLs映射。这些在URL和函数之间建立联系的操作被称之为 路由 。

在Flask应程序中定义路由的最便捷的方式是通过显示定义在应用程序实例之上的app.route装饰器，注册被装饰的函数来作为一个 路由。

3. 视图函数
```
def gello_world():
	return 'Hello World'

```
>客户端接收到的这个函数的返回值被称为 响应 。如果客户端是web浏览器，响应则是显示给用户的文档。类似于gello_world()的函数被称作 视图函数 。
4. 动态名称组件路由
```
@app.route('/index/<name>')

def index(name):

	return 'Hello World %s' % name
```
>用尖括号括起来的部分是动态的部分，所以任何URLs匹配到静态部分都将映射到这个路由。当视图函数被调用，Flask发送动态组件作为一个参数。在前面的示例的视图函数中，这个参数是用于生成一个个性的问候作为响应。在路由中动态组件默认为字符串，但是可以定义为其他类型。例如，路由/user/int:id只匹配有一个整数在id动态段的URLs。Flask路由支持int、float;
5. 项目启动
```
if __name__ == '__main__':
    # app.run()
    # app.run(debug=True)
    app.run(host='0.0.0.0', port=8080, debug=True)
```
>注意： ```__name__``` == ```__main__```在此处使用是用于确保web服务已经启动当脚本被立即执行。当脚本被另一个脚本导入，它被看做父脚本将启动不同的服务，所以app.run()调用会被跳过。

>一旦服务启动，它将进入循环等待请求并为之服务。这个循环持续到应用程序停止，例如通过按下Ctrl-C。

>有几个选项参数可以给app.run()配置web服务的操作模式。在开发期间，可以很方便的开启debug模式，将激活 debugger 和 reloader 。这样做是通过传递debug为True来实现的。

>run()中参数有如下：
- debug: 是否开启调试模式，开启后修改python的代码会自动重启
- port: 启动指定服务器的端口号
- host:主机，默认是127.0.0.1
## 4.修改启动方式，使用命令行参数启动项目
1. 安装插件
```
pip install flask-script
```
2. 添加修改代码
```
from flask_script import Manager
manage = Manager(app)
# 启动项目
if __name__ == '__main__':
    # app.run(debug=True)
    # app.run(host='0.0.0.0', port=8080, debug=True)

    manage.run()
    # 使用manage方法就可以使用代码启动项目了python manage.py runserver -p -h -d
```
3. 启动命令
```
python hellow.py runserver -h 地址 -p 端口 -d -r
```
## 5.route规则（路由选择器）
1. 规则（<converter:variable_name>）
convertaer类型：
- string 字符串
- int 整形
- float 浮点型
- path 接受路径，接收的时候是str，/也当做字符串的一个字符
- uuid 只接受uuid字符串（常用用于生成唯一编码，例如上传图片，图片的命名）
- any 可以同时指定多种路径，进行限定
写法：
```
# 指定路由
@app.route('/index')
# 对应的函数
def index():
    return '<h1>Hello World!</h1>'


@app.route('/student/<int:id>/')
def student(id):
    return '学号%d的学生' % id


@app.route('/course/<id>/')
def course(id):
    return '我是%s的课程' % id


@app.route('/hello/<string:name>/')
def hello_name(name):
    return '你好，%s' % name


@app.route('/float/<float:number>/')
def hello_float(number):
    return f'我是float类型的参数：{number}'


@app.route('/path/<path:name>/')
def path(name):
    return f'path:{name}'


@app.route('/get_uuid/')
def get_uuid():
    # 生成唯一的id(可以用于上传图片)
    uu = uuid.uuid4()
    return str(uu)


@app.route('/uuid/<uuid:name>/')
def uuid_name(name):
    return f'uuid:{name}'

```
2. methods请求方法
常用的请求类型有几种：
- GET : 获取
- POST : 创建
- PUT : 修改(全部属性都修改)
- DELETE : 删除
- PATCH : 修改(修改部分属性)
>定义url的请求类型：
```
# 指定路由
@app_blueprint.route('/index/', methods=['GET','POST','PATCH'])
# 对应的函数
def index():
    if request.method == 'GET':
        # 获取get提交请求传递的参数：request.args
        # request.args[key]或者request.args.get(key)
        return '<h1>Hello World!</h1>'
    if request.method == 'POST':
        # TODO:获取post提交的参数
        # 获取post提交请求传递的参数：request.form

        return '你好，我是post请求'
```
## 6.蓝图
>在Flask项目中可以用Blueprint(蓝图)实现模块化的应用，使用蓝图可以让应用层次更清晰，开发者更容易去维护和开发项目。蓝图将作用于相同的URL前缀的请求地址，将具有相同前缀的请求都放在一个模块中，这样查找问题，一看路由就很快的可以找到对应的视图，并解决问题了。
## 7.安装注册蓝图
1. 安装
```
pip install flask_blueprint
```
2. 实例化蓝图应用
```
# 1.生成蓝图对象，使用蓝图对象管理路由
app_blueprint = Blueprint('app', __name__)
```
>注意：Blueprint中传入了两个参数，第一个是蓝图的名称，第二个是蓝图所在的包或模块，```__name__```代表当前模块名或者包名
3. 注册蓝图
```
# 注册蓝图
app = Flask(__name__)

app.register_blueprint(blueprint=app_blueprint,url_prefix='/app')
```
>注意：第一个参数即我们定义初始化定义的蓝图对象，第二个参数url_prefix表示该蓝图下，所有的url请求必须以/user开始。这样对一个模块的url可以很好的进行统一管理
## 8.使用蓝图
修改视图上的装饰器，修改为@app_blueprint.route('/')
```
# 指定路由
@app_blueprint.route('/index/', methods=['GET','POST','PATCH'])
# 对应的函数
def index():
    if request.method == 'GET':
        # 获取get提交请求传递的参数：request.args
        # request.args[key]或者request.args.get(key)
        return '<h1>Hello World!</h1>'
    if request.method == 'POST':
        # TODO:获取post提交的参数
        # 获取post提交请求传递的参数：request.form

        return '你好，我是post请求'
```
>注意：该方法对应的url为127.0.0.1:5000/app/index/
## 9.url_for反向解析
语法：
```
url_for('蓝图中定义的第一个参数.函数名', 参数名=value)
```
实例：
```
@app_blueprint.route('/redirect/')
def redirect_url():

    # 跳转
    # Django:HttpResponseRedirect(reverse('namespace:name'))
    # 第一种方法
    return redirect('/app/index/')
    # 第二种方法
    # Flask:redirect(url_for('蓝图名称.函数名', key=value))
    # return redirect(url_for('app.index'))
    return redirect(url_for('app.student', id=10))
```
## 10.请求request
>服务端在接收到客户端的请求后，会自动创建Request对象;由Flask框架创建，Request对象不可修改

属性：
- url：完整的请求地址
- base_url：去掉GET参数的url
- host_url：只有主机和端口号的url
- path：路由中的路径
- method：请求方法
- remote_addr：请求的客户端的地址
- args：GET请求参数
- form：POST请求参数
- files：文件上传
- headers：请求头
- cookies：请求中的cookie
```
def index():
    if request.method == 'GET':
        # 获取get提交请求传递的参数：request.args
        # request.args[key]或者request.args.get(key)
        return '<h1>Hello World!</h1>'
    if request.method == 'POST':
        # TODO:获取post提交的参数
        # 获取post提交请求传递的参数：request.form

        return '你好，我是post请求'
```
## 11.响应Response
>Response响应，是后端产生返回给前端的（浏览器），是由开发者自己创建的
```
# make_response(响应内容，响应状态码（默认为200）)
# 响应绑定cookie，set_cookie/delete_cookie
```
创建方法：
```
from flask import make_response
make_response创建一个响应，是一个真正的Response对象
```
>格式：make_response(data, code),其中data是返回的数据内容，code是状态码；
## 12.终止、异常捕获
自动抛出异常：abort(状态码)
捕获异常处理：errorhandler(状态码)，定义的函数中药包含一个参数，用于接受异常信息；
```
@app_blueprint.route('/abort_a/', methods=['POST'])
def abort_a():
    try:
        a = int(request.form.get('a'))
        b = int(request.form.get('b'))
        c = a/b
        return f'{a}/{b}={c}'
    except Exception as e:
        # 程序出错，抛出一个500的错误，异常，
        abort(500)
```
返回错误页面：
```
# 定义一个路由解析错误
@app_blueprint.errorhandler(500)
def error_handler(error):
    # 一般返回错误页面
    return f'Exception is {error}'
```