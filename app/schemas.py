from pydantic import BaseModel


class FlowerBase(BaseModel):
    name: str
    meaning: str


class FlowerCreate(FlowerBase):
    pass  # 추가할 때 필요한 필드 (name, meaning)


class FlowerUpdate(FlowerBase):
    pass  # 수정할 때 필요한 필드 (name, meaning)


class FlowerResponse(FlowerBase):
    id: int

    class Config:
        from_attributes = True
