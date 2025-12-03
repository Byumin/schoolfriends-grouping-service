from sqlalchemy import Column, String, Date, DateTime, Text, Integer
from sqlalchemy.orm import relationship
from app.db.session import Base

'''
RDS에서 가지고 올 테이블을 사전정의 (AWS 데이터 카탈로그 개념과 비슷)
'''

class SchoolClass(Base):
    __tablename__ = "school_class"
    class_code = Column(String, primary_key=True, index=True, nullable=False)
    school_code = Column(String, nullable=False)
    member_no = Column(String, nullable=True, default=None)
    member_name = Column(String, nullable=True, default=None)
    member_cellphone_num = Column(String, nullable=True, default=None)
    class_name = Column(String, nullable=True, default=None)
    school_date = Column(Date, nullable=False)
    school_grade = Column(String, nullable=False)
    school_num = Column(String, nullable=False)
    use_yn = Column(String(1), default='Y', nullable=True)
    memo = Column(String, nullable=True, default=None)
    reg_member_no = Column(String, nullable=False)
    reg_date = Column(DateTime, nullable=False)
    mod_member_no = Column(String, nullable=True, default=None)
    mod_date = Column(DateTime, nullable=True, default=None)

class PsyClass(Base):
    __tablename__ = "psy_class"
    psy_code = Column(String, primary_key=True, index=True, nullable=False)
    class_code = Column(String, nullable=True)
    psy_ord_target = Column(String, nullable=True)
    psy_ord_no = Column(String, nullable=True)
    psy_name = Column(String, nullable=True)
    psy_url = Column(String, nullable=True)
    start_date = Column(Date, nullable=True)
    end_date = Column(Date, nullable=True)
    original_end_date = Column(Date, nullable=True)
    longitudinal_yn = Column(String(1), nullable=True)
    close_yn = Column(String(1), nullable=True)
    use_yn = Column(String(1), default=None, nullable=False)
    use_cnt = Column(Integer, default=0, nullable=True)
    use_date = Column(DateTime, nullable=True)
    memo = Column(String, nullable=True)
    reg_member_no = Column(String, nullable=False)
    reg_date = Column(DateTime, nullable=False)
    mod_member_no = Column(String, nullable=True)
    mod_date = Column(DateTime, nullable=True)