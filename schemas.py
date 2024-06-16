"""Тут прописываются модели"""

from pydantic import BaseModel

from fastapi import File, UploadFile

class AddToilet(BaseModel):
    title: str 
    description: str
    pathToImg: str 
    


class Toilet(AddToilet):
    id: int


class ChoiceToilet(BaseModel):
    id: int

class DeleteToilet(BaseModel):
    id: int



class SearchToilets(BaseModel):
    title: str
    