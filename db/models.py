from operator import index
from db.database import Base
from sqlalchemy import Boolean, Column, ForeignKey, String
from sqlalchemy.sql.sqltypes import Integer
from sqlalchemy.orm import relationship


class DBUser(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String)
    email = Column(String)
    password = Column(String)
    items = relationship("DBArticle", back_populates="user")


class DBArticle(Base):
    __tablename__ = "articles"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    content = Column(String)
    published = Column(Boolean)
    user_id = Column(Integer, ForeignKey("users.id"))
    user = relationship("DBUser", back_populates="items")
