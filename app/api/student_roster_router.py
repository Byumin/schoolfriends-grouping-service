from fastapi import APIRouter
from app.schemas.student_roster_schema import StudentRosterQueryRequest
from app.services.teacher_service import TeacherService

router = APIRouter(prefix="/studentroster", tags=["studentroster"])
service = StudentRosterService()

@router.post("/studentroster")
def get_students(req: StudentRosterQueryRequest):
    return service.get_students_by_teacher(req.teacher_id, req.grade)