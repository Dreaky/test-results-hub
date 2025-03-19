from fastapi import APIRouter
from app.core.services.test_service import TestService

router = APIRouter()

@router.post("/report_failed_test")
async def report_failed_test(data: dict):
    TestService.process_failed_test(
        run_id=data["run_id"],
        tc_id=data["tc_id"],
        test_status=data["status"],
        elapsed=data["elapsed"],
        tag=data["tag"],
        notes=data["notes"],
        report_path=data["report_path"]
    )
    return {"message": "Test result stored successfully"}