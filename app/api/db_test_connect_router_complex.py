# crud, service, schema 적용 라우터
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session # SQLAlchemy 세션
from app.db.session import SessionLocal # DB 세션
from app.schemas.schema import (schema_TestJoinSchoolClassRequest, schema_TestJoinSchoolClassResponse) # 요청/응답 스키마
from app.services.service import service_get_joined_school_class # 서비스 함수

router = APIRouter()
# DB 세션 생성 함수
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
# 라우터
@router.post("/test-join-school-class", response_model=list[schema_TestJoinSchoolClassResponse]) # 응답 스키마 지정 (검증)
def test_join_school_class(request: schema_TestJoinSchoolClassRequest, db: Session = Depends(get_db)): # 응답 스키마 지정 (검증), db 세션 주입
    result = service_get_joined_school_class( # 서비스 함수 호출
        db, # db 세션
        request.school_code , # 요청 데이터에서 조건값 추출
        request.class_code # 요청 데이터에서 조건값 추출
    )
    return result