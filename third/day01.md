## MVC
## MVT

## 创建虚拟环境步骤：
1. ``` --no-site-packages```；没有全局的库，所以虚拟环境是干净的；
```-p C:\users\admini\python.exe djenv```；有两个以上的python版本的话，指定python版本；

2. pip list
   pip freeze pip装了哪些库；
3. cd djenv
4. cd Scripts
5. activate ：进入env
6. pip install django==1.11 ：安装Django
7. deactivate :退出env