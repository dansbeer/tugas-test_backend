from fastapi.exceptions import HTTPException
import sqlalchemy as sa
from sqlalchemy.orm import Session
from pydantic.main import BaseModel

from app.models.produk import Produk
from app.api_models import BaseModelResponse
from app.utils.db import engine
from app.api_models.produk_model import ProdukModel


class UpdateProdukModel(BaseModel):
    nama_produk: str
    harga_produk: str
    deskripsi_produk: str
    nama_penjual: str
    rating_produk: str
    jumlah_terjual: str


class UpdateProdukResponseModel(BaseModelResponse):
    class Config:
        schema_extra = {
            'example': {
                'data': {
                    'nama_produk': 'Laptop',
                    'harga_produk': '1000',
                    'deskripsi_produk': 'Laptop nih',
                    'nama_penjual': 'Royan',
                    'rating_produk': '4.2',
                    'jumlah_terjual': '10'
                },
                'meta': {},
                'success': True,
                'code': 200,
                'message': 'Success'
            }
        }


async def update_produk(id: int, data: UpdateProdukModel):
    with Session(engine) as session:
        produk = session.query(
            Produk
        ).filter(
            Produk.id == id
        ).first()

        if not produk:
            raise HTTPException(404, detail='Produk tidak ditemukan')

        produk.nama_produk = data.nama_produk
        produk.harga_produk = data.harga_produk
        produk.deskripsi_produk = data.deskripsi_produk
        produk.nama_penjual = data.nama_penjual
        produk.rating_produk = data.rating_produk
        produk.jumlah_terjual = data.jumlah_terjual

        session.add(produk)
        session.commit()

        return UpdateProdukResponseModel(
            data=ProdukModel(
                nama_produk=produk.nama_produk,
                harga_produk=produk.harga_produk,
                deskripsi_produk=produk.deskripsi_produk,
                nama_penjual=produk.nama_penjual,
                rating_produk=produk.rating_produk,
                jumlah_terjual=produk.jumlah_terjual
            )
        )
