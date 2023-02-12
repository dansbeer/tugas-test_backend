from sqlalchemy.orm import Session
from pydantic import BaseModel
from app.api_models import BaseModelResponse
from app.models.user import User
from app.utils.db import engine


class CreateUserData(BaseModel):
    nama: str
    jabatan: str
    username: str
    password: str


class CreateUserResponseModel(BaseModelResponse):
    class Config:
        schema_extra = {
            'example': {
                'data': {
                    'id': 1,
                    'url': '/api/v1/user/1'
                },
                'meta': {},
                'success': True,
                'code': 200,
                'message': 'Success'
            }
        }


async def create_user(data: CreateUserData):

    with Session(engine) as session:
        user = User(
            nama=data.nama,
            jabatan=data.jabatan,
            username=data.username,
            password=data.password,
        )
        session.add(user)
        session.commit()

        return CreateUserResponseModel(
            data={
                'id': user.id,
                'url': f'/api/v1/user/{user.id}'  # HATEOAS
            }
        )
