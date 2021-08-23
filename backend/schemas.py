from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import joinedload, lazyload, relationship
from sqlalchemy.sql.functions import now, current_timestamp
from sqlalchemy.sql.sqltypes import TIMESTAMP, Boolean

Base = declarative_base()


class User(Base):
    __tablename__ = "user"
    id = Column(String, primary_key=True)
    tw_id = Column(String)
    tw_name = Column(String)
    tw_access_token = Column(String)
    tw_access_token_verifier = Column(String)
    tw_profile_picture = Column(String)
    tw_email = Column(String)
    created_at = Column(TIMESTAMP, server_default=now())
    settings = relationship("Settings", backref="user")


class Settings(Base):
    __tablename__ = "settings"
    id = Column(String, primary_key=True)
    note = Column(Boolean, default=True)
    task = Column(Boolean, default=True)
    reminder = Column(Boolean, default=True)
    email = Column(Boolean, default=False)
    push = Column(Boolean, default=True)
    user_id = Column(String, ForeignKey("user.id"),  unique=True)

class Session(Base):
    __tablename__ = "session"
    id = Column(String, primary_key=True)
    user_id = Column(ForeignKey("user.id", name="session_user_fk"), nullable=False, index=True)
    access_token = Column(String)
    active = Column(Boolean, default=True)
    created_at = Column(TIMESTAMP, server_default=now())
    end_at = Column(TIMESTAMP)

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
