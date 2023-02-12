from fastapi.exceptions import HTTPException
import sqlalchemy as sa
from sqlalchemy.orm import Session

from app.models.user import User
from app.utils.db import engine


async def delete_user(id: int):
    with Session(engine) as session:
        user = session.query(
            User
        ).filter(
            User.id == id
        ).first()

        if not user:
            raise HTTPException(404, detail='User tidak ditemukan')

        user.id = id

        session.delete(user)
        session.commit()

        return ''
