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







