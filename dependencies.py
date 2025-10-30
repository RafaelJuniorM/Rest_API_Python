# criar uma sessao com o banco de dados 
# A sessao é criada para realizar uma transação com o banco de dados
# será utilizado em todas as rotas que necessitam de acesso ao banco de dados

from sqlalchemy.orm import sessionmaker
from models import db

def criar_sessao_bd():
    try:
        Session = sessionmaker(bind=db) # cria uma "fabrica" de sessões com o banco de dados
        session = Session() # cria uma sessão
        yield session #yield pausa a função e retorna a sessão para ser utilizada na rota apos isso continua o codigo
    finally:
        session.close()