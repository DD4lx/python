## 非关系型数据库redis
>在Linux系统中使用redis
- redis-server --version:查看redis服务端是否安装
- redis-cli --version：查看redis客户端是否安装，
- redis主要用来作网站的高速缓存；
- 启动数据库服务器：
>修改redis配置文件
- 将配置文件拷贝一份到用户主目录：cp redis-4.0.11/redis.conf  ./redis.conf
- 进入vim编辑 到70行
```:ifconfig eth0``` 查看以太网私有ip
将bind改成自己绑定私有ip
- 92行 设置端口 默认是6379
- 搜索```/requirepass``` 在500行改命令 为123456
- ```/appendonly``` 在672行改变为yes；打开持久化操作aof
- ```？RDB``` 第二种持久化方式；在220行；默认是打开的
- 就可以启动服务器了：
- 后台启动服务器：```redis-server redis.conf > redis.log &```
- redis-cli  启动客户端；
- ```redis-cli -h``` 自己的私有ip 连别人连别人的公共ip；
- ```redis-cli -h 172.18.230.165```
- auth 123456:输入密码
- ping检测是否成功；
- ```set key value``` 创建数据
- ```del key``` 删除
- ```exists key``` 查看有没有这个键
- get key 查看信息
- flushall 删除所有数据库所有数据
- redis 默认开了16个数据库
- flushdb 删除当前数据库数据
- save 保存（同步）
- bgsave 后台保存（异步操作）
- set foo foo@qq.com ex 3600
- ttl foo 查看数据存活时间
- 如果值为-1永不超时，-2没有了；
- expire foo 90 ：给数据设置时间限制；
- decr 减少键的数值
- incr 增加键的数值
- redis-benchmark -h ip -a 密码口令
  查看目前的服务器的吞吐量；
- 更多的命令可以去redis的网站学习[Redis](http://redisdoc.com/)





## python中操作redis数据库：
- import redis
- client = redis.StrictRedis(host='', port= , password='') ---创建一个redis对象
- client --- 连接
- 操作redis数据库的方式一般都是```client.redis命令()```


## 网站优化的两大定律：
1. 缓存 - 用空间换取时间 - Redis/Memcached
2. 削峰 - 能推迟的事情都不要马上做 - 消息队列RabbitMQ/RocketMQ(阿里)

>Redis - Remote Dictionary Server
用作高速缓存 - 优化系统的性能

>Redis的安装 - 源代码构建安装
启动Redis服务器
1.  redis-server --port 1234 --requirepass 123123
2.  redis-server redis.conf
3.  redis-server 
停止服务器:
kill 进程号 或者
Ctrl c 或者
客户端>shutdown

>连接redis:
```redis-cli -h 主机 -p 端口```


>redis数据类型：
- key:value
- 最常用的5种数据类型：
- 字符串 -  
- 哈希 - 保存对象
- 列表 - 栈、队列
- 集合 - 例如，适合做贴标签的功能
- 有序集合 - 适合做排行榜的功能


>补充：crontab -e 0 19 * * 5 操作；定时操作任务；

- info 查看服务器信息
- info replication 查看复制、奴隶信息
修改配置文件
- vim redis.conf
- /slave 查找到
slaveof 120.77.222.217 6379 连接主人ip的端口；
masterauth 主人的密码口令
- 重启服务器
主人写了会自动复制给奴隶
奴隶只能读不能写
- 主从复制（读写分离）
- master不用修改任何配置
- slave修改两条配置
- slaveof master的ip地址
- master的端口；
- masterauth master的口令；
- redis-cli 连自己的redis服务器
- info replication 
role:master/slave

>如果master关闭了，就需要设置一个哨兵，来监视master。如果master挂了，就将一个奴隶设置为master；


- ps -ef | grep redis-server | grep -v grep | awk（文字处理工具） '{print $2}' | xargs kill(将结果作为kill的参数)：一次性杀掉多个进程；


>配置哨兵
- cd redis-4.0.11
- cp redis-4.0.11/sentinel.conf ./sentinel.conf
- vim sentinel.conf
- - 编辑16行：
bind 私有ip
- - 编辑69行：
sentinel monitor mymaster 主人ip 端口号 1（投票）（谁得到这个票就成为主人）
- - 编辑98行：
sentinel  down-after-milliseconds mymaster 10000(挂了10s就重新选主人)
- - 编辑131行：
sentinel failover-timeout mymaster 180000(3分钟内连回来就成为奴隶，没连回来就被踢出去)

- 启动哨兵模式：
redis-server sentinel.conf --sentinel






>总结：

>Web前端/移动端 - HTML标签/CSS(Box model)/JavaScript(ES + BOM - window + DOM - document)/jQuery - $/$.getJSON/$.ajax

>Linux - 常用命令/vim/软件安装服务配置

>数据库 -SQL/NoSQL(Redis/MongoDB/ElasticSearch)























