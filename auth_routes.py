# Arquivo contendo as rotas relacionadas a autenticação
from fastapi import APIRouter, Depends
from models import Usuario
from dependencies import criar_sessao_bd

auth_router = APIRouter(prefix="/auth" , tags=["autenticação"])

@auth_router.get("/")
async def criar_conta():
    """
    Função para autenticação de usuários
   
    """
    return {"message":"Voce está na rota de autenticação", "autenticado": False }

@auth_router.post("/criar_conta")
async def criar_conta(email: str, senha: str, nome: str, session = Depends(criar_sessao_bd)):
    usuario = session.query(Usuario).filter(Usuario.email == email).first()
    if usuario:
        #ja existe um usuário com esse email
        return {"message": "Já existe Usuário criado com esse email"}
    else: 
        novo_usuario = Usuario(nome, email, senha)
        session.add(novo_usuario)
        session.commit()
        return {"message": "Usuário criado com sucesso"}