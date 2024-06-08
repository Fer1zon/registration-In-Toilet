"""Тут прописываются команды в базу данных"""


from sqlalchemy import select, delete
from schemas import AddToilet, DeleteToilet
from database.database import new_session, ToiletTable




class Toilets():
    @classmethod
    async def addToilet(self, data:AddToilet):
        async with new_session() as session:
            toiletDict = data.model_dump()

            newToilet = ToiletTable(**toiletDict)

            session.add(newToilet)

            await session.flush()
            await session.commit()

            return newToilet.id
        
    @classmethod
    async def checkAvail(self, id: int):
        async with new_session() as session:
            query = select(ToiletTable).where(ToiletTable.id == id)
            result = await session.execute(query)

            result = result.first()
            
            
            if result is None:
                return False 
            
            else: 
                return True
            

    @classmethod
    async def deleteToilet(self, id: int):
        async with new_session() as session:
            
            
            query1 = delete(ToiletTable).where(ToiletTable.id == id)
            await session.execute(query1)

            await session.commit()

    @classmethod
    async def allToilets(self):
        pass

