create database jd_db default charset utf8mb4;

use jd_db;

create table jd(
id int auto_increment primary key,
sku varchar(32),
title varchar(512),
href varchar(1024),
img varchar(1024),
price varchar(32),
name varchar(1024),
commit_url varchar(1024),
commit varchar(1024),
shop_url varchar(1024),
shop_name varchar(512)

);