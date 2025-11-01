# Arquivo com as rotdas relacionadas a pedidos
from fastapi import APIRouter, Depends
from dependencies import criar_sessao_bd
from sqlalchemy.orm import Session
from schemas import PedidoSchema
from models import Pedido

pedido_router = APIRouter(prefix="/pedidos", tags=["pedidos"])

@pedido_router.get("/") 
async def pedidos():
    """
    Rota para listar pedidos. Todas as rotas pedidos precisam de autenticação.
    """
    return {"message": "Lista de pedidos"}

@pedido_router.post("/pedidos")
async def criar_pedido( pedido_schema: PedidoSchema ,session: Session =  Depends(criar_sessao_bd)):
    """
    Rota para criar um novo pedido.
    """
    novo_pedido = Pedido(usuario=pedido_schema.usuario)
    
    session.add(novo_pedido)
    session.commit()
    return {f"message": f"Pedido criado com sucesso. ID do pedido:  {novo_pedido.id}"}