from datetime import datetime
from typing import List
from pydantic import BaseModel


class ProdukBaseSchema(BaseModel):
    id: str | None = None
    kode_produk: str
    nama_produk: str
    harga: int
    jumlah: int
    status: int

    class Config:
        orm_mode = True
        allow_population_by_field_name = True
        arbitrary_types_allowed = True


class ListProdukResponse(BaseModel):
    status: str
    result: int
    notes: List[ProdukBaseSchema]
