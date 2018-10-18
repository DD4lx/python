## Linux系统安装软件的两种方式：
>使用包管理工具进行安装yum/rpm
- - yum search <name> ---搜索
- - yum -y install <name> <name2> ---安装（安装一个或多个软件）
- - yum -y remove <name>... ---卸载
- - yum info <name> ---查看信息
- - yum update <name> ---更新
- - yum list installed ---列出已经安装的软件
- - yum list installed | grep nginx ---快速找到你要找的软件
>源代码构建安装（安装最新的版本）
- - gcc(自带的) ---make；
- - 以安装redis为例：
- - wget 下载
- - 解压缩gunzip/xz -d
- - 解归档tar -xvf
- - 进入文件目录，然后查看如果makefile了，直接make就可以了；
- - make && make install 构建安装；
- - redis-server --version 检查安装好没；
- - /usr/local/bin目录下已经有了；
- - 编辑.bash_profile文件；配置环境变量；
>安装Nginx：http协议的反向代理服务和web服务器；将阿里云服务器变成web服务器；
1. yum -y install nginx
2. 启动Nginx服务器：systemctl start nginx
>ip地址找到网络上的一台主机，而端口号可以用来区分不同的服务；
HTTP - 80;
HTTPS - 443;
-1 - 可以使用ping;
22 - 可以使用远程连接Xshell;
3389- 监控;

>这时修改index.html首页，就能看见效果了；
- ```cd /usr/share/nginx/html```
- ```vim index.html```
- ```set autoindent```,可以设置在编辑模式是产生自动缩进的效果；
>将自己的项目克隆到服务器上的方法：

1. ```git clone http://gitee.com/jackfrued/Python1806```
2. 将本地的项目上传（这里可以使用Xftp工具）

>再次总结vim编辑器的一些知识：

- 命令模式 ---> 编辑模式 i a
- 编辑模式 ---> 命令模式 ESC
- 命令模式 ---> 末行模式 : / ?
>命令模式下：

键盘按键：
- 移动光标：
- - hjkl/HML/0行首$行尾/w移动一个单词/gg/G/100G
- 翻页： 
- - Ctrl+e / Ctrl+y/Ctrl+f/Ctrl+b
- 复制粘贴删除：
- - yy(复制一行)/p黏贴/dd删除/u撤销/Ctrl+r恢复/ 
- 代码提示：
- - Ctrl+x Ctrl+o -在敲代码时会有部分提示
>末行模式下：
- :w
- :q
- :wq
- :set nu - set配置编辑器
- :set ts=4
- :set autoindent
- /正则表达式 - 正向搜索
- n - 正向一个个搜索
- N - 反向一个个搜索
- ?正则表达式 - 反向搜索
- :1,100s/正则表达式1/正则表达式2 - 将1到100行的正则表达式1替换成表达式2
- :1,$s/新闻/牛粪/g(全局) i(忽略大小写) c(每次替换，要确认) e(允许出错，继续)
- ```vim -d sohu.html sohu2.html``` -- 进行比较
- ```vim sohu.html test.py``` -- 打开两个文件
如果vim打开了多个文件可以在末行模式输入
- :ls - 查看打开的文件
- :b <编号> 切换窗口
- :vs - 垂直拆分窗口；
- Ctrl+w - 在窗口之间切换光标；
- :sp - 水平拆分窗口；
- :qa - 退出全部；
- :map <F2> gg10000dd - 映射命令模式的快捷键F2删除10000行；
- :imap - 映射插入模式下的快捷键
- :inoremap - 不要递归的map;
- 如果想拿到命令行参数：
就用```import sys```
    和```sys.argv``` 可以拿到;
```f('{}')``` 相当于 ```('%s'%)```；
- 三元条件运算符：```y = year if 条件1 else 条件2```；