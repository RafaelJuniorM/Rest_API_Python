# arquivo para definir os modelos de dados
from sqlalchemy import create_engine, Column, Integer, String, Boolean, Float, ForeignKey 
from sqlalchemy.orm import declarative_base
from sqlalchemy_utils.types  import ChoiceType
# cria a conexao com o banco de dados
db = create_engine("sqlite:///banco.db")

# cria a base do bd permite a criação tabela no bd 
Base = declarative_base()

# criar as classses/tabelas do banco
class Usuario(Base):
    __tablename__ = "usuarios" # definindo o nome da tabela 

    # definindo as colunas da tabela
    id = Column("id", Integer, primary_key=True, autoincrement=True) # defini o nome da coluna do banco e o tipo de dado 
    nome = Column("nome", String(100))
    email = Column("email", String(100), nullable=False)
    senha = Column("senha", String(100))
    ativo = Column("ativo", Boolean, default=True)
    admin = Column("admin", Boolean, default=False)

    # quando iniciar a criação do novo usuario qual valores serão passados
    def __init__(self, nome, email, senha, ativo=True, admin=False):
        self.nome = nome
        self.email = email
        self.senha = senha
        self.ativo = ativo
        self.admin = admin

class Pedido(Base):
    __tablename__ ="pedidos"

    #STATUS_PEDIDOS = (
     #   ("PENDENTE", "Pendente"),
      #  ("CANCELADO", "CANCELADO"),
       # ("FINALIZADO", "FINALIZADO"),
    #)

    id  = Column("id", Integer, primary_key=True, autoincrement=True)
    status = Column("status", String) #ChoiceType(STATUS_PEDIDOS))
    usuario = Column("usuario", ForeignKey("usuarios.id"))
    preco = Column("preco", Float)
    #itens  = Column()

    def __init__(self, usuario, status="PENDENTE", preco=0):
        self.usuario = usuario
        self.preco = preco
        self.status = status

class ItemPedido(Base):
    __tablename__ = "itens_pedido"

    id = Column("id", Integer, primary_key=True, autoincrement=True)
    pedido = Column("pedido", ForeignKey("pedidos.id"))
    sabor = Column("sabor", String(100))
    tamanho = Column("tamanho", String(50))
    quantidade = Column("quantidade", Integer)
    preco_unitario = Column("preco_unitario", Float)

    def __init__(self, pedido, produto, quantidade, preco_unitario, tamanho):
        self.pedido = pedido
        self.produto = produto
        self.quantidade = quantidade
        self.preco_unitario = preco_unitario
        self.tamanho = tamanho

# executa a criação dos metadados do bd (cria efetivamente o banco de dados)