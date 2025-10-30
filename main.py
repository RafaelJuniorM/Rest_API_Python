# aplicação principal FastAPI
from fastapi import FastAPI
from passlib.context import CryptContext
from dotenv import load_dotenv
import os

load_dotenv()  # Carrega variáveis de ambiente do arquivo .env

SECRET_KEY = os.getenv("SECRET_KEY")

app = FastAPI()

bycrypt_context = CryptContext(schemes=["bcrypt"], deprecated="auto") # Configuração para hash de senhas

# importando as rotas
from auth_routes import auth_router
from order_routes import order_router

# incluindo as rotas na aplicação principal
app.include_router(auth_router)
app.include_router(order_router)
