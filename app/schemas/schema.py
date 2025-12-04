from datetime import date
from pydantic import BaseModel
'''
JSON을 받아서 자동으로 Python 객체로 변환해줌
학생 명단 조회 요청 스키마
인자 : school_code(학교코드), class_code(학급코드)
예시 : 학지중학교(AD0001), 1학년 15반(AD00012025101F03E)
'''
# 입력 검증용 스키마
class schema_TestJoinSchoolClassRequest(BaseModel):
    school_code: str
    class_code: str

# 출력 검증용 스키마
class schema_TestJoinSchoolClassResponse(BaseModel):
    school_code: str
    class_code: str
    member_no: str
    psy_code: str
    psy_name: str
    end_date: date