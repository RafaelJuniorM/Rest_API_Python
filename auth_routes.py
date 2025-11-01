# Arquivo contendo as rotas relacionadas a autenticação
from fastapi import APIRouter, Depends, HTTPException
from models import Usuario
from dependencies import criar_sessao_bd
from main import bycrypt_context
from schemas import UsuarioSchema


auth_router = APIRouter(prefix="/auth" , tags=["autenticação"])

@auth_router.get("/")
async def criar_conta():
    """
    Função para autenticação de usuários
   
    """
    return {"message":"Voce está na rota de autenticação", "autenticado": False }

@auth_router.post("/criar_conta")
async def criar_conta(usuario: UsuarioSchema, session = Depends(criar_sessao_bd)):
    usuario = session.query(Usuario).filter(Usuario.email == UsuarioSchema.email).first()
    if usuario:
        #ja existe um usuário com esse email
        raise HTTPException(status_code=400, detail="E-mailç do usuário já cadastrado")
    else: 
        senha_criptografada = bycrypt_context.hash(UsuarioSchema.senha)   # criptografa a senha utilizando bcrypt
        novo_usuario = Usuario(UsuarioSchema.nome, UsuarioSchema.email, senha_criptografada, usuarioSchema.ativo, usuarioSchema.admin)

        session.add(novo_usuario)
        session.commit()
        return {"message": "Usuário criado com sucesso {usuarioSchema.email}"}  