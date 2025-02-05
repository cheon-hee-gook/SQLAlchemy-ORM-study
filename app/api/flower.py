from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.crud import create_flower, get_flower, get_flowers, update_flower, delete_flower, get_flower_with_category
from app.schemas import FlowerCreate, FlowerUpdate, FlowerResponseWithCategory, FlowerResponseWithoutCategory

router = APIRouter()


def get_db():
    """ 데이터베이스 세션을 요청마다 생성 및 종료 """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/", response_model=FlowerResponseWithCategory)
def add_flower(flower: FlowerCreate, db: Session = Depends(get_db)):
    """ 꽃 추가 (카테고리 포함 가능) """
    return create_flower(db, flower)


@router.put("/{flower_id}", response_model=FlowerResponseWithCategory)
def edit_flower(flower_id: int, flower_update: FlowerUpdate, db: Session = Depends(get_db)):
    """ 꽃 정보 수정 (카테고리 포함 가능) """
    updated_flower = update_flower(db, flower_id, flower_update)
    if not updated_flower:
        raise HTTPException(status_code=404, detail="꽃을 찾을 수 없습니다.")
    return updated_flower


@router.get("/{flower_id}", response_model=FlowerResponseWithoutCategory)
def read_flower(flower_id: int, db: Session = Depends(get_db)):
    """ 특정 꽃 조회 """
    flower = get_flower(db, flower_id)
    if not flower:
        raise HTTPException(status_code=404, detail="꽃을 찾을 수 없습니다.")
    return flower

@router.get("/detail/{flower_id}", response_model=FlowerResponseWithCategory)
def read_detail_flower(flower_id: int, db: Session = Depends(get_db)):
    """ 꽃 정보를 카테고리 정보와 함께 조회 """
    flower = get_flower_with_category(db, flower_id)
    if not flower:
        raise HTTPException(status_code=404, detail="꽃을 찾을 수 없습니다.")
    return flower


@router.get("/", response_model=list[FlowerResponseWithoutCategory])
def read_flowers(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    """ 모든 꽃 조회 (페이징) """
    return get_flowers(db, skip, limit)


@router.delete("/{flower_id}", response_model=FlowerResponseWithoutCategory)
def remove_flower(flower_id: int, db: Session = Depends(get_db)):
    """ 꽃 정보 삭제 """
    deleted_flower = delete_flower(db, flower_id)
    if not deleted_flower:
        raise HTTPException(status_code=404, detail="꽃을 찾을 수 없습니다.")
    return deleted_flower
