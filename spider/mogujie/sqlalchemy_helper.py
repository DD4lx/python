from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey, UniqueConstraint, Index
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy import create_engine

from models import MogujieProduct

engine = create_engine("mysql+pymysql://root:123456@127.0.0.1/mogujie_db?charset=utf8mb4", max_overflow=5)
session_maker = sessionmaker(bind=engine)
session = session_maker()


def save_db(result_list):
    for item in result_list:
        mogu = MogujieProduct()
        mogu.tradeitemid = item['tradeItemId']
        mogu.img = item['img']
        mogu.itemtype = item['itemType']
        mogu.clienturl = item['clientUrl']
        mogu.link = item['link']
        mogu.itemmarks = item['itemMarks']
        mogu.acm = item['acm']
        mogu.title = item['title']
        mogu.type = item['type']
        mogu.orgprice = item['orgPrice']
        mogu.hassimilarity = item['hasSimilarity']
        mogu.cfav = item['cfav']
        mogu.price = item['price']
        mogu.similarityurl = item['similarityUrl']


        session.add(mogu)
        session.commit()



