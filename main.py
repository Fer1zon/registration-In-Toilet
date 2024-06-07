from contextlib import asynccontextmanager

from fastapi import FastAPI


from database import createTables

from scheduler.main import scheduler

from fastapi.staticfiles import StaticFiles






@asynccontextmanager
async def lifespan(app: FastAPI):
    scheduler.start()
    await createTables()
    yield








app = FastAPI(lifespan=lifespan)
app.mount('/static', app=StaticFiles(directory='static'), name="static")