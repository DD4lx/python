## 查询(续)
>或条件：
- **补充**：导包的快捷键（alt + enter）
- 首先要导入Q对象：```from django.db.models import Q```;
- 查询年龄为20或者性别为女的学生：```stus = Student.objects.filter(Q(s_age=20) | Q
(s_gender=0))```

>且条件
- 查询年龄为20且性别为女的学生
```
# 第一种方式
stus = Student.objects.filter(Q(s_age=20), Q
(s_gender=0))
# 第二种方式
stus = Student.objects.filter(Q(s_age=18) & Q
(s_gender=0))
```
>非条件
- 查找年龄不是20的学生：
```stus = Student.objects.filter(~Q(s_age=20))```
>查询语文成绩比数学成绩高5分的学生信息：
前提需要导入F对象：
```from django.db.models import F```
```
stus = Student.objects.filter(chines__gt=F('math') + 5)
```
## 删除
>模型名.objects.filter(条件).delete()
- 删除名为小王的学生记录
```
 Student.objects.filter(s_name='小王').delete()
```
## 更新
>模型名.objects.filter(条件).update(字段=值)
- 更新姓名为小李的学生的姓名为李世民；先过滤查找出该记录，再改变对应字段的值；
```
stu = Student.objects.filter(s_name='小李').first()
# Student.objects.get(s_name='小李')
stu.s_name = '李世民'
stu.save()
return HttpResponse('修改成功')
```
## 数据库表间的关联关系
>1.一对一：OneToOneFiled()方法，
在创建表的对象的时候，使用OneToOneFiled方法关联相应的表对象；

例子：
```
class StudentInfo(models.Model):
    phone = models.CharField(max_length=11,null=True)
    address = models.CharField(max_length=100,null=True)
    # OneToOneField指定一对一关联关系,在数据库中显示的字段名为stu_id，定义外键的时候，Django会自动为字段加上‘_id’；
    
    stu = models.OneToOneField(Student)

    class Meta:
        db_table = 'student_info'
```
>2.一对多：在多的一方使用ForeignKey()方法添加一个外键约束，创建方法与一对一类似。

例子：为学生表设置一个班级外键；
```
grade = models.ForeignKey(Grade, null=True)
```
**注意**：在数据库表中会自动补充‘_id’,多一列‘grade_id’；
>3.使用Templates(MVT中的T)模板步骤：
1. 创建一个名为templates的文件目录；
2. 在setting.py文件中设置```DIRS```的值：```'DIRS': [os.path.join(BASE_DIR, 'templates')]```；其中，BASE_DIR的值为```BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))```表示项目的绝对路径；
3. 在urls.py中新建一个url连接```url(r'^all_stu/', views.all_stu)```
4. 在views.py中创建其对应的方法：
```
def all_stu(request):
    # 获取所有学生信息
    stus = Student.objects.all()
    # 返回页面，渲染页面(请求，页面，字典数据)
    return render(request, 'stus.html', {'students': stus})
```
5. 编写HTML页面
```
<body>
    <!--{{}}数据解析-->
    {{ students }}
    {% for stu in students %}
    <p>姓名：{{stu.s_name}},年龄：{{stu.s_age}}</p>
    {% endfor %}
</body>
```
>**补充**：获得请求数据的两种方法:request.POST.get()、request.GET.get()

>一对一关联数据库表的查询：通过一张表中的记录信息查找另外一张表中对应的记录的其他信息；
```表对象.关联的模型名的小写```

通过学生的姓名查找学生的扩展信息表：
```
stu =Student.objects.get(s_name='李元霸')
# 第一种方式
info = StudentInfo.objects.filter(stu_id=stu.id)
# 或者
info = StudentInfo.objects.filter(stu=stu)
# 第2种方式，学生对象.关联的模型名(与模型名本身大小写没有关系)的小写
info = stu.studentinfo
```
通过扩展表中的手机号查找学生表里的信息：
```
# 获取该手机号所对应的记录对象
info = StudentInfo.objects.get(phone='13645578923')
# 记录对象.设置的OneToOneFiled所对应属性名
student = info.stu
```
>一对多关联数据库表的查询：与一对一类似，但是有部分差异

例子：
```
# 1.通过学生查找班级
stu = Student.object.filter(s_name='李元霸')
grade = stu.grade
# 2.通过班级找学生
grade = Grade.object.get(g_name='python1班')
# 拿到班级的学生信息；与一对一比较，后面加上'_set'就行了
grade.student_set
# 就可以对该班级的信息进行操作了，例如，查询该班级的学生的信息
grade.student_set.filter(s_gender=0).all()
```
