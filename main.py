from contextlib import asynccontextmanager

from fastapi import FastAPI


from database.database import createTables

from scheduler.main import scheduler

from fastapi.staticfiles import StaticFiles


from routers.mainSheet import router as mainRouter
from routers.toiletManagement.main import router as toiletManagementRouter
from routers.toiletManagement.search import router as searchRouter






@asynccontextmanager
async def lifespan(app: FastAPI):
    scheduler.start()
    await createTables()
    yield








app = FastAPI(lifespan=lifespan)
app.mount('/static', app=StaticFiles(directory='static'), name="static")
app.include_router(mainRouter)
app.include_router(toiletManagementRouter)  
app.include_router(searchRouter)     