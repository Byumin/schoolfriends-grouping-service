SELECT_ALL = """
    SELECT  
        A.SCHOOL_CODE AS school_code,
        A.SCHOOL_GRADE AS school_grade,
        B.STUDENT_CODE AS student_code
    FROM SCHOOL_CLASS A , SCHOOL_STUDENT B
    WHERE A.CLASS_CODE = B.CLASS_CODE
    AND A.SCHOOL_CODE = :school_code
    AND A.SCHOOL_GRADE = :school_grade
"""
INSERT_ITEM = """
    INSERT INTO CLASS_ASSIGNMENT_STUDENT (
        SCHOOL_CODE, 
        SCHOOL_GRADE, 
        STUDENT_CODE
    )VALUES (
        :school_code, 
        :school_grade, 
        :student_code
    )
"""
SCHOOL_CLASS_SELECT_ALL = """
    SELECT
        A.SCHOOL_CODE AS school_code,
        A.SCHOOL_NAME AS school_name,
        B.CLASS_CODE AS class_code,
        B.SCHOOL_GRADE AS school_grade,
        B.SCHOOL_NUM AS school_num
    FROM SCHOOL_INFO A
    INNER JOIN SCHOOL_CLASS B
    ON A.SCHOOL_CODE = B.SCHOOL_CODE
    WHERE A.SCHOOL_CODE = :school_code
    AND B.CLASS_CODE = :class_code
"""