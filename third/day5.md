## 模板重定向
>首先，需要导入HttpResponseRedirect包；使用HttpResponseRedirect()方法，通过代码注释理解
```
# 实现重定向到index方法上去
# 第一种重定向
# 地址用的硬编码
# return HttpResponseRedirect('/app/index/')
# HttpResponse()返回响应结果
# render()渲染页面的方法
# 第二种重定向，使用反向解析reverse('namespace:name')
# 规范写法
# 导入reverse包
# 在项目的urls.py和app的urls.py 对路由进行别名；
return HttpResponseRedirect(reverse('dy:all'))

```
>其中需要对项目的应用和路由进行别名：
```
# 在应用路由地址中别名
url(r'^index/', views.index, name='ind'),
url(r'^all_stu/', views.all_stu, name='all'),

# 在项目路由中给app路由取个别名，改变include中的namespace=xxx
url(r'^app/', include('app.urls',namespace='dy')),
```
>不止views.py中可以使用路由反向解析，在HTML页面中也可以使用反向解析：```{% url 'namespace:name' %}```
```

{# HTML页面中使用反向解析:{% url 'namesapce:name' 变量 %} #}
<!--<a href="/app/edit_stu/{{ stu.id }}/">编辑</a>-->
<!--HTML页面中反向解析格式-->
<a href="{% url 'dy:edit' stu.id %}">编辑</a>
```
## 用户注册、登录和注销功能的实现
>用户注册实现步骤：
1. 在项目的urls.py中创建应用路由：
   ```url(r'^user/', include('user.urls', namespace='user')),```
2. 在应用目录下的urls.py中创建路由：
``` 
# 注册
url(r'^register/', views.register, name='register'),
```
3. 在models.py中创建用户所对应的数据库表User:
```
class User(models.Model):
    username = models.CharField(unique=True, max_length=20, verbose_name='用户名')
    password = models.CharField(max_length=200)
    email = models.CharField(max_length=30, null=True)
    create_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'user'
```
4. 在templates中创建4个html页面

base.html
```
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>
        {% block title %}
        {% endblock %}

        {% block css %}
        {% endblock %}
    </title>
</head>
<body>
    {% block content %}
    {% endblock %}

    {% block js %}
    {% endblock %}
</body>
</html>
```
register.html
```
{% extends 'base.html' %}

{% block content %}
    <form action="" method="post">
        姓名：<input type="text" name="username" placeholder="请输入用户名">
        密码：<input type="password" name="password" placeholder="请输入密码">
        确认密码：<input type="password" name="sure_password" placeholder="确认密码">
        <input type="submit" value="注册">
    </form>
{% endblock %}

```
login.html
```
{% extends 'base.html' %}
{% block content %}
<form action="" method="post">
    用户名：<input type="text" name="username" placeholder="请输入用户名">
    密码：<input type="password" name="password" placeholder="请输入密码">
    <input type="submit" value="登录">
</form>
{% endblock %}
```
index.html
```
{% extends 'base.html'%}
{% block content %}
    <h2>欢迎光临</h2>
    <a href="{% url 'user:logout' %}">注销</a>
{% endblock %}
```
5. 在views.py中实现注册功能：
```
def register(request):
    if request.method == 'GET':
        return render(request, 'register.html')

    if request.method == 'POST':
        # 用于创建用户
        # 获取参数
        name = request.POST.get('username')
        password = request.POST.get('password')
        sure_password = request.POST.get('sure_password')
        # 2.校验参数是否完整
        if not all([name, password, sure_password]):
            msg = '请填写完整的参数'
            return render(request, 'register.html', {'msg': msg})
        # 3.先判断数据库中是否存在该name的用户
        if User.objects.filter(username=name).first():
            msg = '该账号已注册，请去登录'
            return render(request, 'register.html', {'msg': msg})
        # 4.校验密码是否一致
        if password != sure_password:
            msg = '密码不一致'
            return render(request, 'register.html', {'msg': msg})
        # 5.注册
        User.objects.create(username=name, password=password)
        # 不能使用渲染，要使用跳转
        # return render(request, 'login.html')
        return HttpResponseRedirect(reverse('user:login'))
```
>登录功能：因为Http协议，具有一个无状态的协议；所以需要通过使用cookie和session来标识用户是登录成功的或者成功登录过，这样，用户下次访问网站就不需要再次登录了，除非就浏览器中cookie删除了；这样就相当于，在访问页面的时候，就先判断你的标识符是否与该网站的标识符匹配，如果匹配，则放行，可以正常浏览；如果不匹配，则不让访问；
1. 在urls.py中加入一个登录页面路由：
```
# 登录
url(r'^login/', views.login, name='login'),
```
2. 由于这时涉及到一个cookie令牌，所以需要创建一个token数据库表来存储浏览器产生的cookie数据；
```
class UserToken(models.Model):
    # 标识符，用于用户访问需要登录验证页面的时候使用，校验标识符是否正确；
    token = models.CharField(max_length=30, verbose_name='标识符')
    user = models.OneToOneField(User)

    class Meta:
        db_table = 'usertoken'
```
3. 在views.py中实现登录功能：
```
def login(request):
    if request.method == 'GET':
        return render(request, 'login.html')

    if request.method == 'POST':
        # 1.获取参数
        name = request.POST.get('username')
        password = request.POST.get('password')
        # 2.验证数据完整性
        if not all([name, password]):
            msg = '请填写完整的登录信息'
            return render(request, 'login.html', {'msg': msg})
        # 3.验证用户是否注册
        user = User.objects.filter(username=name).first()
        if not user:
            msg = '该账户没有注册，请去注册'
            return render(request, 'login.html', {'msg': msg})
        # 4.校验密码
        if password != user.password:
            msg = '密码不正确'
            return render(request, 'login.html', {'msg': msg})
        # 5.标识符（重点）
        # 请求与响应：
        # 请求：是从浏览器发送请求的时候，传递给后端的。
        # 响应：后端返回给浏览器的
        res = HttpResponseRedirect(reverse('user:index'))
        # set_cookie(key, value, max_age)绑定了一个cookie值，把标识符丢给页面，浏览器会存起来
        token = ''
        s = '1234567890qazwsxedcrfvtgbyhnujmiklop'
        for i in range(25):
            token += random.choice(s)
        res.set_cookie('token', token, max_age=6000)

        # 服务端数据库存token值
        user_token = UserToken.objects.filter(user=user).first()
        if not user_token:
            UserToken.objects.create(token=token, user=user)
        else:
            user_token.token = token
            user_token.save()

        return res
```
> 当用户登录成功后，浏览器就会生成一个cookie字典，当用户下次访问index的时候，不需登录就可以直接访问，而用户是第一次访问的话，就必须先登录才行；这时，就需要对index页面做一些设置；
1. 在urls.py中添加一个首页路由，和注销路由
```
# 首页
url(r'^index/', views.index, name='index'),
# 注销
url(r'^logout/', views.logout, name='logout'),
```
2. 在浏览器和服务器中分别对用户的cookie进行一个判断：即查询cookie和删除cookie（注销）
```
@login_required
def index(request):
    if request.method == 'GET':
        # # 可以拿到COOKIES的值
        # token = request.COOKIES.get('token')
        # # 查询标识符是否有效
        # user_token = UserToken.objects.filter(token=token).first()
        # if not user_token:
        #     # 查询不到信息，说明用户没有登录
        #     return HttpResponseRedirect(reverse('user:login'))
        # 上述方法可以闭包，创建一个装饰器来封装功能，

        return render(request, 'index.html')


@login_required
def logout(request):
    if request.method == 'GET':
        # 1.删除浏览器cookie中的token参数
        res = HttpResponseRedirect(reverse('user:login'))
        res.delete_cookie('token')
        # 2.删除usertoken中的数据
        token = request.COOKIES.get('token')
        UserToken.objects.filter(token=token).delete()

        return res

```
3. 由于在上述两个方法中都需要对cookie值进行查询和判断，因此可以将该方法闭包，生成一个装饰器，避免重复代码；
   在项目中新建一个‘utls’python工具包，用于存放公共方法；

functions.py
```
# 定义登录验证的装饰器
# 闭包的三个条件；
# 1.外层函数套内层函数
# 2.内层函数调用外层函数的参数(函数)
# 3.外层函数返回内层函数
from django.http import HttpResponseRedirect
from django.urls import reverse

from user.models import UserToken


def login_required(func):

    def check_login(request):
        # func是被login_required装饰的函数
        token = request.COOKIES.get('token')
        if not token:
            # cookie中没有登录的标识符，跳转到登录界面
            return HttpResponseRedirect(reverse('user:login'))
        user_token = UserToken.objects.filter(token=token).first()
        if not user_token:
            # token标识符有误，跳转到登录界面
            return HttpResponseRedirect(reverse('user:login'))
        return func(request)

    return check_login
```

结果：

![结果](C:\Users\Administrator\Downloads\login.gif)