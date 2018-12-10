from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey, UniqueConstraint, Index
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy import create_engine

engine = create_engine("mysql+pymysql://root:123456@127.0.0.1:3306/jd_db?charset=utf8mb4", max_overflow=5)
Base = declarative_base()

class JD(Base):
    __tablename__ = 'jd'
    id = Column(Integer, primary_key=True, autoincrement=True)    #主键，自增
    sku = Column(String(32))
    title = Column(String(512))
    href = Column(String(1024))
    img = Column(String(1024))
    price = Column(String(32))
    name = Column(String(1024))
    commit = Column(String(1024))
    commit_url = Column(String(1024))
    shop_url = Column(String(1024))
    shop_name = Column(String(512))
