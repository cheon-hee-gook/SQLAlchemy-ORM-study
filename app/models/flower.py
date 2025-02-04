from sqlalchemy import Column, Integer, String
from app.database import Base


class Flower(Base):
    __tablename__ = "flowers"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    meaning = Column(String)
