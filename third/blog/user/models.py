from django.db import models


class User(models.Model):
    username = models.CharField(max_length=20, unique=True, verbose_name='用户名')
    password = models.CharField(max_length=16, verbose_name='密码')
    create_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'user'


class UserToken(models.Model):
    token = models.CharField(max_length=25, verbose_name='浏览器标识符')
    user = models.OneToOneField(User)

    class Meta:
        db_table = 'usertoken'
