from sqlalchemy.orm import Session
from fastapi.exceptions import HTTPException


from app.api_models import BaseModelResponse
from app.utils.db import engine
from app.models.user import User
from app.api_models.user_model import UserModel


class LoginResponseModel(BaseModelResponse):
    class Config:
        schema_extra = {
            'example': {
                'data': {
                    'message': 'Success Login'
                },
                'meta': {},
                'success': True,
                'code': 200,
                'message': 'Success'
            }
        }


async def LoginUser(username: str, password: str):
    with Session(engine) as session:
        user = session.query(
            User
        ).filter(
            User.username == username,
            User.password == password
        ).first()

        if not user:
            raise HTTPException(404, detail='User Tidak ditemukan')

        return LoginResponseModel(
            data={
                'message': 'Success Login'
            }

        )
