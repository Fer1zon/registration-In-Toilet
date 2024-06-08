from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from sqlalchemy.orm import DeclarativeBase, mapped_column, Mapped

dbEngine = create_async_engine(
    "sqlite+aiosqlite:///database/dataBase.db"
)


new_session = async_sessionmaker(dbEngine, expire_on_commit=False)

class Model(DeclarativeBase):
    pass

class ToiletTable(Model):
    __tablename__ = "toilet"

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str]
    description: Mapped[str]
    pathToImg: Mapped[str]







async def createTables():
    async with dbEngine.begin() as conn:
        await conn.run_sync(Model.metadata.create_all)