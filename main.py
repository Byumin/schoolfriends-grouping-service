from fastapi import FastAPI
from app.api.db_test_connect_router_complex import router as db_test_connect_router_complex
from app.api.db_test_connect_router import router as db_test_connect_router

app = FastAPI()

# FastAPI에서 하나의 엔드포인트(API URL)를 만드는 방법
# @app.get("/")  # 데코레이터, '/'주소로 들어오는 GET 요청을 처리
# def root():
#     return {"message": "FastAPI running!"}

# 라우터 등록
app.include_router(db_test_connect_router)
app.include_router(
    db_test_connect_router_complex,
    prefix="/complex",     # 선택사항: 엔드포인트 앞에 접두사 붙이기
    tags=["Complex Test"]  # Docs용
)

# 실행: uvicorn main:app --reload
# 가상환경 : .\venv\Scripts\Activate.ps1 (Windows)