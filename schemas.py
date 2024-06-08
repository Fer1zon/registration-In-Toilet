"""Тут прописываются модели"""

from pydantic import BaseModel

from fastapi import File, UploadFile

class AddToilet(BaseModel):
    title: str 
    description: str
    pathToImg: str 
    


class ToiletTable(AddToilet):
    id: int


class DeleteToilet(BaseModel):
    id: int