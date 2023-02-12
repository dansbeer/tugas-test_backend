from pydantic import BaseModel


class ProdukModel(BaseModel):
    nama_produk: str
    deskripsi_produk: str
    nama_penjual: str
    rating_produk: str
    jumlah_terjual: str
