from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.crud import create_flower, get_flower, get_flowers, update_flower, delete_flower
from app.schemas import FlowerCreate, FlowerUpdate, FlowerResponse

router = APIRouter()


def get_db():
    """ 데이터베이스 세션을 요청마다 생성 및 종료 """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/", response_model=FlowerResponse)
def add_flower(flower: FlowerCreate, db: Session = Depends(get_db)):
    """ 새로운 꽃 추가 """
    return create_flower(db, flower)


@router.get("/{flower_id}", response_model=FlowerResponse)
def read_flower(flower_id: int, db: Session = Depends(get_db)):
    """ 특정 꽃 조회 """
    flower = get_flower(db, flower_id)
    if not flower:
        raise HTTPException(status_code=404, detail="꽃을 찾을 수 없습니다.")
    return flower


@router.get("/", response_model=list[FlowerResponse])
def read_flowers(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    """ 모든 꽃 조회 (페이징) """
    return get_flowers(db, skip, limit)


@router.put("/{flower_id}", response_model=FlowerResponse)
def edit_flower(flower_id: int, flower_update: FlowerUpdate, db: Session = Depends(get_db)):
    """ 꽃 정보 수정 """
    updated_flower = update_flower(db, flower_id, flower_update)
    if not updated_flower:
        raise HTTPException(status_code=404, detail="꽃을 찾을 수 없습니다.")
    return updated_flower


@router.delete("/{flower_id}", response_model=FlowerResponse)
def remove_flower(flower_id: int, db: Session = Depends(get_db)):
    """ 꽃 정보 삭제 """
    deleted_flower = delete_flower(db, flower_id)
    if not deleted_flower:
        raise HTTPException(status_code=404, detail="꽃을 찾을 수 없습니다.")
    return deleted_flower
