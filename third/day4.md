## 表与表之间的关联关系（续）
>多对多关系：以学生与课程表之间的关系为例
```
# 建课程表，与学生表的关系是多对多
class Course(models.Model):
    c_name = models.CharField(max_length=10)
    # 多对多关联字段
    stu = models.ManyToManyField(Student)

    class Meta:
        db_table = 'course'
```
**使用ManyToManyField()方法会自动创建一个中间表，只包含id和两个表的主键作为外键的三个字段；如果需要中间表添加额外的字段，就通过创建两个一对多的关系来关联多对多关系；**
>多对多关系表的查询、增加和删除操作：
```
def add_stu_course(request):
    if request.method == 'GET':
        cous = Course.objects.all()
        return render(request, 'course.html', 
{'cous': cous})

    if request.method == 'POST':
        # 获取课程id和学生id
        # cous_id是select标签的名字name的值
        c_id = request.POST.get('cous_id')
        s_id = request.GET.get('stu_id')
        # 获取学生对象
        stu = Student.objects.get(pk=s_id)
        # 通过学生表和课程表之间的多对多关系,然后调用add方法，中间表就会多一条记录；
        course = Course.objects.get(pk=c_id)
        # stu.course_set.add(course)
        # 删除
        # stu.course_set.remove(course)
        course.stu.add(stu)
        # return HttpResponse('选课成功')

        # 跳转(重定向)，首先需要导入包HttpResponseRedirect,重定向状态码302；
        return HttpResponseRedirect('/all_stu/')
```
## 模板（MVT中的T）：简单说就是将后台数据体现在HTML页面中
>在templates目录下的模板里可以直接使用多表间的数据(先尝试下面的例子)：
```
    <table>
        <thead>
            <th>姓名</th>
            <th>年龄</th>
            <th>电话</th>
            <th>课程</th>
            <th>操作</th>
        </thead>
        <tbody>
            {% for stu in students %}
            <tr>
                <td>{{stu.s_name}}</td>
                <td>{{stu.s_age}}</td>
                <td>{{ stu.studentinfo.phone }}</td>
                <td>
                    {% for cou instu.course_set.all %}
                        {{ cou.c_name }}
                    {% endfor %}
                </td>
                <td>

                </td>
                <td>
                    <a href="/add_info/?stu_id={{ stu.id }}">添加扩展信息</a>
                    |
                    <a href="/add_stu_course/?stu_id={{ stu.id }}">添加课程</a>
                </td>
            </tr>
        {% endfor %}
        </tbody>
    </table>
```
>创建模板的一般步骤：
1. 首次创建模板，建议在项目的urls.py文件中导入include包；
```
from django.conf.urls import include
```
2. 在urls.py中定义项目功能应用的路由地址：
```
# 127.0.0.1:8080/app/xx
url(r'^app/', include('app.urls'))
```
3. 在不同功能app目录下创建各自的urls.py文件，并在其中定义属于自己功能的路由地址：
```
from django.conf.urls import url

from app import views

urlpatterns = [
    url(r'^index/', views.index)
]
```

**这样做的好处是将一个项目的路由地址进行了分类，简洁明了；以后要查看哪个功能的路由地址时，直接到对应的功能app文件夹下查找就可以了。**
## 模板（HTML页面）之间的继承
>父模板base.html：相当于在页面中留一些空（挖坑）以便以后更新数据；
```
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>
        {% block title %}
        {% endblock %}
    </title>
    {% block css %}
    {% endblock%}

</head>
<body>
    {% block content %}
    {% endblock %}

    {% block js %}
    {% endblock %}
</body>
</html>
```
>初始化模板（子模板）-base_main.html:在开发时，一般在父模板中是不会有数据的，所以，要想初始化父模板的话，是通过新建一个继承自父模板的子模板来实现的；这是一种习惯，实在是不想在子模板中初始化也可以。

下面就是初始化父模板中的js块:导入jQuery；
```
{% extends 'base.html' %}

{% block js %}
    <script src="https://cdn.bootcss.com/jquery/2.1.4/jquery.min.js"></script>
{% endblock %}
```
>子模板-index.html:就是继承父模板，然后在你想要填充内容的地方，补充内容（填坑）;
```
{% extends 'base_main.html' %}
{% block title %}
    我是首页
{% endblock %}

{% block content %}
    <p>你好，Django</p>
{% endblock %}
```
## Django提供了一些方法，使得创建模板很方便：
- ```{% block xxx %}{% endblock %}```块方法，挖坑，填坑
- ```{{ 变量 }}```，解析views.py中方法中变量所对应的值；
- ```{# 注释 #}```,单行注释，这个注释功能较为强大，html中的注释，在浏览器中查看源代码时，能看见注释，而使用该注释方法，是看不见的；
- ```{% content %} {% endcomment %}```,多行注释；
- ```{{ block.super }}```,调用父模板中的内容；
- ```{% load static %}```,加载静态文件；
- 
## Django中使用静态文件
- 先在项目的settings.py文件中定义静态路由，```STATIC_URL = '/static/'```
- 紧接着指定静态目录stattic的地址
```
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static')
]
```
- 但是我们的项目中没有static文件夹，所以要在项目中创建一个名为static的文件夹，以存储项目所涉及的一些静态文件，比如，CSS，JS，img等；
- 这里以在页面中加载静态文件CSS文件为例：
```
<!--加载静态文件css的两种方式-->
    <!--<link rel="stylesheet" href="/static/css/index.css">-->
    <!--规范的模式-->
    {% load static %}
    <link href="{% static 'css/index.css' %}" rel="stylesheet">
```
