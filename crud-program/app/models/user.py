import sqlalchemy as sa
from app.models import Base


class User(Base):
    __tablename__ = 'users'

    id = sa.Column('id', sa.Integer, primary_key=True)
    nama = sa.Column('nama', sa.String)
    jabatan = sa.Column('jabatan', sa.String)
    username = sa.Column('username', sa.String)
    password = sa.Column('password', sa.String)
