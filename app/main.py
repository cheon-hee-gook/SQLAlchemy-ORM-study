from fastapi import FastAPI
from app.api import flower, category

app = FastAPI()

# 꽃 API 라우터 등록
app.include_router(flower.router, prefix="/flowers", tags=["Flowers"])
# 카테고리 API 라우터 등록
app.include_router(category.router, prefix="/categories", tags=["Categories"])

@app.get("/")
def read_root():
    return {"message": "Welcome to Flower Meaning API"}
