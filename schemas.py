# schemas é 
from pydantic import BaseModel
from typing import Optional 

class UsuarioSchema(BaseModel):
    nome: str
    email: str
    senha: str
    ativo: Optional[bool]
    admin: Optional[bool]  

    class Config: # converte para o formalo de class
        from_attributes = True

class LoginSchema(BaseModel):
    email: str
    senha: str

    class Config:
        from_attributes = True


class PedidoSchema(BaseModel): # oque o usuario precisa passar para que ele possa criar um pedido
    usuario: int

    class Config:
        from_attributes = True