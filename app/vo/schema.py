from pydantic import BaseModel
# VO = Value Object
'''
JSON을 받아서 
자동으로 Python 객체로 검증 및 반환해줌
학교에 속한 학급 명단 조회 요청 스키마
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
    school_name: str
    class_code: str
    school_grade: str
    school_num: str