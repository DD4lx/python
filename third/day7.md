## 将登录跳转到首页时的装饰器改为中间件：
- 会出现重定向次数太多的问题，状态码302
- 这时可以将登录和注册的url路由屏蔽掉
```
class TestMiddleware(MiddlewareMixin):

    def process_request(self, request):
        # 屏蔽掉登录和注册的url，不需要做登录验证

        no_check = ['/user/login/', '/user/register/']
        path = request.path
        if path in no_check:
            # 不需要执行以下登录验证的代码，直接执行视图函数
            return None
        token = request.COOKIES.get('token')
        if not token:
            # cookie中没有登录的标识符，跳转到登录界面
            return HttpResponseRedirect(reverse('user:login'))
        user_token = UserToken.objects.filter(token=token).first()
        if not user_token:
            # token标识符有误，跳转到登录界面
            return HttpResponseRedirect(reverse('user:login'))
        # 给全局request对象修改user属性值，修改为当前登录用户
        request.user = user_token.user
        return None
```

**注意：给全局request对象修改user属性值，修改为当前登录用户```request.user = user_token.user```,这样可以全局使用当前user对象；而使用Django时，auth.login方法会自带给全局request对象修改user属性值，修改为当前登录用户的功能**



## 上传图片的实现
1. 首先在项目中创建一个media文件夹，用来存放图片，然后在settings.py中配置media路径：
```
# 配置media路径
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
```
2. 在models.py模型中定义文章表：
```
class Article(models.Model):
    title = models.CharField(max_length=20)
    desc = models.CharField(max_length=150)
    # 上传到article文件夹里
    img = models.ImageField(upload_to='article')
    create_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'article'
```
**注意：在使用imageField的时候，需要安装Pillow库```"pip install Pillow"```;迁移的时候，没有article表，数据库中migration表中已经有记录了，应该先将他删除了，再迁移；**
3. 在添加文章页面提交时，一定要在form属性中添加```<form action="" method="post"enctype="multipart/form-data">```

article.html：
```
<form action="" method="post" enctype="multipart/form-data">
    标题：<input type="text" name="title" placeholder="请输入标题"><br>
    描述：<input type="text" name="desc" placeholder="请添加描述"><br>
    图片：<input type="file" name="img" value="请选择上传图片"><br>

    <input type="submit" value="提交">
</form>
```
4. 这时候，就可以通过request.FILES拿到图片request.POST 拿到数据存的是图片的路径，存放在media文件夹下upload_to属性的值对应的文件夹下面；
5. 但是图片在页面中显示不出来，这时就需要将media文件夹解析为静态文件夹，在urls.py文件中，先导包```from django.contrib.staticfiles.urls import static```;然后在urls.py中加上一段代码
```
# Django在debug为true的情况下，就可以访问media文件夹的内容了
urlpatterns += static(MEDIA_URL, document_root=MEDIA_ROOT)
```
## 分页的实现
views.py
```
# 查询文章列表
def articles(request):
    if request.method == 'GET':
        # 如果拿不到page,就使用第二参数的值；
        page = request.GET.get('page', 1)
        # 查询所有的文章
        arts = Article.objects.all()
        # 导入包Paginator,进行分页
        paginator = Paginator(arts, 3)
        # 通过自带的page方法获取具体某一页的内容
        page_art = paginator.page(page)
        return render(request, 'arts.html', {'page_art': page_art})
```
arts.html
```
<table>
    <thead>
    <th>标题</th>
    <th>描述</th>
    <th></th>
    </thead>
{% for x in page_art %}
    <tr>
        <td>{{ x.title }}</td>
        <td>{{ x.desc }}</td>
    </tr>
{% endfor %}
    <tr>
        {% for i in page_art.paginator.page_range %}
        <a href="{% url 'user:articles' %}?page={{ i }}">{{ i }}</a>
        {% endfor %}
    </tr>
    <tr>
        {% if page_art.has_previous %}
        <a href="{% url 'user:articles' %}?page={{ page_art.previous_page_number}}">上一页</a>
        {% endif %}

        <a href="{% url 'user:articles' %}?page={{ page_art.number}}">当前第{{ page_art.number }}页</a>

        {% if page_art.has_next %}
        <a href="{% url 'user:articles' %}?page={{ page_art.next_page_number }}">下一页</a>
        {% endif %}

    </tr>
</table>
```
**注意：```paginator = paginator(all_articles, 3)```---参数:所有的文章条数，一页的条数；简言之，按3条分页；**
## 生成日志：
1. 向项目中创建一个logs日志文件夹，用于存放日志文件；
2. 在settings.py中配置日志
```
# 配置日志
LOGGING = {
    # 必须是1
    'version': 1,
    # 是否禁用日志
    'disable_existing_loggers': False,
    # 指定formatters,指定写入到日志文件中的日志格式
    'formatters': {
        'default': {
            'format': '%(name)s %(asctime)s %(message)s'
        }
    },
    # 处理日志，指定格式存于哪个文件夹
    'handlers': {
        'console': {
            'level': 'INFO',
            # 存在哪里
            'filename': '%s/log.txt' % os.path.join(BASE_DIR, 'logs'),
            # 指定格式写日志
            'formatter': 'default',
            # 当大于多少时，会自动备份
            'class': 'logging.handlers.RotatingFileHandler',
            #  当日志文件大于5M,就自动备份
            'maxBytes': 5 * 1024 * 1024,
        }
    },
    # 接受日志,给handler处理
    'loggers': {
        '': {
            'handlers': ['console'],
            'level': 'INFO'
        }
    }

}

```
3. 在中间件middleware.py文件中写日志
```
class LoggingMiddleware(MiddlewareMixin):
    def process_request(self, request):
        # 记录当前请求访问服务器的时间，请求参数，请求内容
        request.init_time = time.time()
        request.inin_body = request.body
        return None

    def process_response(self, request, response):
        try:
            # 记录返回响应的时间和访问服务器的时间的差，记录返回状态码
            times = time.time() - request.init_time
            # 响应状态码
            code = response.status_code
            # 响应内容
            res_body = response.content
            # 请求内容
            req_body = request.init_body

            # 存到日志里面
            msg = '%s %s %s %s' % (times, code, res_body, req_body)
            # 写入日志
            logging.info(msg)
        except Exception as e:
            logging.critical('log error, Exception: %s' % e)

        return response

```












