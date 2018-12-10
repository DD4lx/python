import pymysql

# 获取数据库连接
def get_connection():
    host = '127.0.0.1'
    port = 3306
    user = 'root'
    password = '123456'
    database = 'maoyan_db'
    db = pymysql.connect(host, user, password, database, charset='utf8', port=port)
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
    sql = "insert into maoyan (star, name, score, rate, time, img_url) values ('%s', '%s', '%s', '%s', '%s', '%s')" % (item['star'], item['name'], item['score'], item['rate'], item['time'], item['img_url'])
    print(sql)
    cursor.execute(sql)
    db.commit()
