## 练习MySQL查询语句
>实例一：学生选课表
```
-- 创建SRS数据库
drop database if exists SRS;
create database SRS default charset utf8 collate utf8_bin;

-- 切换到SRS数据库
use SRS;

-- 创建学院表
create table tb_college
(
collid int not null auto_increment comment '学院编号',
collname varchar(50) not null comment '学院名称',
collmaster varchar(20) not null comment '院长姓名',
collweb varchar(511) default '' comment '学院网站',
primary key (collid)
);

-- 添加唯一约束
alter table tb_college add constraint uni_college_collname unique (collname);

-- 创建学生表
create table tb_student
(
stuid int not null comment '学号',
sname varchar(20) not null comment '学生姓名',
gender bit default 1 comment '性别',
birth date not null comment '出生日期',
addr varchar(255) default '' comment '籍贯',
collid int not null comment '所属学院编号',
primary key (stuid)
);

-- 添加外键约束
alter table tb_student add constraint fk_student_collid foreign key (collid) references tb_college (collid);

-- 创建教师表
create table tb_teacher
(
teaid int not null comment '教师工号',
tname varchar(20) not null comment '教师姓名',
title varchar(10) default '' comment '职称',
collid int not null comment '所属学院编号'
);

-- 添加主键约束
alter table tb_teacher add constraint pk_teacher primary key (teaid);

-- 添加外键约束
alter table tb_teacher add constraint fk_teacher_collid foreign key (collid) references tb_college (collid);

-- 创建课程表
create table tb_course
(
couid int not null comment '课程编号',
cname varchar(50) not null comment '课程名称',
credit tinyint not null comment '学分',
teaid int not null comment '教师工号',
primary key (couid)
);

-- 添加外键约束
alter table tb_course add constraint fk_course_tid foreign key (teaid) references tb_teacher (teaid);

-- 创建学生选课表
create table tb_score
(
scid int not null auto_increment comment '选课编号',
sid int not null comment '学号',
cid int not null comment '课程编号',
seldate date comment '选课时间日期',
mark decimal(4,1) comment '考试成绩',
primary key (scid)
);

-- 添加外键约束
alter table tb_score add constraint fk_score_sid foreign key (sid) references tb_student (stuid);
alter table tb_score add constraint fk_score_cid foreign key (cid) references tb_course (couid);
-- 添加唯一约束
alter table tb_score add constraint uni_score_sid_cid unique (sid, cid);


-- 插入学院数据
insert into tb_college (collname, collmaster, collweb) values 
('计算机学院', '左冷禅', 'http://www.abc.com'),
('外国语学院', '岳不群', 'http://www.xyz.com'),
('经济管理学院', '风清扬', 'http://www.foo.com');

-- 插入学生数据
insert into tb_student (stuid, sname, gender, birth, addr, collid) values
(1001, '杨逍', 1, '1990-3-4', '四川成都', 1),
(1002, '任我行', 1, '1992-2-2', '湖南长沙', 1),
(1033, '王语嫣', 0, '1989-12-3', '四川成都', 1),
(1572, '岳不群', 1, '1993-7-19', '陕西咸阳', 1),
(1378, '纪嫣然', 0, '1995-8-12', '四川绵阳', 1),
(1954, '林平之', 1, '1994-9-20', '福建莆田', 1),
(2035, '东方不败', 1, '1988-6-30', null, 2),
(3011, '林震南', 1, '1985-12-12', '福建莆田', 3),
(3755, '项少龙', 1, '1993-1-25', null, 3),
(3923, '杨不悔', 0, '1985-4-17', '四川成都', 3);

-- 插入老师数据
insert into tb_teacher (teaid, tname, title, collid) values 
(1122, '张三丰', '教授', 1),
(1133, '宋远桥', '副教授', 1),
(1144, '杨逍', '副教授', 1),
(2255, '范遥', '副教授', 2),
(3366, '韦一笑', '讲师', 3);

-- 插入课程数据
insert into tb_course (couid, cname, credit, teaid) values 
(1111, 'Python程序设计', 3, 1122),
(2222, 'Web前端开发', 2, 1122),
(3333, '操作系统', 4, 1122),
(4444, '计算机网络', 2, 1133),
(5555, '编译原理', 4, 1144),
(6666, '算法和数据结构', 3, 1144),
(7777, '经贸法语', 3, 2255),
(8888, '成本会计', 2, 3366),
(9999, '审计学', 3, 3366);

-- 插入选课数据
insert into tb_score (sid, cid, seldate, mark) values 
(1001, 1111, '2017-09-01', 95),
(1001, 2222, '2017-09-01', 87.5),
(1001, 3333, '2017-09-01', 100),
(1001, 4444, '2018-09-03', null),
(1001, 6666, '2017-09-02', 100),
(1002, 1111, '2017-09-03', 65),
(1002, 5555, '2017-09-01', 42),
(1033, 1111, '2017-09-03', 92.5),
(1033, 4444, '2017-09-01', 78),
(1033, 5555, '2017-09-01', 82.5),
(1572, 1111, '2017-09-02', 78),
(1378, 1111, '2017-09-05', 82),
(1378, 7777, '2017-09-02', 65.5),
(2035, 7777, '2018-09-03', 88),
(2035, 9999, date(now()), null),
(3755, 1111, date(now()), null),
(3755, 8888, date(now()), null),
(3755, 9999, '2017-09-01', 92);

-- 查询所有学生信息
select * from tb_student;
-- 查询所有课程名称及学分(投影和别名)
select cname as '课程名称',credit as '学分' from tb_course;
-- 查询所有女学生的姓名和出生日期(筛选)
select sname as '姓名',birth as '出生日期' from tb_student where gender=0;
-- 查询所有80后学生的姓名、性别和出生日期(筛选)
select sname as 姓名,gender as 性别,birth as 出生日期 from tb_student where birth between '1980-1-1' and '1989-12-31';
-- 查询姓”杨“的学生姓名和性别(模糊)
select sname as 姓名,gender as 性别 from tb_student where sname like '杨%';
-- 查询姓”杨“名字两个字的学生姓名和性别(模糊)
select sname as 姓名,gender as 性别 from tb_student where sname like '杨_';
-- 查询姓”杨“名字三个字的学生姓名和性别(模糊)
select sname as 姓名,gender as 性别 from tb_student where sname like '杨__';
-- 查询名字中有”不“字或“嫣”字的学生的姓名(模糊)
select sname as 姓名 from tb_student where sname like '%不%' or sname like '%嫣%';
-- 查询没有录入家庭住址的学生姓名(空值)
select sname as 姓名 from tb_student where addr is null or addr='';
-- 查询录入了家庭住址的学生姓名(空值)
select sname from tb_student where addr is not null and addr<>'';
-- 查询学生选课的所有日期(去重)
select distinct seldate from tb_score;
-- 查询学生的家庭住址(去重)
select distinct addr from tb_student where addr is not null and addr<>'';
-- 查询学生的姓名和生日按年龄从大到小排列(排序)
select sname,birth from tb_student order by birth asc;
-- max()/min()/sum()/avg()/count()
-- 查询年龄最大的学生的出生日期(聚合函数)
select min(birth) from tb_student; 
-- 查询年龄最小的学生的出生日期(聚合函数)
select max(birth) from tb_student; 
-- 查询男女学生的人数(分组和聚合函数)
select if (gender, '男', '女') as 性别,count(gender) as 人数 from tb_student group by gender;
-- 查询课程编号为1111的课程的平均成绩(筛选和聚合函数)
select avg(mark) from tb_score where cid=1111;
-- 查询学号为1001的学生所有课程的总成绩(筛选和聚合函数)
select sum(mark) from tb_score where sid=1001;
-- 查询每个学生的学号和平均成绩(分组和聚合函数)
select sid,avg(mark) from tb_score group by sid;
-- 查询平均成绩大于等于90分的学生的学号和平均成绩
-- 分组之前用where筛选，分组之后用having筛选；
select sid,avg(mark) from tb_score group by sid having avg(mark)>=90; 
-- 查询年龄最大的学生的姓名(子查询 + 运算)
-- 子查询-在一个查询中又使用到了另外一个查询的结果；
select sname from tb_student where birth=(select min(birth) from tb_student);
select sname as 姓名,year(now()) - year(birth) as 年龄 from tb_student where birth=(select min(birth) from tb_student);
-- 查询选了两门以上的课程的学生姓名(子查询/分组条件/集合运算)
select sname from tb_student where stuid in (
select sid from tb_score group by sid having count(cid)>2);
-- 查询选课学生的姓名和平均成绩(子查询和连接查询)
select sname,avgmark from tb_student t1,
(select sid,avg(mark) as avgmark from tb_score group by sid) t2 
where stuid=sid;
-- 查询学生姓名、所选课程名称和成绩(连接查询)
-- 注意：在连接查询时如果没有给出连接条件就会形成笛卡尔积；
select sname,cname,mark 
from tb_score,tb_student,tb_course 
where stuid=sid and couid=cid and mark is not null;

-- 第二种内连接
select sname,cname,mark from tb_student 
inner join tb_score on stuid=sid
inner join tb_course on couid=cid where mark is not null;
-- 查询每个学生的姓名和选课数量(左外连接和子查询)
select sname,num from tb_student t2,
(select sid,count(cid) as num from tb_score group by sid) t1
where t2.stuid=t1.sid;

select sname,num from tb_student t2
left join (select sid,count(cid) as num from tb_score group by sid) t1
on stuid=sid;

-- 左外连接 left join 或者在where下在连接条件加上(+) Mysql不支持； ---把左表（写在前面的表）不满足连接条件的记录也查出来对应记录补上null;
-- 右外链接 right join ---把右边表（写在后面的表）不满足连接条件的记录也查出来对应记录补上null;


-- DDL
-- DML
-- DCL --- grant /remoke

create user 'hellokitty'@'%' identified by '123123';
-- 创建用户，密码为123123，@后面跟ip,表示只能从改地址登录，hellokitty可以从任意位置连上来
 
 
-- 授权 grant .. to ..
-- 给helloKitty授予查看srs所有数据的权限；
grant select on srs.* to 'hellokitty'@'%';

-- 
grant insert,delete,update on srs.* to 'hellokitty'@'%';

--
grant create,drop,alter on srs.* to 'hellokitty'@'%';

-- 将对srs数据库的所有操作权限授予hellokitty；
grant all privileges on srs.* to 'hellokitty'@'%';

-- 将对srs数据库的所有操作权限授予hellokitty,并且hellokitty可以将该权限授予其他用户；
grant all privileges on srs.* to 'hellokitty'@'%' with grant option;


-- 召回权限revoke .. from ..
revoke all privileges on srs.* from 'hellokitty'@'%';


-- 事务控制:要么多个操作全做，要么都不做；要么都成功，要么都失败；例如，转账；
-- 开启事务环境
begin
-- start transaction -- 开启事务，二选一都可以；
update tb_score set mark=mark-2 where sid=1001 and mark is not null;
update tb_score set mark=mark+2 where sid=1002 and mark is not null;
commit;-- 提交，成功了就提交；
rollback; -- 事务回滚，
```
>实例2：员工系统
```
-- 创建人力资源管理系统数据库
drop database if exists HRS;
create database HRS default charset utf8 collate utf8_bin;

-- 切换数据库上下文环境
use HRS;

-- 删除表
drop table if exists TbEmp;
drop table if exists TbDept;

-- 创建部门表
create table TbDept
(
dno tinyint not null comment '部门编号',
dname varchar(10) not null comment '部门名称',
dloc varchar(20) not null comment '部门所在地',
primary key (dno)
);

-- 添加部门记录
insert into TbDept values (10, '会计部', '北京');
insert into TbDept values (20, '研发部', '成都');
insert into TbDept values (30, '销售部', '重庆');
insert into TbDept values (40, '运维部', '深圳');

-- 创建员工表
create table TbEmp
(
eno int not null comment '员工编号',
ename varchar(20) not null comment '员工姓名',
job varchar(20) not null comment '员工职位',
mgr int comment '主管编号',
sal int not null comment '月薪',
comm int comment '月补贴',
dno tinyint comment '所在部门编号',
primary key (eno)
);

-- 添加外键约束
alter table TbEmp add constraint fk_dno foreign key (dno) references TbDept(dno) on delete set null on update cascade;-- 如果把部门删了，就把部门编号设为空值；如果改了部门编号，也跟着改；但是默认的最好，不让删，也不让改；

-- 添加员工记录
insert into TbEmp values (7800, '张三丰', '总裁', null, 9000, 1200, 20);
insert into TbEmp values (2056, '乔峰', '分析师', 7800, 5000, 1500, 20);
insert into TbEmp values (3088, '李莫愁', '设计师', 2056, 3500, 800, 20);
insert into TbEmp values (3211, '张无忌', '程序员', 2056, 3200, null, 20);
insert into TbEmp values (3233, '丘处机', '程序员', 2056, 3400, null, 20);
insert into TbEmp values (3251, '张翠山', '程序员', 2056, 4000, null, 20);
insert into TbEmp values (5566, '宋远桥', '会计师', 7800, 4000, 1000, 10);
insert into TbEmp values (5234, '郭靖', '出纳', 5566, 2000, null, 10);
insert into TbEmp values (3344, '黄蓉', '销售主管', 7800, 3000, 800, 30);
insert into TbEmp values (1359, '胡一刀', '销售员', 3344, 1800, 200, 30);
insert into TbEmp values (4466, '苗人凤', '销售员', 3344, 2500, null, 30);
insert into TbEmp values (3244, '欧阳锋', '程序员', 3088, 3200, null, 20);
insert into TbEmp values (3577, '杨过', '会计', 5566, 2200, null, 10);
insert into TbEmp values (3588, '朱九真', '会计', 5566, 2500, null, 10);

-- 查询薪资最高的员工姓名和工资
select ename,sal from tbemp where sal=
(select max(sal) from tbemp);

-- 查询员工的姓名和年薪((月薪+补贴)*12)
-- 也可以使用MySQL的ifnull(comm,0)
select ename as 姓名,((sal + if(comm, comm, 0))* 12) as 年薪 from tbemp
where (sal + if(comm, comm, 0))* 12>50000;

-- 查询有员工的部门的编号和人数
select dno as 部门编号,count(dno) as 人数 from tbemp group by dno;

-- 查询所有部门的名称和人数
select dname as 部门名称,ifnull(num,0) as 人数 from tbdept t1
left join(select dno,count(dno) as num from tbemp group by dno) t2 
on t1.dno=t2.dno;

-- 查询薪资最高的员工(Boss除外)的姓名和工资
select ename,sal from tbemp where sal=(select max(sal) from tbemp where mgr is not null);

-- 查询薪水超过平均薪水的员工的姓名和工资
select ename,sal from tbemp where sal>
(select avg(sal) from tbemp);

-- 查询薪水超过其所在部门平均薪水的员工的姓名、部门编号和工资
select ename,t2.dno,sal,salary from tbemp t2,
(select dno,avg(sal) as salary from tbemp group by dno) t1
where t2.dno=t1.dno and t2.sal>t1.salary;

-- 查询薪水超过其所在部门平均薪水的员工的姓名、部门名称和工资
select ename,dname,sal,salary from tbemp t2,tbdept,
(select dno,avg(sal) as salary from tbemp group by dno) t1
where t2.dno=t1.dno and t2.sal>t1.salary and t2.dno=tbdept.dno;

-- 查询部门中薪水最高的人姓名、工资和所在部门名称
select ename,sal,dname from tbemp,tbdept,(select dno as dno2,max(sal) as salary from tbemp group by dno) t1 
where tbemp.sal=t1.salary and t1.dno2=tbdept.dno and t1.dno2=tbemp.dno;

-- 查询主管的姓名和职位
select ename,dname from tbemp,tbdept,
(select mgr as mgr2,dno as dno2 from tbemp group by mgr) t1
where tbemp.eno=mgr2 and tbdept.dno=tbemp.dno and t1.dno2=tbemp.dno;

select ename,job from tbemp
where eno in (select distinct mgr from tbemp where mgr is not null);
-- 说明：去重操作和集合运算in效率很低；
-- 通常建议用exists或not exists 来替代去重操作和集合运算；

select ename,job from tbemp t1
where exists (select 'x' from tbemp t2 where t1.eno=t2.mgr);




-- 视图（查询的快照） ---限制用户只能看见部分列内容，就是给用户授权只能查看该视图；
-- 通过视图可以将用户对表的访问权限进一步加以限制
-- 也就是说将来普通用户不能够直接查询表的数据
-- 只能通过指定视图去查看
-- 创建视图
create view xw_emp_no_sal as
select eno,ename,job,mgr,dno from tbemp;


select * from xw_emp_no_sal;





-- 索引（相当于一本书的目录）
-- 为表创建索引可以加速查询（用额外的空间换时间），增删改会变慢
-- 索引虽然好但不能滥用，一方面会占用额外的存储空间，另外增删改会变慢；
-- 因为增删改操作可能会导致更新索引；
-- 如果哪个列经常被用于查询的筛选条件，那么就应该在这个列上建立索引；
-- 默认主键都有索引（唯一索引）；


-- 创建索引
-- 说明：如果使用模糊查询，如果查询条件不以‘%’开头，那么有效；
-- 如果模糊查询的条件以‘%’开头，那么索引失效；
create index idx_emp_ename on tbemp(ename);
-- 建立唯一索引
create unique index uni_emp_ename on tbemp(ename);
-- 删除索引
alter table tbemp drop index idx_emp_ename;

```
## 在python中连接MySQL数据库
>在python中装第3方库；
- 方式一：file-setting-project-点击‘+’；
- 方式二：不用管，直接```import pymysql```，如果报错，直接在报错的地方install...；
- 方式三：点击```Terminal```，输入```pip install pymysql```;或者
```pip install -i https://pypi.doubanio.com/simple pymysql```;

> 更改下载第三方库时，从国内镜像下载;
- 在用户主目录，新建一名为‘pip’的文件夹，在pip文件夹中创建一个‘pip.ini’文件，在其中输入‘[global]
index-url=https://pypi.doubanio.com/simple’；这样，就可以一劳永逸了，以后下载第三方库时，都是从豆瓣的国内镜像下载的；速度很快；
>在python连接mysql数据库并操作数据实例：
```
import pymysql


def main():
    no = int(input('部门编号: '))
    name = input('部门名称: ')
    location = input('部门所在地: ')
    # 1. 创建数据库连接
    conn = pymysql.connect(host='localhost', port=3306,
                           user='root', password='123456',
                           db='hrs', charset='utf8',
                           autocommit=True)
    try:
        # 2. 获得游标对象
        with conn.cursor() as cursor:
            # 3. 向数据库服务器发出SQL
            result = cursor.execute(
                query='insert into TbDept values (%s,%s,%s)',
                args=(no, name, location))
            if result == 1:
                print('新增成功!')
    finally:
        # 4. 关闭连接释放资源
        conn.close()


if __name__ == '__main__':
    main()

```
>实例2：
```
import pymysql


def main():
    no = int(input('部门编号: '))
    name = input('部门名称: ')
    location = input('部门所在地: ')
    # 1. 创建数据库连接
    conn = pymysql.connect(host='localhost', port=3306,
                           user='root', password='123456',
                           db='hrs', charset='utf8',
                           autocommit=True)
    try:
        # 2. 获得游标对象
        with conn.cursor() as cursor:
            # 3. 向数据库服务器发出SQL
            result = cursor.execute(
                query='update TbDept set dname=%(name)s, dloc=%(loc)s where dno=%(no)s',
                args={'no': no, 'name': name, 'loc': location})
            if result == 1:
                print('更新成功!')
    finally:
        # 4. 关闭连接释放资源
        conn.close()


if __name__ == '__main__':
    main()
```
>实例3：
```
import pymysql


class Dept(object):

    def __init__(self, no, name, location):
        self.no = no
        self.name = name
        self.location = location


def main():
    # 1. 创建数据库连接
    conn = pymysql.connect(host='localhost', port=3306,
                           user='root', password='123456',
                           db='hrs', charset='utf8',
                           autocommit=True,
                           cursorclass=pymysql.cursors.DictCursor)
    try:
        # 2. 获得游标对象
        with conn.cursor() as cursor:
            # 3. 向数据库服务器发出SQL
            cursor.execute(
                '''
                select dno as no, dname as name, dloc as location
                from TbDept
                ''')
            # print(cursor.fetchone())
            # print(cursor.fetchmany(2))
            print('编号\t名称\t\t所在地')
            print('-' * 20)
            for row in cursor.fetchall():
                dept = Dept(**row)
                print(dept.no, end='\t')
                print(dept.name, end='\t')
                print(dept.location)

    finally:
        # 4. 关闭连接释放资源
        conn.close()


if __name__ == '__main__':
    main()

```