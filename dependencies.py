# criar uma sessao com o banco de dados 
# A sessao é criada para realizar uma transação com o banco de dados
from sqlalchemy.orm import sessionmaker
from models import db

def criar_sessao_bd():
    Session = sessionmaker(bind=db)
    session = Session()
    return session