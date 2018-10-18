## 使用阿里云服务器和Linux系统
>阿里云服务器公网ip：39.108.185.170
Windows下可以通过Xshell和Xftp来连接自己的阿里云服务器；mac可以使用命令或shellcraft；

Shell - 人机对话的交互式环境；

BASH - bourne again shell；

>命令：
- clear ---清屏；
- who ---可以看到有谁连接了我的服务器；
- w ---较为完整的信息；
- last ---最近登录过系统的；
- who am i ---只能看见自己的名字；
- whoami ---只能看到自己的名字；
- ps ---查看进程；process
- kill+PID：关闭进程；
- kill+ -9 +PID ：强制关闭进程；
- logout：退出连接；
- 命令行提示符：#：超级管理员；$:普通用户
- adduser + 用户名：添加用户；
- userpdel + 用户名：删除用户；
- passwd + 用户名：设置密码；
- su + 用户名：切换用户；switch user；
- sudo - super user do - 以超级管理员运行；
- history :查看历史命令；
- ! + 历史命令的id:就可以执行历史命令；
- history -c :清除历史命令；
- Ctrl + c:强行终止；
- whatis + 命令的名字：查看命令的描述；
- man + 命令的名字：查看命令的手册；
- ~ ：用户主目录；
- pwd：打印工作目录；
- cd：-change directory 改变所在目录；
- etc：系统配置文件夹；
- usr：程序文件夹；
- home：普通用户文件；
- root：超级用户文件；
- ls：显示目录中的文件；
- ls -l：详细显示；
- ls -a：包括隐藏目录；
- ls -laR:文件夹下面的文件；
- wget + URL :通过网络下载文件；
- cat + 文件：查看一个或多个文件；
- cat -n 文件：查看文件时会有行号；
- cat - concatenate - 连接多个文件并显示到标准输出上；
- mkdir ：make directory -创建文件夹
- rmdir ：remove directory - 删除空文件夹
- touch ：创建文件；
- cp ：copy-拷贝文件；
- rm ：rm - 删除文件；
- rm -f ：强制删除（没有提示）；
- rm -r ：递归删除；
- mv ：移动；
- mv sohu.html sohu2.html:重命名；
- touch ：创建一个空的文件；
- echo ：打印；
- > ：输出重定向；
- >> ：追加重定向；
- date：查看系统时间日期
- cal ：-calen 查看日历；
- head -n 文件：查看文件的头n行
- tail -n 文件：查看文件的最后n行；
- less/more 文件：翻页查看；


- mkdir abc/efg： 在abc文件夹中创建efg文件夹；
- mkdir -p hello/goodbye : 如果没有hello，就帮我创建；
- mkdir --help ：查看帮助（用户）；
- info mkdir： 查看手册（程序员）；
- shutdown：关机
- init 0：关机
- init 6：重启
- reboot：重启
- which/whereis：查看命令的位置；


