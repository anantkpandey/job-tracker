from fastapi import APIRouter
from app.models.job import Job

router = APIRouter()

jobs = []
next_id = 1


@router.get("/jobs")
def get_jobs():
    return jobs


@router.post("/jobs")
def create_job(job: Job):
    global next_id

    job_data = {
        "id": next_id,
        "company": job.company,
        "position": job.position,
        "status": job.status
    }

    jobs.append(job_data)
    next_id += 1

    return job_data