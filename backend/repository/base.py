from os import environ
from typing import Any, Dict

from sqlalchemy import Table, create_engine
from sqlalchemy.orm import Session, sessionmaker

DATABASE_URL: str = environ.get("CLEARDB_DATABASE_URL", "mysql://root:1234@127.0.0.1:3306/nidus")


class BaseRepository:
    def __init__(self):
        engine = create_engine(DATABASE_URL)
        Session = sessionmaker(bind=engine)
        self.session = Session()

    def insert(self, table: Table, values: Dict[str, Any]) -> int:
        obj_to_insert = table(**values)
        self.session.add(obj_to_insert)
        self.session.commit()
        return obj_to_insert.id

    def update(self, table: Table, row_id: int, values: Dict[str, Any]) -> None:
        self.session.query(table).filter(table.id == row_id).update(values)
        self.session.commit()
