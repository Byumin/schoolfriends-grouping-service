from sqlalchemy.orm import Session
from app.db.models import models_SchoolClass, models_PsyClass

def crud_test_join_school_class(db: Session, condition_school_code: str, condition_class_code: str):
    return (
        db.query(
            models_SchoolClass.school_code,
            models_SchoolClass.class_code,
            models_SchoolClass.member_no,
            models_PsyClass.psy_code,
            models_PsyClass.psy_name,
            models_PsyClass.end_date
        )
        .join(
            models_PsyClass,
            models_SchoolClass.class_code == models_PsyClass.class_code
        )
        .filter(
            models_SchoolClass.school_code == condition_school_code,
            models_SchoolClass.class_code == condition_class_code
        )
        .all()
    )