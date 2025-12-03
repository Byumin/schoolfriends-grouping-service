from app.db.crud.teacher_crud import get_students_of_teacher

class StudentRosterService:
    def get_students_by_class(self, class_code: str):
        students = get_students_of_class(class_code)
        return {"students": students}