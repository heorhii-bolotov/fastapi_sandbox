from operator import index
from db.database import Base
from sqlalchemy import Column, String
from sqlalchemy.sql.sqltypes import Integer


class DBUser(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String)
    email = Column(String)
    password = Column(String)
