# 🌸 Flower Meaning API

## 📌 프로젝트 개요
이 프로젝트는 SQLAlchemy ORM을 활용하여 꽃과 꽃말을 관리하는 API입니다.  
FastAPI를 기반으로 CRUD 기능과 고급 ORM 기능을 학습하는 목적으로 개발되었습니다.

## 🚀 학습 목표
✅ FastAPI 기반 REST API  
✅ SQLAlchemy ORM & Alembic 마이그레이션  
✅ 1:N & N:M 관계형 데이터 모델링  
✅ 이벤트 리스너를 활용한 자동 데이터 변환  
✅ Pydantic을 통한 데이터 유효성 검사  
✅ 비동기 SQLAlchemy ORM 
✅ 최적화된 쿼리 (`joinedload`, `subqueryload`)  

## 📂 프로젝트 구조
```plaintext
flower-meaning-api/
│── app/
│   ├── main.py              # FastAPI 엔트리포인트
│   ├── models/              # SQLAlchemy ORM 모델
│   ├── crud.py              # 데이터 조작 함수 (CRUD)
│   ├── schemas.py           # Pydantic 데이터 모델
│   ├── api/                 # API 엔드포인트
│   ├── database.py          # 데이터베이스 연결 설정
│── migrations/              # Alembic 마이그레이션 폴더
│── tests/                   # 테스트 코드 폴더
│── .env                     # 환경 변수 설정 파일
│── requirements.txt         # 패키지 종속성 목록
│── README.md                # 프로젝트 설명서
│── .gitignore               # Git에 포함하지 않을 파일 목록
```

### 1️⃣ 패키지 설치
```bash
pip install -r requirements.txt
```
### 2️⃣ 데이터베이스 마이그레이션
```bash
alembic upgrade head
```
### 3️⃣ FastAPI 실행
```bash
uvicorn app.main:app --reload
```

## 📝 1일 차 진행 내용

### ✅ 프로젝트 기본 설정
1. Git 레포지토리 생성 및 초기화
2. FastAPI 프로젝트 구조 설정
3. SQLAlchemy ORM 및 Alembic 설정 
4. 데이터베이스 연결 코드 (database.py) 작성 
5. 기본 Flower 모델 (models/flower.py) 구현 
6. 마이그레이션 생성 및 적용 (alembic)
7. FastAPI 기본 라우트 (main.py) 추가 및 서버 실행 테스트

## 📝 2일 차 진행 내용

### ✅ CRUD 기능 구현
1. SQLAlchemy ORM을 사용한 CRUD 함수 (crud.py) 작성 
   - 꽃 정보 추가 (create_flower)
   - 특정 꽃 조회 (get_flower)
   - 꽃 목록 조회 (get_flowers)
   - 꽃 정보 수정 (update_flower)
   - 꽃 삭제 (delete_flower)

2. Pydantic을 활용한 데이터 유효성 검사 (schemas.py)
3. FastAPI 엔드포인트 (api/flower.py) 추가 
   - POST /flowers/ - 꽃 추가 
   - GET /flowers/ - 꽃 목록 조회 with 페이징 
   - GET /flowers/{id} - 특정 꽃 조회 
   - PUT /flowers/{id} - 꽃 정보 수정 
   - DELETE /flowers/{id} - 꽃 삭제
4. FastAPI 메인 파일 (main.py)에서 API 라우터 등록 
5. Postman 및 Swagger UI를 활용한 API 테스트