## MVC
- M(模型层)：对象
- V(视图层)：页面
- C(业务层)：功能
## Django --- MVT
- M(模型层)
- V(视图)：处理业务逻辑
- T(模板)：HTML页面

## 创建虚拟环境步骤：
1. ```virtualenv --no-site-packages <name>```；没有全局的库，所以虚拟环境是干净的；
   ```virtualenv --no-site-packages -p C:\XXX\python.exe <name>```；有两个以上的python版本的话，指定python版本；

2. 检测pip装了哪些库

   pip list

   pip freeze
3. cd djenv
4. cd Scripts
5. activate ：进入env
6. pip install django==1.11 ：安装Django
7. deactivate :退出env
## 创建项目：
>在虚拟环境下，进入自己创建的项目文件夹，创建第一个web项目；
- django-admin startproject day01
- 在pycharm中打开该项目：
- manage.py:是一个管理集工具
- settings.py :项目配置信息文件
- - BASE_DIR:项目路径
- - DEBUG：开发的时候设置为True，项目上线的时候设置为False；
- - ALLOWED_HOSTS:允许访问的ip地址；
- - Templates:'Dirs'存放页面的路径；
- - DATABASES：与连接数据库有关的；默认是sqllite;
- urls.py：路由
- - 打开setting,projiect Interpreter(解释器),```show All```,点击'+',选择'Existing environment',将之前配置好的环境导入，导入完成后,切换到'Terminal',将之前配置好的环境导入，导入完成,如果出现虚拟环境命令，则说明导入虚拟环境成功；
- wsgi.py：项目部署相关；
## 启动项目
>在Terminal中，```python manage.py``` ;查看django命令；

>```python manage.py runserver```,进入127.0.0.1:8000就可以看见运行成功界面；

>更改settings.py里的language_code = 'zh-hans',页面就变成中文显示了

>```python manage.py runserver 0.0.0.0:8080```;
>还要设置settings.py里的```allowed_hosts = ['*']```,这样其他人就可以访问我的ip了；runserver后面只加ip的话，会报错，只加端口号的话，就只能本机访问相应的端口号；

>永久配置别人也能访问的做法，点击```add configuration```，进入配置界面；

## 设置数据库：（设置数据库相关信息）
1. 数据库类型改为mysql
2. 设置数据库名字
3. 设置用户名
4. 设置密码
5. 设置主机ip
6. 设置端口号
```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'dj',
        'USER': 'root',
        'PASSWORD': '123456',
        'HOST': '127.0.0.1',
        'PORT': 3306
    }
}
```
###### 注意：python3不能直接连接MySQL；
## 安装MySQL数据库驱动
- 需要装第三方库，```pip install pymysql```；
- 安装完成后，在```__init.py__```初始化文件里，导入mysql，接着导入数据库驱动；
```
import pymysql

pymysql.install_as_MySQLdb()
```
## 访问Django默认的管理后台：
- 迁移数据库中的表(将表映射到数据库中)：
  - ```python manage.py migrate```
    -数据库中就会有对应的表；
- 向表中插入超级用户从而可以登录：
  - ```python manage.py createsuperuser```
  - 然后再登录，就可以登录跳转页面了

## 补充：git使用时遇到的一个报错：
1. git过程中的bug

```RT ! [rejected] master -> master (fetch first)```:在push远程服务器的时候发现出现此错误；原因是没有同步远程的master,所以我们需要先同步一下```git pull origin master```;
2. git commit 过程中```Changes not staged for commit```:需要先git add 后在commit 然后 push

- 整个流程：
- ```$ git add menudd``` //其中 menudd 是一个目录 也可以是文件 会自动更新有修改的文件

- ```$ git commit -m "asdf"``` //“asdf”是更新注释

- ```$ git push origin master```
  ok完成 更新成功;
