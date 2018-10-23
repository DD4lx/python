## 创建app
>Terminal窗口下：```python manage.py startapp <name>```;创建一个功能app,代码文件中就多了一个app文件夹,其中有很多文件，对应不同的功能；
- ```__init__.py```:一个空文件，告诉python这个目录应该被认为是一个python包。
- ```admin.py```:可以用来注册模型，让Django自动创建管理界面。
- ```apps.py```:当前应用的配置。
- ```migrations```:存放与模型有关的数据库迁移信息。
- - ```__init__.py```:一个空文件，告诉python这个目录应该被认为是一个python包。
- ```models.py```:存放应用的数据模型，即实体类及其之间的关系（MVC/MVT中的M）。
- ```tests.py```:包含测试应用各项功能的测试类和测试函数。
- ```views.py```:处理请求并返回响应的函数（MVC中的C，MVT中的V）。
## 写自己的路由(urls)和方法(views)
- 在urls.py中定义一个路由，访问app中的hello对象方法：```url(r'^hello/', views.hello)```,
- 在views.py中创建对应的hello方法：
```
from django.http import HttpResponse

def hello(requst):
    return HttpResponse('你好，Django')
```
## 在Django中定义自己的模型，并迁移到数据库中：
>ORM（object-relational-mapping）对象关系映射,
可以不用写原生的SQL语句，直接使用orm提供的方法；例如，```all()#查询所有数据```,但是当查询语句很复杂的时候，使用orm可能会影响效率，这时候，就会考虑使用SQL语句；
- 在models.py文件中定义模型：
```
class Student(models.Model):
    # 定义s_name字段，varchar类型，最长不超过6个字符，唯一
    s_name = models.CharField(max_length=6, unique=True)
    # 定义s_age字段，int类型,默认值为18
    s_age = models.IntegerField(default=18)
    # 定义s_gender字段，bit类型，默认值为1
    s_gender = models.BooleanField(default=1)

    class Meta:
        # 定义模型迁移到数据库中的表名
        db_table = 'student'
```

- 在setting.py中将自己的app加入到INSTALLED_APPS；
```
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'app',
]
```
- 然后运行```python manage.py makemigrations```，生成一个迁移文件在migrations文件夹中，该迁移文件包含建表的一些信息；
- 最后执行```python manage.py migrate```,将表迁移到数据库中；
- 数据库中表django_migrations中多了一条记录；
- 更新数据库，为表新增两个字段
```
   # 定义create_time字段，创建时间，不再更改,默认为空
   create_time = models.DateTimeField(auto_now_add=True, null=True)
   # 定义修改时间operate_time字段，修改时间,每次修改的时候，都更新最新的时间，默认为空
   opreate_time = models.DateTimeField(auto_now=True, null=True)
```
- 再次执行```python manage.py makemigrations``` 和 ```python manage.py migrate```就可以了；



## 向数据库中插入数据
- 在urls.py中定义创建数据的路由：```url(r'^create_stu/', views.create_stu)```,
- 在views中创建create_stu方法
```
from app.models import Student
def create_stu(request):
    # 创建学生
    stu = Student()
    stu.s_name = '小李'
    stu.s_age = 20
    stu.save()
    return HttpResponse('创建成功')
```
- 再执行一次，就会报错‘Duplicate’，因为s_name具有唯一性约束；
- 第二种方式：（对象自带一个object对象）
```
Student.object.create(s_name='小王')
return HttpResponse('创建成功')
```
## 使用Debug：
- 如果关闭了服务器，浏览器还是正常显示，就换端口。debug项目，往下执行一步，切换到‘Console’页面，点击‘show python prompt’图标，输入变量名；
## 查询：
```
def sel_stu(request):
    # 实现查询
    # all()查询所有对象信息
    stus = Student.objects.all()
    # filter()过滤
    stus = Student.objects.filter(s_name='小王')
    # first()获取第一个对象
    # last()获取最后一个对象
    stus = Student.objects.filter(s_age=20).first()
    # get方法与上面效果相同，容易出错
    stus = Student.objects.get(s_age=20)
```
###### 注意：当filter里的条件超出范围时，返回一个空集合，当get方法里的条件超出时，会报错；get()方法拿不到值会报错，拿到多个值，也会报错；
```
# 模糊查询 like
    # 包含
    stus = Student.objects.filter(s_name__contains='司')
    stu_names = [stu.s_name for stu in stus]
    print(stu_names)

    # 以开头
    stus = Student.objects.filter(s_name__startswith='小')
    stu_names = [stu.s_name for stu in stus]
    print(stu_names)

    # 以结尾
    stus = Student.objects.filter(s_name__endswith='蝉')
    stu_names = [stu.s_name for stu in stus]
    print(stu_names)

    # 大于/大于等于 gt/gte 小于小于等于 lt/lte
    stus = Student.objects.filter(s_age__gt=18)
    stus = Student.objects.filter(s_age__gte=18)
    stu_names = [stu.s_name for stu in stus]
    print(stu_names)

    # 排序 order_by()
    # 升序
    stus = Student.objects.order_by('id')
    # 降序
    stus = Student.objects.order_by('-id')

    # 查询不满足条件的数据 exclude()
    stus = Student.objects.exclude(s_age=20).order_by('id')

    # 计算统计的个数：count()\len()
    print(len(stus))
    stus_count = stus.count()
    print(stus_count)

    # values()
    stus_values = stus.values()
    print(stus_values)
    # id 一般= pk(primary key)
    stus = Student.objects.filter(id=3)
    stus = Student.objects.filter(pk=3)

    stu_names = [stu.s_name for stu in stus]
    print(stu_names)
    return HttpResponse('查询成功')

```











