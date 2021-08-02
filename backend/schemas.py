from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy.sql.sqltypes import TIMESTAMP

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
