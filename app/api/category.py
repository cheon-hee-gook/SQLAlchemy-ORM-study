from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.models.category import Category
from app.schemas import CategoryCreate, CategoryResponse

router = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/", response_model=CategoryResponse)
def add_category(category: CategoryCreate, db: Session = Depends(get_db)):
    """ 새로운 카테고리 추가 """
    db_category = Category(name=category.name)
    db.add(db_category)
    db.commit()
    db.refresh(db_category)
    return db_category


@router.get("/", response_model=list[CategoryResponse])
def read_categories(db: Session = Depends(get_db)):
    """ 모든 카테고리 조회 """
    return db.query(Category).all()
