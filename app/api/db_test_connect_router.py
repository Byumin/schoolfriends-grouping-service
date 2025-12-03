from fastapi import APIRouter, Depends
from app.db.session import SessionLocal

router = APIRouter()

@router.get("/db-test")
def test_db():
    db = SessionLocal()
    result = db.execute("SELECT 1").fetchone()
    db.close()
    return {"db_connected": bool(result)}