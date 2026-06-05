from fastapi import APIRouter

router = APIRouter()

@router.get("/jobs")
def get_jobs():
    return [
        {
            "id": 1,
            "company": "OpenAI",
            "position": "Backend Developer",
            "status": "Applied"
        }
    ]