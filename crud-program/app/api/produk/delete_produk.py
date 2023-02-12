from fastapi.exceptions import HTTPException
import sqlalchemy as sa
from sqlalchemy.orm import Session

from app.models.produk import Produk
from app.utils.db import engine


async def delete_produk(id: int):
    with Session(engine) as session:
        produk = session.query(
            Produk
        ).filter(
            Produk.id == id
        ).first()

        if not produk:
            raise HTTPException(404, detail='Produk tidak ditemukan')

        produk.id = id

        session.delete(produk)
        session.commit()

        return ''
