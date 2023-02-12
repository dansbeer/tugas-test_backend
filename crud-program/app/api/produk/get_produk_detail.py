from sqlalchemy.orm import Session
from fastapi.exceptions import HTTPException


from app.api_models import BaseModelResponse
from app.utils.db import engine
from app.models.produk import Produk
from app.api_models.produk_model import ProdukModel


class GetProdukDetailResponseModel(BaseModelResponse):
    class Config:
        schema_extra = {
            'example': {
                'data': {
                    'id': 1,
                    'name': 'Laptop'
                },
                'meta': {},
                'success': True,
                'code': 200,
                'message': 'Success'
            }
        }


async def get_produk_detail(id: int):
    with Session(engine) as session:
        produk = session.query(
            Produk
        ).filter(
            Produk.id == id
        ).first()

        if not produk:
            raise HTTPException(404, detail='Produk tidak ditemukan')

        return GetProdukDetailResponseModel(
            data=ProdukModel(
                nama_produk=produk.nama_penjual,
                harga_produk=produk.harga_produk,
                deskripsi_produk=produk.deskripsi_produk,
                nama_penjual=produk.nama_penjual,
                rating_produk=produk.rating_produk,
                jumlah_terjual=produk.jumlah_terjual
            )
        )
