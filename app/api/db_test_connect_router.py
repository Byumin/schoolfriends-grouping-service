from fastapi import APIRouter, Depends
from app.db.session import SessionLocal
from sqlalchemy import text
from sqlalchemy.orm import Session
from app.db.models import models_PsyClass, models_SchoolClass

router = APIRouter()

@router.get("/db_test")
def test_db():
    db = SessionLocal()
    result = db.execute(text("SELECT 1")).fetchone()
    db.close()
    return {"db_connected": bool(result)}

@router.get("/test_school_class")
def test_school_class():
    db: Session = SessionLocal() # session 정보
    rows = db.query(SchoolClass).limit(10).all()
    db.close()

    # SQLAlchemy 객체는 바로 JSON 변환이 안 되므로 dict로 변환
    result = []
    for row in rows:
        result.append({
            "class_code": row.class_code,
            "school_code": row.school_code,
            "member_no": row.member_no,
            "member_name": row.member_name,
            "class_name": row.class_name,
            "school_grade": row.school_grade,
            "school_num": row.school_num,
        })

    return {"data": result}

# 테스트 : SCHOOL_CLASS 와 PSY_CLASS 조인
@router.get("/test_join_school_class")
def test_join_school_class():
    # rds 연결
    db: Session = SessionLocal()
    # 조건값 설정
    condition_school_code = 'AD0001'
    condition_class_code = 'AD00012025101F03E'
    # 조인 쿼리 실행
    rows = (
        # select 절
        db.query( 
            models_SchoolClass.school_code,
            models_SchoolClass.class_code,
            models_SchoolClass.member_no,
            models_PsyClass.psy_code,
            models_PsyClass.psy_name,
            models_PsyClass.end_date
        )
        # from 절 및 join 절
        .join(
            models_PsyClass,
            models_SchoolClass.class_code == models_PsyClass.class_code
        )
        # where 절
        .filter(
            models_SchoolClass.school_code == condition_school_code,
            models_SchoolClass.class_code == condition_class_code
        )
        .all()
    )
    db.close()
    # row 객체 → dict 변환
    result = []
    for row in rows:
        result.append({
            "school_code": row[0],
            "class_code": row[1],
            "member_no": row[2],
            "psy_code": row[3],
            "psy_name": row[4],
            "end_date": row[5]
        })
    return {"data": result}

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