>版本控制器的发展：

CVS/VSS --- 锁定模式

2000年 - Subversion（SVN） --- 合并模式

集中控制式的版本控制系统 --- 必须有中央服务器的存在；

2005年 --- Git --- 版本控制（分布式的版本系统）

>命令：
- git init :初始化仓库（生成一个隐藏文件夹.git）
- dir /a:显示所有文件（包括隐藏文件）
- notepad hello.py：创建一个文件
- git add hello.py:添加文件到仓库暂存区
- git status：查看状态
- git commit -m "更新了。。。":提交
- git config --global user.name " ":设置全局用户名
- git config --global user.email "":设置全局邮箱
- git log:查看日志
- git add .:把所有的文件都加入到版本控制
- git reset：重置 git reset --hard 921658(代码)/HEAD^(上个版本);
- git reflog:获得删除之前的版本
>git仓库大致分为工作区---暂存区---仓库

步骤：
- git init ---将一个文件夹初始化成git仓库；
- git add file ---将文件添加到暂存区；
- git reset HEAD file ---将文件从暂存区移除；
- git checkout --file ---将暂存区的文件恢复到工作区；
- git status ---查看暂存区的状态；
- git config --global user.name "用户名"
- git config --global user.email "用户邮箱"
- git commit ---将暂存区的内容提交到本地仓库
- git log --- 查看日志
- git reflog ---查看所有版本
- git reset --hard id/HEAD^ ---回到上一个版本，--hard让工作区和版本完全一致
>代码托管平台 --- 用别人提供的Git服务器
github.com
gitee.com
coding.net
- git clone url - 克隆服务器上的项目（仓库）到本地；在本地实施版本控制；
- git push - 将代码推送到服务器(上传)（分享自己的成果）；
- git pull - 将服务器代码同步到本地（下载）（看到他人的更新）