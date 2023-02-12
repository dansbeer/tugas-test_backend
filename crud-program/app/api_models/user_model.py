from pydantic import BaseModel


class UserModel(BaseModel):
    nama: str
    jabatan: str
    username: str
    password: str
