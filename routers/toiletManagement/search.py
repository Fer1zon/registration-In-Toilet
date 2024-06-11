from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse

from fastapi.templating import Jinja2Templates

from schemas import SearchToilets

from repository import Toilets




router = APIRouter(prefix="/toilet")


@router.post("/search")
async def searchToilet(data : SearchToilets):
    result = await Toilets.getSearchToilets(data.title)
    return result
