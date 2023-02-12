from fastapi.exceptions import HTTPException
import sqlalchemy as sa
from sqlalchemy.orm import Session
from pydantic.main import BaseModel

from app.models.user import User
from app.api_models import BaseModelResponse
from app.utils.db import engine
from app.api_models.user_model import UserModel


class UpdateUserModel(BaseModel):
    nama: str
    jabatan: str
    username: str
    password: str


class UpdateUserResponseModel(BaseModelResponse):
    class Config:
        schema_extra = {
            'example': {
                'data': {
                    'nama': 'User',
                    'jabatan': 'developer',
                    'username': 'user',
                    'password': 'password'
                },
                'meta': {},
                'success': True,
                'code': 200,
                'message': 'Success'
            }
        }


async def update_user(id: int, data: UpdateUserModel):
    with Session(engine) as session:
        user = session.query(
            User
        ).filter(
            User.id == id
        ).first()

        if not user:
            raise HTTPException(404, detail='User tidak ditemukan')

        user.nama = data.nama
        user.jabatan = data.jabatan
        user.username = data.username
        user.password = data.password

        session.add(user)
        session.commit()

        return UpdateUserResponseModel(
            data=UserModel(
                nama=user.nama,
                jabatan=user.jabatan,
                username=user.username,
                password=user.password
            )
        )
