from sqlalchemy.orm import Session
from fastapi import HTTPException
from app.dao import crud
from app.vo.schema import schema_TestJoinSchoolClassRequest, schema_TestJoinSchoolClassResponse
from app.core.log_config import get_logger

log = get_logger()

# 비즈니스 로직을 수행하고, DAO에게 DB 작업을 시키는 계층
def school_class_get_list(db: Session, search: schema_TestJoinSchoolClassRequest):
    log.info("리스트 조회 서비스 시작")
    return crud.crud_select(db, search)

# # 저장 서비스
# def service_school_class_register(db: Session, vo: schema_TestJoinSchoolClassResponse):
#     log.info(f"등록 요청: {vo.school_code}")
    
#     # 트랜잭션 시작 (Spring의 @Transactional 범위)
#     # 이 블록({}) 안의 모든 DB 작업은 한 몸입니다.
#     with db.begin():
#         log.info("트랜잭션 시작 (Auto Commit 모드)")
        
#         # DAO 호출 (여기서 에러 나면 알아서 Rollback 됨)
#         result = crud.insert(db, vo)
        
#         # 필요하면 DAO 또 호출
#         # crud.update_stock(db, ...)
        
#         log.info("로직 완료. (잠시 후 자동 커밋됨)")
#         return result
    
#     # 블록을 무사히 빠져나오면 여기서 자동으로 'COMMIT'이 실행된 상태임