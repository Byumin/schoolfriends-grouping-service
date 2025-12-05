from fastapi import APIRouter, Depends
from app.database import CurrentSession
from app.vo.schema import schema_TestJoinSchoolClassRequest, schema_TestJoinSchoolClassResponse
from app.services import service

# 이 'router' 변수가 나중에 main.py로 배달되어 app에 장착됩니다.
router = APIRouter()

# [GET] 
# URL: http://127.0.0.1:8090/items/ (main.py의 prefix="/items"와 합쳐짐)
@router.get("/", response_model=list[schema_TestJoinSchoolClassResponse]) 
def get_list(
        # [중요] 의존성 주입 (DI)
        # 요청이 올 때마다 DB 세션을 하나 만들어서 db 변수에 꽂아줍니다.
        db: CurrentSession,
        search: schema_TestJoinSchoolClassRequest = Depends()
    ):
    # Service 호출 (DB 세션을 파라미터로 넘겨줌)
    return service.school_class_get_list(db, search)

# # [POST] 
# # URL: http://127.0.0.1:8090/items/
# @router.post("/", response_model=ResultVO)
# def register(
#         # [중요] Request Body 파싱 - Spring의 @RequestBody
#         # DB 세션 주입
#         db: CurrentSession,
#         # JSON 데이터를 받아서 ItemCreateVO 객체로 자동 변환해줍니다.
#         item: ItemResponseVO = Depends()
#     ):
#     # Service 호출
#     return service_school_class_register(db, item)