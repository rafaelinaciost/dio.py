from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Cliente(Base):
    __tablename__ = 'clientes'
    id = Column(Integer, primary_key=True)
    nome = Column(String)
    cpf = Column(String, unique = True)
    endereco = Column(String)
    contas = relationship('Conta', back_populates='cliente')

class Conta(Base):
    __tablename__ = 'contas'
    id = Column(Integer, primary_key=True)
    tipo = Column(String)
    agencia = Column(String)
    numero = Column(String, unique=True)
    id_cliente = Column(Integer, ForeignKey('clientes.id'))
    saldo = Column(Integer)
    cliente = relationship('Cliente', back_populates='contas')

# Configurar a conexão ao SQLite
engine = create_engine('sqlite:///banco_relacional.db')
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)