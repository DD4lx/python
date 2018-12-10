import pymysql


# 获取数据库连接
def get_connection():
    host = '127.0.0.1'
    port = 3306
    user = 'root'
    password = '123456'
    database = 'douban_db'
    db = pymysql.connect(host, user, password, database, charset='utf8mb4', port=port)
    return db


# 获取数据库游标
def get_cursor(db):
    cursor = db.cursor()
    return cursor


# 关闭数据库连接
def close_connection(db):
    db.close()


# 插入一条数据
def insert_record(db, cursor, item):
    sql = "insert into douban (title, likes, content, groups, time, group_url, image_url) values ('%s', '%s', '%s', '%s', '%s', '%s', '%s')" % (item['title'], item['likes'], item['content'], item['groups'], item['time'], item['group_url'], item['image_url'])
    print(sql)
    cursor.execute(sql)
    db.commit()

