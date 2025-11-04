# Arquivo contendo as rotas relacionadas a autenticação
from fastapi import APIRouter, Depends, HTTPException
from models import Usuario
from dependencies import criar_sessao_bd
from main import bycrypt_context, SECRET_KEY, ALGORITHM, ACCESS_TOKEN_EXPIRE_MINUTES
from schemas import UsuarioSchema, LoginSchema
from sqlalchemy.orm import Session
from datetime import datetime, timedelta, timezone
from jose import jwt, JWTError


auth_router = APIRouter(prefix="/auth" , tags=["autenticação"])

def criar_token(id_usuairo, duracao_token=timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)):
    data_expericao = datetime.now(timezone.utc) + duracao_token
    dicionario_informacoes = {
        "sub": id_usuairo,
        "exp": data_expericao.timestamp()  # Convertendo para timestamp
    }
    jwt_codificado = jwt.encode(dicionario_informacoes, SECRET_KEY, ALGORITHM)
    return jwt_codificado

def verificar_token(token, session:  Session = Depends(criar_sessao_bd)):
    usuario = session.query(Usuario).filter(Usuario.id ==1).first()
    return usuario

def autenticar_usuario(email, senha, session):
    usuario = session.query(Usuario).filter(Usuario.email == email).first()
    if not usuario:
        return False
    if not bycrypt_context.verify(senha, usuario.senha):
        return False
    return usuario


@auth_router.get("/")
async def criar_conta():
    """
    Função para autenticação de usuários
   
    """
    return {"message":"Voce está na rota de autenticação", "autenticado": False }

@auth_router.post("/criar_conta")
async def criar_conta(usuario_schema: UsuarioSchema, session: Session = Depends(criar_sessao_bd)):
    usuario = session.query(Usuario).filter(Usuario.email == usuario_schema.email).first()
    if usuario:
        #ja existe um usuário com esse email
        raise HTTPException(status_code=400, detail="E-mail do usuário já cadastrado")
    else: 
        senha_criptografada = bycrypt_context.hash(usuario_schema.senha)   # criptografa a senha utilizando bcrypt
        novo_usuario = Usuario(usuario_schema.nome, usuario_schema.email, senha_criptografada, usuario_schema.ativo, usuario_schema.admin)

        session.add(novo_usuario)
        session.commit()
        return {"message": f"Usuário criado com sucesso {novo_usuario.email}"} 
    
# processo de login 
# login -> receber email e senha -> gerar token JWT -> retornar token para o usuario
# cada rota precisa receber o token JWT 

@auth_router.post("/login")
async def login(login_schema:LoginSchema, session: Session = Depends(criar_sessao_bd)):
    # verificar se o usuário existe no banco de dados
    usuario = autenticar_usuario(login_schema.email, login_schema.senha, session) # sempre buscar algo no bd usa o session.query("nome da tabela")
    if not usuario:
        raise HTTPException(status_code=400, detail="Usuário não encontrado ou credenciais inválidas")
    else:
        acsess_token = criar_token(usuario.id) # duração curta 
        refresh_token = criar_token(usuario.id, duracao_token=timedelta(days=7)) 
        return {
            "access_token": acsess_token, 
            "refresh_token": refresh_token,
            "token_type": "bearer"}
    

@auth_router.post("/refresh")
async def use_refresh_token(token):
    usuario = verificar_token(token)
    access_token = criar_token(usuario.id)
    return{
        "access_token": access_token,
        "token_type": "bearer"
    }