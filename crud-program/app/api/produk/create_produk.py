from sqlalchemy.orm import Session
from pydantic import BaseModel
from app.api_models import BaseModelResponse
from app.models.produk import Produk
from app.utils.db import engine


class CreateProdukData(BaseModel):
    nama_produk: str
    harga_produk: str
    deskripsi_produk: str
    nama_penjual: str
    rating_produk: str
    jumlah_terjual: str


class CreateProdukResponseModel(BaseModelResponse):
    class Config:
        schema_extra = {
            'example': {
                'data': {
                    'id': 1,
                    'url': '/api/v1/produk/1'
                },
                'meta': {},
                'success': True,
                'code': 200,
                'message': 'Success'
            }
        }


async def create_produk(data: CreateProdukData):

    with Session(engine) as session:
        produk = Produk(
            nama_produk=data.nama_produk,
            harga_produk=data.harga_produk,
            deskripsi_produk=data.deskripsi_produk,
            nama_penjual=data.nama_penjual,
            rating_produk=data.rating_produk,
            jumlah_terjual=data.jumlah_terjual
        )
        session.add(produk)
        session.commit()

        return CreateProdukResponseModel(
            data={
                'id': produk.id,
                'url': f'/api/v1/produk/{produk.id}'  # HATEOAS
            }
        )
