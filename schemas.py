"""Тут прописываются модели"""

from pydantic import BaseModel



class Model(BaseModel):
    test1 : int
    test2 : str