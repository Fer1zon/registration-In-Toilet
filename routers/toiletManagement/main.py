


from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse

from fastapi.templating import Jinja2Templates

from schemas import AddToilet, DeleteToilet

from repository import Toilets




router = APIRouter(prefix="/toilet")


@router.post("/add")
async def addToilet(toilet: AddToilet):
    newToilet = AddToilet(title=toilet.title, description=toilet.description, pathToImg=toilet.pathToImg)
    toiletId = await Toilets.addToilet(newToilet)

    return {
        "ok" : True,
        "toiletId" : toiletId
            }



@router.post("/delete")
async def deleteToilet(toilet: DeleteToilet):
    response = await Toilets.checkAvail(toilet.id)

    if response:
        await Toilets.deleteToilet(toilet.id)

        return {
            "ok" : True,
            "toiletId" : toilet.id,
            "reason" : None
            }
    
    else:
        return {
            "ok" : False,
            "toiletId" : toilet.id,
            "reason" : "Туалета с таким ID не существует"
            }
    

@router.get("")
async def getAllToilets():
    return {
        "data" : await Toilets.allToilets()
    }

