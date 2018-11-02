from django.db import models


# 创建栏目表
class Category(models.Model):
    name = models.CharField(max_length=20)
    describe = models.TextField(null=True)
    create_time = models.DateTimeField(auto_now_add=True)
    is_delete = models.BooleanField(default=0)

    class Meta:
        db_table = 'category'


# 创建文章表
class Article(models.Model):
    title = models.CharField(max_length=20)
    content = models.TextField(null=True)
    describe = models.CharField(max_length=150)
    # 上传到article文件夹里
    img = models.ImageField(upload_to='article')
    create_time = models.DateTimeField(auto_now=True)
    is_delete = models.BooleanField(default=0)
    category = models.ForeignKey(Category, null=True)

    class Meta:
        db_table = 'article'



