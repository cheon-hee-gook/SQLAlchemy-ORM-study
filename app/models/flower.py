from sqlalchemy import Column, Integer, String
from app.database import Base
from sqlalchemy.orm import relationship
from app.models.flower_category import flower_category


class Flower(Base):
    __tablename__ = "flowers"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    meaning = Column(String)

    categories = relationship("Category", secondary=flower_category, back_populates="flowers")
