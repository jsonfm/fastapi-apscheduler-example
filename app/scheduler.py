from apscheduler.schedulers.asyncio import AsyncIOScheduler
from apscheduler.jobstores.memory import MemoryJobStore


scheduler = None


def get_scheduler():
    global scheduler
    jobstores = {"default": MemoryJobStore()}
    if scheduler is None:
        scheduler = AsyncIOScheduler(jobstores=jobstores, timezone="US/Pacific")
    return scheduler
