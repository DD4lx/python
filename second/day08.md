## Linux系统下一些常用命令：
- ps -processes:查看进程快照；
- kill <pid> :杀死进程；
- kill -9 <pid>:强制杀死进程；
- history ：查看历史命令；
- man ：查看手册；
- ll - ls -l 的alias(别名)；
- alias: 定义别名：例如，alias rmd = "rm -rf"；
- unalias:反别名；
- ls :列出文件夹内容；
- - -l :长格式查看
- - -a :查看所有（包括以点开头的文件和文件夹）
- - -R :递归查看；
- ls --help | more :"|"表示管道，前一个的输出作为后一个的输入；
- '>' :输出重定向
- '>>' :追加输出重定向
- '2>' :错误输出重定向
- '<' ：输入重定向
- grep - 搜索字符串；
- wc - word count - 统计行、单词、字节数量；
- uniq - unique - 去重（去掉文本内容中相邻且相同的行）；
- diff ：查看文件的不同；

## Linux系统安装软件的方式
### 1、使用包管理工具（yum/rpm）进行安装
>yum search :查找；

>yum install git :安装git；

>yum -y install git:不用回答问题直接安装git；

>yum remove git:卸载git；

>yum info git:查看git软件信息；

### 2、CentOS安装Python3.7步骤：
>首先，Linux压缩文件的命令：
- gz --- gzip压缩工具/gunzip解压工具
- xz --- xz -z 压缩/xz -d 解压；
>WinRAR - 归档和解归档命令：
- tar - 归档文件
- 归档 - 把多个文件合成一个文件
- 解归档 - 把一个文件拆成多个文件；
- tar -x;tar -xv :可以看见安装信息；tar -xvf(后面的文件名)；
- gcc - C语言编译器；
>下面，实现Linux安装最新软件，以Python3.7为例：
1. 下载Python源代码
- wget https://www.python.org/ftp/python/3.7.0/Python-3.7.0.tgz
2. 解压缩
- gunzip Python-3.7.0.tgz
3. 解归档
- tar -xvf Python-3.7.0.tar
4. 安装更新依赖库
- yum -y install zlib-devel bzip2-devel openssl-devel ncurses-devel sqlite-devel readline-devel tk-devel gdbm-devel db4-devel libpcap-devel xz-devel libffi-devel
5. 安装前的配置
- 进入Python-3.7.0目录，执行configure文件,prefix安装到指定usr/local目录下；
- cd Python-3.7.0
- ./configure --prefix=/usr/local/python37 --enable-optimizations
6. 构建安装
- make && make install (构建和安装)
7. 配置PATH环境变量
- export PATH=$PATH:/usr/local/python37/bin；
- ($PATH:读取原有的PATH路径，将后面的路径添加到PATH中）基本就可以使用Python了；
- 也可以vim .bash_profile 进入文件，进行编辑；
修改PATH：PATH=$PATH:/usr/local/python37/bin；
退出重新链接，就可以永久使用了；
8. 注册软链接（符号链接）--相当于Windows下的快捷方式：ln -s 路径 链接名字;（这一步骤是非必须的）
- ln -s /usr/local/python37/bin/python3 
- /usr/bin/python3：在usr目录下的bin目录下创建python3快捷方式；


>硬链接 - 文件的引用，只要引用数不为0，文件就会一直存在；
(ln 带完整路径的文件名 链接文件名)；

>软链接 - 相当于文件的快捷方式，如果文件被删除，就会失效；(ln -s 带完整路径的文件名 链接文件名)；
## vim文本编辑器
>命令：
- vim 文件名---初始是命令模式，按i进入insert模式，输入:,再输入set nu,可以显示行号；
- pip3 install pycodestyle;安装代码检查工具；
- pycodestyle hello.py;检查代码是否规范；
- pip3 install pylint;另外一个检查工具；
- pylint hello.py;检查代码；
- ./;运行可执行程序；
- 将python改成可执行程序:在py文件中加入"#!/usr/bin/python3";然后保存退出;赋予该文件执行权限：```chmod u+x hello.py```给同组的赋予权限:chmod g+x,o+x hello.py；
## vim中一般模式下的命令：
>1、寻找和替换：
- ```/word```:向光标之下寻找一个名称为word的字符串；
- ```?word```:向光标之上寻找一个字符串为word的字符串；
- ```:n1,n2s/word1/word2/g```:n1与n2为数字。在第n1与n2行之间寻找word1这个字符串，并将该字符串取代为word2;例如，```:100,200s/vbird/VBIRD/g```在 100 到 200 行之间搜寻 vbird 并取代为 VBIRD ;
- ```:1,$s/word1/word2/gc```从第一行到最后一行寻找 word1 字符串，并将该字符串取代为 word2;
- ```:1,$s/word1/word2/gc```从第一行到最后一行寻找 word1 字符串，并将该字符串取代为 word2 ！且在取代前显示提示字符给用户确认 (confirm) 是否需要取代;
>2、删除、复制和粘贴
- x,X ---在一行字当中，x 为向后删除一个字符 (相当于 [del] 按键)， X 为向前删除一个字符(相当于 [backspace] 亦即是退格键);
- dd ---删除游标所在的整行;
- p,P ---p 为将已复制的数据在光标下一行贴上，P 则为贴在游标上一行;
- J ---将光标所在行与下一行合并为一行；
- c ---重复删除多个数据；
- u ---撤销；
- . ---重复前一个动作；
>3、末行模式指令：
- :w -- 保存
- :w! -- 强制保存
- :q -- 离开vi
- :q! -- 强制离开
- :wq -- 存储后离开
- ZZ -- 若档案没有更动，则不储存离开，若档案已经被更动过，则储存后离开
- :w[filename] -- 将编辑的数据存储成另一个档案（类似另存）
- :r[filename] -- 在编辑的数据中，读入另一个档案的数据。将这个档案的数据内容加到游标后面；
- :n1,n2 w [filename] -- 将n1到n2的内容存储成filename这个档案；
- :! command -- 暂时离开 vi 到指令行模式下执行 command 的显示结果！例如『:! ls /home』即可在 vi 当中察看 /home 底下以 ls 输出的档案信息！
- :set nu 显示行号
- :set nonu 取消行号；


>常用的命令模式下命令:
- ctrl + e y f b;移行翻页；
- dd d$ d0 : 删除；

>vim .vimrc:设置配置文件；
- set nu 设置行号
- set ts=4 设置tab键为4个空格
- syntax on 显示高亮语法
- set ruler 显示光标位置
