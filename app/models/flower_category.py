from sqlalchemy import Column, Integer, ForeignKey, Table
from app.database import Base


flower_category = Table(
    "flower_category",
    Base.metadata,
    Column("flower_id", Integer, ForeignKey("flowers.id"), primary_key=True),
    Column("category_id", Integer, ForeignKey("categories.id"), primary_key=True),
)
