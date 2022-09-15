from fastapi import APIRouter

from .endpoints import orders

api_router = APIRouter(prefix='/v1')
api_router.include_router(orders.router, prefix='/orders', tags=['orders'])
