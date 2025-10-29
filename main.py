# aplicação principal FastAPI
from fastapi import FastAPI
app = FastAPI()

# importando as rotas
from auth_routes import auth_router
from order_routes import order_router

# incluindo as rotas na aplicação principal
app.include_router(auth_router)
app.include_router(order_router)
