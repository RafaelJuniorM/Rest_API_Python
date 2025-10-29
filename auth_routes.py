# Arquivo contendo as rotas relacionadas a autenticação
from fastapi import APIRouter

auth_router = APIRouter(prefix="/auth" , tags=["autenticação"])

@auth_router.get("/")
async def autenticar():
    """
    Função para autenticação de usuários
   
    """
    return {"message":"Voce está na rota de autenticação", "autenticado": False }

