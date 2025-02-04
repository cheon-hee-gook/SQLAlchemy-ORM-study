from sqlalchemy.orm import Session
from app.models.flower import Flower
from app.schemas import FlowerCreate, FlowerUpdate


def create_flower(db: Session, flower: FlowerCreate):
    """ 꽃 데이터 추가 """
    db_flower = Flower(name=flower.name, meaning=flower.meaning)
    db.add(db_flower)
    db.commit()
    db.refresh(db_flower)
    return db_flower


def get_flower(db: Session, flower_id: int):
    """ 특정 꽃 조회 """
    return db.query(Flower).filter(Flower.id == flower_id).first()


def get_flowers(db: Session, skip: int = 0, limit: int = 10):
    """ 모든 꽃 조회 (페이징) """
    return db.query(Flower).offset(skip).limit(limit).all()


def update_flower(db: Session, flower_id: int, flower_update: FlowerUpdate):
    """ 꽃 정보 수정 """
    db_flower = db.query(Flower).filter(Flower.id == flower_id).first()
    if not db_flower:
        return None
    db_flower.name = flower_update.name
    db_flower.meaning = flower_update.meaning
    db.commit()
    db.refresh(db_flower)
    return db_flower


def delete_flower(db: Session, flower_id: int):
    """ 꽃 정보 삭제 """
    db_flower = db.query(Flower).filter(Flower.id == flower_id).first()
    if not db_flower:
        return None
    db.delete(db_flower)
    db.commit()
    return db_flower
