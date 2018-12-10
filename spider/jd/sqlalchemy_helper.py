from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey, UniqueConstraint, Index
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy import create_engine

from models import JD

engine = create_engine("mysql+pymysql://root:123456@127.0.0.1/jd_db?charset=utf8mb4", max_overflow=5)
session_maker = sessionmaker(bind=engine)
session = session_maker()


def save_db(result_list):
    for item in result_list:
        jd = JD()
        jd.sku = item['sku']
        jd.img = item['img']
        jd.price = item['price']
        jd.title = item['title']
        jd.href = item['href']
        jd.name = item['name']
        jd.commit = item['commit']
        jd.commit_url = item['commit_url']
        jd.shop_name = item['shop_name']
        jd.shop_url = item['shop_url']
        session.add(jd)
        session.commit()



