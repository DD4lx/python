## 在windows安装MySQL：

通过MySQL Installer 安装；
- 点击选择“NO”进入安装界面，选择“Custom”自定义安装；
- 展开MySQL Server 选择相应的服务器，进入右边，默认选，下一步；
- 如果提示缺文件，就先安装，直到出现“ready。。”，点击“Execute”；
- 下一步，进行配置，进入“Type and Networking”,选择第一项；点下一步
- 默认配置，点下一步；端口是ip地址的扩展；
- 在运行里输入services.msc，进入window的服务窗口；
- 设置超级管理员；点下一步
- 默认选项，点下一步；
- 点执行；
configure - 配置



## 在Linux安装MySQL：
- Docker - 构造一个虚拟的环境，屏蔽硬件和软件的差异；
- yum -y docker-io:下载docker；
- docker pull mysql:5.7； 联网下载MySQL；
- docker run -d -p 3306:3306 - name mysql57 -e MYSQL_ROOT_PASSWORD=123456 mysql:5.7




## 安装Navicat for mysql：（MySQL图形化客户端工具）
连接mysql：
- 主机：写127.0.0.1（回环地址） - localhost - ip 都可以




## 启动MySQL服务：
- net start mysql；
打开MySQL client；
命令、语句：
- show databases; -->显示已有的数据库；分号不能少；
- use mysql; --> 进入名为mysql数据库；
- show tables; -->显示数据库中的表；



## 数据库 - database - 数据的仓库（集散地）
>通过数据库可以实现数据的持久化；
当我们做数据持久化操作是不仅仅是希望能够把数据长久的保存起来；更为重要的是我们希望很方便的管理数据，在需要数据的时候能够很方便的把需要的数据取出来；
- 在1970s - IBM发表论文 - 奠定了关系型数据库的基础
- 理论基础：关系代数和集合论
- 具体表象：用二维表来组织数据
例如，一个学生表，
行：记录（1001 小李 1980年1月 男 四川成都） - 实体
列：字段（学号、姓名、出生日期、性别、家庭住址） - 实体的属性
- 数据库的编程语言 - SQL（结构化查询语言）
- DDL（数据定义语言）：create/drop(删除)/alter(修改)
- DML（数据操作语言）：insert/delete/update/select
- DCL（数据控制语言）：grant(授权)/revoke(召回权限)


- 关系型数据库产品：
- Oracle - Oracle公司 - Oracle 12c支持云计算
- MySQL - Oracle公司 - MySQL8.x/5.7.x
- SQLServer
- PostgreSQL 
- DB2



- 非关系型数据库作为关系型数据库的补充；
- MongoDB非关系型数据库 
- Redis非关系型数据库
- ElasticSearch其实是搜索引擎；
## MySQL数据库中的具体操作：
>以具体的实例为例：
```
-- SQL(Structred Query Language)
-- DDL（数据定义语言）：create/drop(删除)/alter(修改)
-- DML（数据操作语言）：insert/delete/update/select
-- DCL（数据控制语言）：grant(授权)/revoke(召回权限)

-- 删除数据库
drop database if exists school;
-- 创建数据库
create database school default charset utf8;
-- 切换到school数据库
use school;


-- 删除表
drop table if exists tb_student;

-- 创建二维表保存数据
-- 列名 数据类型 约束条件
-- 非空约束 - not null
-- 默认值约束 - default
-- 主键约束 - 表中能够唯一标识一条记录的列 - primary key (一列或多个列) 
create table tb_student
(
stuid int not null,
name varchar(4) not null,
gender bit not null default 1,
birth date,
addr varchar(50),
primary key (stuid)
);



-- 修改表
alter table tb_student add column tel char(11) not null;
alter table tb_student drop column birth;
-- 给学生表添加一个学院id列；
alter table tb_student add column college_id int;
-- 添加外键，给学生表学院id列添加外键约束
alter table tb_student add constraint fk_student_collid foreign key (college_id) references tb_college(college_id);
-- 删除外键
alter table tb_student drop foreign key fk_student_collid;




-- 创建学生和课程的中间表（关系型数据库无法用两张表实现多对多关系）
create table tb_score
(
scid int not null auto_increment,
sid int not null,
cid int not null,
seldate datetime default now(),
-- decimal固定小数的位数,总共有4位数字，小数点后有1位
mark decimal(4,1),
primary key (scid)
);

alter table tb_score add constraint fk_score_id foreign key (sid) references tb_student (stuid);
alter table tb_score add constraint fk_score_courseid foreign key (cid) references tb_course (courseid);

alter table tb_score add constraint uni_score_sid_cid unique (sid, cid);

-- alter table tb_score add constraint uni_sid_cid unique ();
-- alter table tb_score drop index uni_sid_cid;









-- DML (Data Manipulation Language)
-- 插入数据
insert into tb_student values 
(1001, '小张', 1, '四川成都', '13478919495');

insert into tb_student values 
(1002, '小李', 1, '四川成都', '13478919495');

insert into tb_student(stuid, name, tel) values 
(1003, '小杨', '13478919495');

insert into tb_student (name, stuid, gender, addr, tel) values 
('小王', 1004, 0, '北京', '13601919495');

insert into tb_student (stuid, name, tel) values
(1005, '方既白', '13676534123'),
(1006, '慕容百', '13847634438'),
(1007, '司马懿', '13456081454');

-- 删除数据
delete from tb_student where stuid = 1006;
delete from tb_student where stuid in (1002, 1005,1007, 2000);
-- 要删除全表，不是用delete，而是用截断数据
truncate table tb_student;


-- 更新数据
update tb_student set addr = '四川绵阳', gender=0 where stuid in (1003, 2000);


-- 查询数据
select * from tb_student;
-- 投影：只查询部分列
select name,gender from tb_student;
-- 别名（alias - as）
select name as 姓名, gender as 性别 from tb_student;
-- if是mysql特有的，其他数据库语法不同；
select name as 姓名, if(gender, '男', '女') as 性别 from tb_student;
-- 通用的语法
select name as 姓名, case gender when 1 then '男' else '女' end as 性别 from tb_student;
select name as 姓名, case gender when 1 then '男' when 0 then '女' end as 性别 from tb_student;
-- 对列做运算
select concat(name, ':', tel) as 信息 from tb_student;
-- 筛选
select * from tb_student where stuid = 1001;
-- 查学号不等于1001的学生
select * from tb_student where stuid<>1001;
select stuid, name, gender from tb_student where stuid>1002;
select stuid, name, gender from tb_student where gender=1;
select * from tb_student where stuid between 1002 and 1007;
select * from tb_student where stuid>1003 and gender=0;
select * from tb_student where stuid>1003 or gender=0;
-- 注意：判断一个字段是否为null不能用=和<>，而是用is;
select * from tb_student where addr is null;
select * from tb_student where addr is not null;

-- 模糊查询（char / varchar）
-- %是一个通配符表示零个或任意多个字符
select * from tb_student where name like '小%';
select * from tb_student where name like '%白%';
-- _也是一个通配符它表示一个字符
select * from tb_student where name like '白_';
select * from tb_student where name like '白__';
-- regexp - regular expression 正则表达式：字符串模式匹配的工具
select * from tb_student where name regexp "[王白].{1,3}";


-- 排序
select * from tb_student order by stuid;
select * from tb_student order by stuid desc;
select * from tb_student order by name asc;
-- 多个排序关键字；
select * from tb_student order by gender asc, stuid desc;
-- 注意：一定要先筛选再排序；
select * from tb_student where gender=0 order by stuid desc;
-- limit 限定
select * from tb_student limit 3;
-- 跳过前3个，显示3条，offset偏移；
select * from tb_student limit 3 offset 3;
-- 一起构成分页效果；
select * from tb_student limit 3 offset 6;
-- 也可以这样写
select * from tb_student limit 0,5;
select * from tb_student limit 5,5;
select * from tb_student limit 10,5;
-- 先筛选，再排序，在分页；
select * from tb_student where gender=1 order by stuid desc limit 0,3;
select * from tb_student where gender=1 order by stuid desc limit 3,3;







```