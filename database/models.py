from sqlalchemy import BigInteger, String
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy.ext.asyncio import AsyncAttrs, async_sessionmaker, create_async_engine

engine = create_async_engine(url='sqlite+aiosqlite:///db.sqlite3')

async_session = async_sessionmaker(engine)

class Base(AsyncAttrs, DeclarativeBase):
    pass

class User(Base):
    __tablename__ = 'users'
    
    id: Mapped[int] = mapped_column(primary_key=True)
    tg_id = mapped_column(BigInteger)
    premium: Mapped[bool] = mapped_column(default=False)
    registr_date: Mapped[str] = mapped_column(String(15))
    language: Mapped[str] = mapped_column(String(5), default='ru')
    
class Cryptocurrency(Base):
    __tablename__ = 'cryptocurrencies24'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(6))
    price1: Mapped[str] = mapped_column(String(30))
    price2: Mapped[str] = mapped_column(String(30))  
    
    
async def async_main():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

