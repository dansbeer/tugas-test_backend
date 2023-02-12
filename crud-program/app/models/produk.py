import sqlalchemy as sa
from app.models import Base


class Produk(Base):
    __tablename__ = 'products'

    id = sa.Column('id', sa.Integer, primary_key=True)
    nama_produk = sa.Column('nama_produk', sa.String)
    harga_produk = sa.Column('harga_produk', sa.String)
    deskripsi_produk = sa.Column('deskripsi_produk', sa.String)
    nama_penjual = sa.Column('nama_penjual', sa.String)
    rating_produk = sa.Column('rating_produk', sa.String)
    jumlah_terjual = sa.Column('jumlah_terjual', sa.String)
