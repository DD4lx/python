## Linux远程连接
- PING to death
- DoS - Deny of Service
- DDoS - Distributed Deny of Service (分布式拒绝服务)
- eth0:以太网.私有ip
- ssh root@公网ip 可以连上另一个服务器；远程连接；
- scp 安全拷贝，从网络拷贝，远程文件拷贝
- scp -r 加-r 递归拷贝；
- ```scp -r code2 root@59.110.227.152:/root/code2``` ;远程拷贝；
- sftp root@ip;远程上传下载文件
- get <文件名> 下载
- put <文件名>  上传
- lls 看自己的目录信息 local ls
- lpwd 本地操作
- lcd 切换到本地目录
- 带l的就是本地操作，不带l的就是远端操作；
- bye/exit ：退出；
## 计算机网络分层架构模型
- Internet --- TCP/IP协议族
- IP --- Internet Protocol -网际协议
- TCP --- Transfer Control Protocol - 传输控制协议
- UDP --- User Datagram Protocol - 用户数据报协议

## TCP/IP模型：

- 应用层（定义应用之间如何传输数据；定义应用级协议） 
    - HTTP/SMTP/POP3/FTP/SSH/
    - ICQ/QQ/
- 传输层（端到端传输数据） - TCP/UDP
- 网际层/网络层 --- 寻址和路由 --- IP/ICMP 
- 物理链路层（数据分帧+校验） - 冗余校验码

## 补充一些Linux命令：
- netstat -na :查看所有ip网络状态；
- netstat -na | grep 80 : 查看80端口是否被占用
- netstat -nap | grep 80:查看80端口被哪个进程占用了
- kill -9 ：强杀；
- daemon：守护进程；系统关机，未执行完毕的进程也会关闭；
- systemctl start <service>：开启服务
- systemctl stop nginx：停止服务
- systemctl restart nginx:重启
- systemctl status nginx:查看服务状态
###### 注意：CentOS 6.x没有以上命令，只能用以下两条命令：
- service nginx stop
- service <name> start
- 设置服务开机自启：
- systemctl enable <name> - 开机自启
- systemctl disable <name> - 禁用开机自启；
- 安装apache服务器
- yum -y install httpd
- systemctl start httpd
开启服务


## 自己配防火墙：
- 自己关闭安全组规则：添加1/65535的安全组规则
- Linux常用的防火墙服务有firewall和iptables:
- systemctl start firewalld
- ps -ef | grep firewalld 查看是否打开了防火墙；
- 配置防火墙；（开启80端口）
- firewall-cmd
- firewall-cmd --add-port=443/tcp
- firewall-cmd --remove-port=443/tcp;删除端口；
- firewall-cmd --permanent --add-port=80/tcp ：永久有效；
- systemctl restart firewalld: 重启防火墙；
- firewall-cmd --query-port=443/tcp ：查看端口是否打开
- firewall-cmd --query-service=http:
- 打开任务管理器：按cpu占用率排列进程；
- top
- 将正在运行的程序暂停并放在后台； Ctrl+ z；
- 如果需要把运行中的进程终止掉： Ctrl + c
- 查看后台进程：                jobs
- ./func.py & :                直接让进程在后台运行
- 如果执行命令时在命令后面加上&，就可以让命令在后台运行；
- bg %<jobs中的编号>  让暂停的进程继续在后台运行；
- fg %<编号>---------- 让后台的进程在前台运行；

## 根目录下的文件夹：
- boot -- 系统启动
- dev -- 设备，每一个设备对应一个文件夹
- etc -- （！！重要）配置文件，装的软件的配置文件
    --  例如，改变Nginx默认的端口号，进入/etc/nginx/nginx.conf,改变        两个listen;保存退出
- home -- 非超级管理员用户目录
- lost+found -- 在服务器意外崩溃时，会将数据保存在改目录
- media -- 挂载媒体资源
- mnt -- 挂载文件 monut 路径  ； umount 反挂载
- opt -- 安装额外的软件
- proc -- 进程信息，内存，cpu
- run -- 程序运行产生的临时文件
- usr/bin -- 用户安装的软件的可执行程序
- usr/local -- 安装的软件
- 硬件 --- Linux Kernel --- shell

## 在shell中执行代码：
```
a=5
b=10
echo $a+$b ---> 5+10
echo $[a+b] ----> 15
```

## 一次性执行多个命令
```
ls;cal;wall 'hello'
ls && cal && wall 'hello'
ls || cal || wall 'hello' --- 第一个没有成功就干第2个
```



## 编写/root/.bash_profile 登录shell设置，环境配置文件
编写/etc/profile文件，在PATH前面，写代码，在登录成功之前执行代码；换个用户登录也是可以看见的;每个用户进来都会执行profile文件；
username=`whoami`---在``号内写Linux命令
