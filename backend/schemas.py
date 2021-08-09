from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy.sql.functions import current_timestamp
from sqlalchemy.sql.sqltypes import TIMESTAMP, Boolean

Base = declarative_base()


class Users(Base):
    __tablename__ = "usuario"
    id = Column(Integer, primary_key=True)
    tw_id = Column(Integer)
    tw_handle = Column(Integer)
    tw_token = Column(Integer)
    apelido_usuario = Column(Integer)
    email = Column(String)
    registrado_em = Column(TIMESTAMP)
    preferencias_id = Column(
        ForeignKey("preferencias.id", name="usuario_preferencias_id_fk"), nullable=False, index=True
    )


class Preferences(Base):
    __tablename__ = "preferencias"

    id = Column(Integer, primary_key=True)
    integ_anotacoes = Column(Integer)
    integ_tarefas = Column(Integer)
    integ_lembretes = Column(Integer)
    integ_email = Column(Integer)
    integ_push = Column(Integer)


class RegisterType(Base):
    __tablename__ = "tipo_registro"

    id = Column(Integer, primary_key=True)
    nome = Column(String, nullable=False)


class Register(Base):
    __tablename__ = "registro"

    id = Column(Integer, primary_key=True)
    tweet_content = Column(String)
    data_hora_registro = Column(TIMESTAMP, nullable=True, default=current_timestamp)
    tweet_id = Column(String, nullable=False, unique=True)
    parent_tweet_id = Column(Integer, nullable=True)

    usuario_id = Column(ForeignKey("usuario.id", name="registro_usuario_fk"), nullable=False, index=True)
    tipo_registro = Column(ForeignKey("tipo_registro.id", name="registro_tipo_fk"), nullable=False)


class TaskList(Base):
    __tablename__ = "lista_tarefas"

    id = Column(Integer, primary_key=True)
    completo = Column(Integer, nullable=False, default=0)

    registro_id = Column(ForeignKey("registro.id", name="lista_tarefas_registro_id_fk"), nullable=False, index=True)


class Task(Base):
    __tablename__ = "tarefa"

    id = Column(Integer, primary_key=True)
    texto_tarefa = Column(String, nullable=True)
    completo = Column(Boolean, nullable=False, default=False)
    lista_id = Column(ForeignKey("lista_tarefas.id", name="tarefa_lista_id_fk"), nullable=False, index=True)
