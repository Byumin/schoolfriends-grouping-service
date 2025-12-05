import uvicorn
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from app.controller import router_db_test_connect # 라우터 api 엔드포인트 
from app.core.config import settings # db, app host, port 설정
from app.core.log_config import get_logger # 로거 설정

# 로거 가져오기
log = get_logger()
app = FastAPI()

# 전역 예외 처리기
# 시스템에서 처리하지 못한 모든 에러를 잡아서 로그 파일에 기록
@app.exception_handler(Exception)
async def global_exception_handler(request: Request, exc: Exception):
    # 핵심: 에러 발생 시 Traceback(위치 추적 정보) 전체를 로그 파일에 저장
    log.error(f"서버 내부 치명적 오류: {str(exc)}", exc_info=True)
    
    return JSONResponse(
        status_code=500,
        content={"message": "서버 내부 오류가 발생했습니다. 관리자에게 문의하세요."}
    )

# 라우터 등록 (임시)
app.include_router(
    router_db_test_connect.router, # <--- 저 파일 안에 있는 'router' 변수를 꺼내옴
    prefix="/grouping",        # <--- 이 라우터 안의 모든 URL 앞에 /grouping를 붙임
    tags=["grouping"]          # <--- Swagger 문서에서 'grouping'라는 제목으로 묶어서 보여줌
)

# 서버 실행
if __name__ == "__main__":
    log.info(f"=== 서버 시작 준비 완료 (Port: {settings.app_port}) ===")
    uvicorn.run(
        "main:app", 
        host=settings.app_host, 
        port=settings.app_port, 
        reload=True
    )
# 실행: uvicorn main:app --reload
# 가상환경 : .\venv\Scripts\Activate.ps1 (Windows)