from fastapi import APIRouter
from app import callback
from app.scheduler import get_scheduler


router = APIRouter(prefix="/events", tags=["Events"])
scheduler = get_scheduler()


@router.get("/")
def get_events():
    jobs = scheduler.get_jobs()
    data = list(map(lambda job: {"id": job.id, "name": job.name}, jobs))
    return data


@router.get("/{job_id}")
def get_event(job_id: str):
    job = scheduler.get_job(job_id)
    job_id = None
    if job is not None:
        job_id = job.id
    return {"job_id": job_id}


@router.post("/")
def create_event():
    job = scheduler.add_job(callback, "interval", seconds=10)
    return {"job_id": job.id}


@router.delete("/{job_id}")
def delete_event(job_id: str):
    job = scheduler.get_job(job_id)
    if job is not None:
        job.remove()
    return {"job_id": job_id}
