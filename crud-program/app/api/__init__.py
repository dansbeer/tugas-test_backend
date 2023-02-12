from fastapi import APIRouter

from app.api.user.create_user import create_user, CreateUserResponseModel
from app.api.user.get_user import get_user_detail, GetUserResponseModel
from app.api.user.update_user import update_user, UpdateUserResponseModel
from app.api.user.delete_user import delete_user

from app.api.user.login import LoginUser, LoginResponseModel

from app.api.produk.create_produk import create_produk, CreateProdukResponseModel
from app.api.produk.get_produk_detail import get_produk_detail, GetProdukDetailResponseModel
from app.api.produk.update_produk import update_produk, UpdateProdukResponseModel
from app.api.produk.delete_produk import delete_produk

api_router = APIRouter(prefix='/api')

# LOGIN
api_router.add_api_route('/v1/user/{username}/{password}',
                         LoginUser,
                         methods=['GET'],
                         tags=['Login'],
                         response_model=LoginResponseModel
                         )


# USER
api_router.add_api_route('/v1/user', create_user,
                         methods=['POST'],
                         tags=['User'],
                         response_model=CreateUserResponseModel
                         )


api_router.add_api_route('/v1/user/{id}',
                         get_user_detail,
                         methods=['GET'],
                         tags=['User'],
                         response_model=GetUserResponseModel
                         )

api_router.add_api_route('/v1/user/{id}',
                         update_user,
                         methods=['PUT'],
                         tags=['User'],
                         response_model=UpdateUserResponseModel
                         )

api_router.add_api_route('/v1/user/{id}',
                         delete_user,
                         methods=['DELETE'],
                         tags=['User'],
                         status_code=204
                         )

# PRODUK

api_router.add_api_route('/v1/produk', create_produk,
                         methods=['POST'],
                         tags=['Produk'],
                         response_model=CreateProdukResponseModel
                         )

api_router.add_api_route('/v1/produk/{id}',
                         get_produk_detail,
                         methods=['GET'],
                         tags=['Produk'],
                         response_model=GetProdukDetailResponseModel
                         )

api_router.add_api_route('/v1/produk/{id}',
                         update_produk,
                         methods=['PUT'],
                         tags=['Produk'],
                         response_model=UpdateProdukResponseModel
                         )

api_router.add_api_route('/v1/produk/{id}',
                         delete_produk,
                         methods=['DELETE'],
                         tags=['Produk'],
                         status_code=204
                         )
