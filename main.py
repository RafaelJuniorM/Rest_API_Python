# aplicação principal FastAPI
from fastapi import FastAPI
from passlib.context import CryptContext
from dotenv import load_dotenv
import os

load_dotenv()  # Carrega variáveis de ambiente do arquivo .env

SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = os.getenv("ALGORITHM")
ACCESS_TOKEN_EXPIRE_MINUTES = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES"))

app = FastAPI()

bycrypt_context = CryptContext(schemes=["bcrypt"], deprecated="auto") # Configuração para hash de senhas

# importando as rotas
from auth_routes import auth_router
from pedido_routes import pedido_router

# incluindo as rotas na aplicação principal
app.include_router(auth_router)
app.include_router(pedido_router)
