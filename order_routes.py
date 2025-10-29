# Arquivo com as rotdas relacionadas a pedidos
from fastapi import APIRouter

order_router = APIRouter(prefix="/orders", tags=["pedidos"])

@order_router.get("/") 
async def pedidos():
    """
    Rota para listar pedidos. Todas as rotas pedidos precisam de autenticação.
    """
    return {"message": "Lista de pedidos"}