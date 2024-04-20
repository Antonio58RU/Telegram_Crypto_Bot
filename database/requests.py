from database.models import async_session
from database.models import User
from sqlalchemy import select
import datetime

async def set_user(tg_id):
    async with async_session() as session:
        user = await session.scalar(select(User).where(User.tg_id == tg_id))
        if not user:
            current_date = datetime.datetime.now().strftime('%d-%m-%Y')
            session.add(User(tg_id=tg_id, registr_date=current_date))
            await session.commit()
            
async def get_user(tg_id):
    async with async_session() as session:
        return await session.scalar(select(User).where(User.tg_id == tg_id))

async def update_user_premium_status(tg_id):
    async with async_session() as session:
        user = await session.scalar(select(User).where(User.tg_id == tg_id))
        user.premium = True
        await session.commit()