create database douban_db default character set 'utf8mb4';

use douban_db;

create table douban(
    id int auto_increment primary key,
    title varchar(128),
    likes varchar(32),
    content text,
    groups varchar(128),
    time varchar(512),
    group_url varchar(1024),
    image_url varchar(1024)
);

create index ix_douban_title on douban(title);





