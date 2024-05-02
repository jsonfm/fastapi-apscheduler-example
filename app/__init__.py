from contextlib import asynccontextmanager
from fastapi import FastAPI
from app.router import router
from app.scheduler import get_scheduler


@asynccontextmanager
async def lifespan(app: FastAPI):
    print("starting scheduler")
    scheduler = get_scheduler()
    scheduler.start()
    yield
    scheduler.shutdown()
    print("closed scheduler!")


def get_app():
    app = FastAPI(lifespan=lifespan)
    app.include_router(router)
    return app
