from sqlalchemy import select, update, delete, func
from models import async_session, User, Task
from pydantic import BaseModel, ConfigDict
from typing import list


class TaskSchema(BaseModel):
    id: int
    title: str
    completed: bool
    user: int

    model_config = ConfigDict(from_attributes=True)

async def add_user(tg_id):
    async with async_session() as session:
        uer = await session.scalar(select(User).where(User.tg_id == td_id))
        if user:
            return user

        new_user = User(tg_id=tg_id)
        session.add(new_user)
        await session.commit()
        await session.refresh(new_user)
        return new_user



async def get_tasks(user_id):
    async with async_session() as session:
        tasks = await session.scalars(
            select(Task).where(Task.user == user_id, Task.complited == False)
        )

        serialized_tasks = [
            TaslSchema.model_validate(t).model_dump for t in tasks
        ]

        return serialized_tasks


async def get_complited_tasks_count(user_id):
    async with async_session() as session:
        return await session.scalar(select(func.count(Task.id)).where(Task.completed == True))
        