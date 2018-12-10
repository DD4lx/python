create database mogujie_db default charset utf8mb4;

use mogujie_db;

create table Tbmogujie(
id int auto_increment primary key,
tradeItemId varchar(32),
img varchar(1024),
itemType varchar(32),
clientUrl varchar(1024),
link varchar(1024),
itemMarks varchar(32),
acm varchar(1024),
title varchar(1024),
type varchar(32),
orgPrice varchar(32),
hasSimilarity varchar(32),
cfav varchar(32),
price varchar(32),
similarityUrl varchar(1024)
);


create table mogujie_product(
id int auto_increment primary key,
tradeitemid varchar(32),
img varchar(1024),
itemtype varchar(32),
clienturl varchar(1024),
link varchar(1024),
itemmarks varchar(1024),
acm varchar(1024),
title varchar(1024),
type varchar(32),
orgprice varchar(32),
hassimilarity varchar(32),
cfav varchar(32),
price varchar(32),
similarityurl varchar(1024)
);
