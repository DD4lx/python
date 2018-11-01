## 权限

>RBAC基于角色的访问控制,
只要定义了模型，Django会自动创建对应的增、改、删权限；

>继承Django自带的user模型进而拓展user模型
```
from django.contrib.auth.models import AbstractUser
from django.db import models


class MyUser(AbstractUser):
    # 拓展Django自带的auth_user表，可以自定义新增的字段

    class Meta:
        # Django默认给每个模型初始化三个权限
        # 默认的是change，delete，add权限
        permissions = (
            # 新增权限名称，权限描述
            ('add_my_user', '新增用户权限'),
            ('change_my_user_username', '修改用户名权限'),
            ('change_my_user_password', '修改用户密码权限'),
            ('all_my_user', '查看用户权限')
        )
```
>在settings.py中，添加AUTH_USER_MODEL字段的配置：

AUTH_USER_MODEL = 'user.MyUser'告诉DjangoUser模型修改为自定义的User模型；


>创建用户，并赋予其相应的权限：

```
from django.contrib.auth.models import Permission
from django.http import HttpResponse
from django.shortcuts import render

from user.models import MyUser


def add_user_permission(request):
    if request.method == 'GET':
        # 1.创建用户
        MyUser.objects.create_user(username='小李',
                                   password='123456'
                                   )
        # 2.指定刚创建的用户，并分配给他权限（新增用户、查看用户权限）
        user = MyUser.objects.filter(username='小李').first()
        permissions = Permission.objects.filter(codename__in=['add_my_user',
                                                              'all_my_user']).all()
        for permission in permissions:
            # 多对对的添加
            user.user_permissions.add()
        # 3.删除刚创建的用户的新增用户权限
        user.user_permissions.remove('add_my_user')

        return HttpResponse('创建用户权限成功')
```
**补充：user.groups.all.0获取用户所在的组的第一个组**



>Django自带的一些方法：

- Csrf校验，{% csrf_token %},防止被第三方劫持；
```
<form action="" method="post">
    {% csrf_token %}
    <input type="text" name="username" placeholder="Username">
    <input type="password" placeholder="Password" name="pwd">
    <input type="submit" value="登录">
</form>
```

- user.get_group_permissions()获取组的权限
- user.get_all_group_permissions()获取所有权限


## 权限总结
- 表：用户表、权限表、角色表
- 思想：
	- 1.创建角色
	- 2.角色对应权限
	- 3.用户分配角色
	- 4.（特殊情况）用户分配权限
- 用户表和权限表的ManyToManyFiled()为：user_permissions
- 用户表和组表的ManyToManyFiled()为：groups
- 组表和权限表的ManyToManyFiled()为：permissions

添加和删除：add()、remove()


>查询
1. 通过用户查询权限
```
#自己实现查询用户对应的权限方法：
user.user_permission.all()
user.groups.all().0.permissions.all()
# Django自带查询
user.get_group_permissions()
user.get_all_permission()
```
2. 权限验证
```
# 自己实现权限验证
user.user_permission.filter(codename='xx')
user.groups.all().0.permissions.filter(codename='xx')


# Django实现权限验证
user.has_perm('app名称.权限名')
```

3. 装饰器
```
# 自己实现
def a(func):
    def b(request):
        return func(request)
    return b
# Django实现
permission_required('名称.权限名')
```


**补充：验证不通过，就跳转该地址：**
LOGIN_URL = '/user/login/'















