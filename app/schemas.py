from typing import List, Optional

from pydantic import BaseModel

from typing import List, Optional
from pydantic import BaseModel


class FlowerBase(BaseModel):
    name: str
    meaning: str


class FlowerCreate(FlowerBase):
    category_ids: Optional[List[int]] = []  # 꽃 생성 시 카테고리 ID 리스트 추가 ✅


class FlowerUpdate(FlowerBase):
    category_ids: Optional[List[int]] = None  # 꽃 수정 시 카테고리 변경 가능하도록 추가 ✅


class CategoryBase(BaseModel):
    name: str


class CategoryCreate(CategoryBase):
    pass


class CategoryResponse(CategoryBase):
    id: int

    class Config:
        from_attributes = True


class FlowerResponseWithoutCategory(FlowerBase):
    id: int

    class Config:
        from_attributes = True


class FlowerResponseWithCategory(FlowerBase):
    id: int
    categories: List[CategoryResponse] = []  # Many-to-Many 관계 대응 ✅

    class Config:
        from_attributes = True