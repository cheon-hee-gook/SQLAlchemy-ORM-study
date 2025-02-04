from fastapi import FastAPI
from app.api import flower

app = FastAPI()

# 꽃 API 라우터 등록
app.include_router(flower.router, prefix="/flowers", tags=["Flowers"])


@app.get("/")
def read_root():
    return {"message": "Welcome to Flower Meaning API"}
