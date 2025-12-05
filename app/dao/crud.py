from sqlalchemy.orm import Session
from sqlalchemy import text
from app.mapper import raw_sql
from app.vo.schema import schema_TestJoinSchoolClassRequest, schema_TestJoinSchoolClassResponse
from app.core.log_config import get_logger
# DAO = Data Access Object 라는 뜻
# DB에 직접 접근해서 SQL을 실행하는 계층 -> DB 작업만 담당하는 모듈
log = get_logger()

# 조회 쿼리   
def crud_select(db: Session, search: schema_TestJoinSchoolClassRequest): # 세선과 검색 조건(condition) 파라미터을 받아
    try:
        # serch라는 VO 객체를 딕셔너리(Map)로 변환
        params = search.model_dump() # model_dump(): Pydantic 객체를 dict로 변환해주는 메서드
        log.debug(f"전달할 파라미터: {params}")
        # MyBatis: session.selectList("mapper.selectAll")
        result = db.execute(text(raw_sql.SCHOOL_CLASS_SELECT_ALL), params).all() # SQL 실행 및 결과 받기
        
        # result 객체를 dict 변환 후 리스트로 리턴
        return [row._mapping for row in result] # _mapping: Row 객체를 dict로 변환해주는 속성
        
    except Exception as e:
        # [로그] 에러 스택 트레이스 저장 (e.printStackTrace())
        log.error("전체 조회 중 DB 에러 발생", exc_info=True)
        raise e # 서비스로 에러 던지기
    
# #! 이건 건들지 말자
# def crud_insert(db: Session, vo: schema_TestJoinSchoolClassResponse):
#     try:
#         log.debug(f"SQL 실행 준비: {raw_sql.INSERT_ITEM}")
        
#         # INSERT 실행
#         # 파라미터: VO를 딕셔너리(Map)로 풀어서 바인딩 (:name, :price ...)
#         db.execute(text(raw_sql.INSERT_ITEM), vo.model_dump())
        
#         # [Flush] 임시 반영
#         # DB 메모리에 SQL은 보냈지만, 아직 '확정(Commit)'은 안 찍은 상태.
#         db.flush() 
        
#         # 리턴
#         return {"status": "success", "message": "저장 성공했다"}
        
#     except Exception as e:

#         log.error(f"데이터 저장 실패 - 입력값: {vo}", exc_info=True)
        
#         # 서비스(Service)에게 "비상 사태!" 알림 (에러 재발생)
#         raise e 
