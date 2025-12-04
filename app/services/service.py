from sqlalchemy.orm import Session # SQLAlchemy 세션
from app.db.crud import crud_test_join_school_class # CRUD 함수 (쿼리만 던지는)
from app.schemas.schema import schema_TestJoinSchoolClassResponse # 응답 스키마

def service_get_joined_school_class(db: Session, condition_school_code: str, condition_class_code: str):

    rows = crud_test_join_school_class(db, condition_school_code, condition_class_code)

    result = []
    for row in rows:
        result.append(schema_TestJoinSchoolClassResponse(
            school_code=row[0],
            class_code=row[1],
            member_no=row[2],
            psy_code=row[3],
            psy_name=row[4],
            end_date=row[5]
        ))

    return result