from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse

from fastapi.templating import Jinja2Templates

from repository import Toilets

templates = Jinja2Templates(directory="templates")

router = APIRouter()


@router.get("/")
async def mainSheet(request:Request):
    response = await Toilets.allToilets()
    
    return templates.TemplateResponse(
        "assets.html",
        {
            "request": request,
            #"content" : response
            
        }
)




