from sqlalchemy.orm import Session, joinedload

from app.models.category import Category
from app.models.flower import Flower
from app.schemas import FlowerCreate, FlowerUpdate


def create_flower(db: Session, flower_data: FlowerCreate):
    """ 꽃 추가 및 카테고리 연결 """
    db_flower = Flower(name=flower_data.name, meaning=flower_data.meaning)
    db.add(db_flower)
    db.commit()
    db.refresh(db_flower)

    if flower_data.category_ids:
        categories = db.query(Category).filter(Category.id.in_(flower_data.category_ids)).all()
        db_flower.categories.extend(categories)
        db.commit()

    return db_flower


def update_flower(db: Session, flower_id: int, flower_data: FlowerUpdate):
    """ 꽃 정보 및 카테고리 수정 """
    db_flower = db.query(Flower).filter(Flower.id == flower_id).first()
    if not db_flower:
        return None

    db_flower.name = flower_data.name
    db_flower.meaning = flower_data.meaning

    if flower_data.category_ids is not None:
        categories = db.query(Category).filter(Category.id.in_(flower_data.category_ids)).all()
        db_flower.categories = categories

    db.commit()
    db.refresh(db_flower)
    return db_flower

def get_flower(db: Session, flower_id: int):
    """ 특정 꽃 조회 """
    return db.query(Flower).filter(Flower.id == flower_id).first()


def get_flowers(db: Session, skip: int = 0, limit: int = 10):
    """ 모든 꽃 조회 (페이징) """
    return db.query(Flower).offset(skip).limit(limit).all()


def delete_flower(db: Session, flower_id: int):
    """ 꽃 정보 삭제 """
    db_flower = db.query(Flower).filter(Flower.id == flower_id).first()
    if not db_flower:
        return None
    db.delete(db_flower)
    db.commit()
    return db_flower


def get_flower_with_category(db: Session, flower_id: int):
    """ 꽃 정보를 카테고리 정보와 함께 조회 """
    return db.query(Flower).options(joinedload(Flower.categories)).filter(Flower.id == flower_id).first()
