from sqlalchemy.orm import Session
from fastapi.exceptions import HTTPException


from app.api_models import BaseModelResponse
from app.utils.db import engine
from app.models.user import User
from app.api_models.user_model import UserModel


class GetUserResponseModel(BaseModelResponse):
    class Config:
        schema_extra = {
            'example': {
                'data': {
                    'id': 1,
                    'name': 'User'
                },
                'meta': {},
                'success': True,
                'code': 200,
                'message': 'Success'
            }
        }


async def get_user_detail(id: int):
    with Session(engine) as session:
        user = session.query(
            User
        ).filter(
            User.id == id
        ).first()

        if not user:
            raise HTTPException(404, detail='Produk tidak ditemukan')

        return GetUserResponseModel(
            data=UserModel(
                nama=user.nama,
                jabatan=user.jabatan,
                username=user.username,
                password=user.password
            )
        )
