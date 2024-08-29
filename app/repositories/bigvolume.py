from datetime import datetime
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordBearer
from app.models.bigvolume import BixVolumeTable
from app.models.symbol import SymbolTable


class BigVolumeRepository:
    def __init__(self, db_session: Session) -> None:
        self.session: Session = db_session
        self.MainTable = BixVolumeTable

    def get(self, id: str):
        return (
            self.session.query(self.MainTable)
            .filter(
                self.MainTable.id == id,
            )
            .first()
        )

    def get_opened(self, symbol: str):
        return (
            self.session.query(self.MainTable)
            .join(self.MainTable.SYMBOLS)
            .filter(self.MainTable.status_close == None, SymbolTable.symbol == symbol)
            .all()
        )

    def create(self, dataIn):
        data = self.MainTable(**dataIn)
        self.session.add(data)
        self.session.commit()
        self.session.refresh(data)
        return data

    def update(self, id: int, dataIn: dict):
        dataIn_update = dataIn if type(dataIn) is dict else dataIn.__dict__
        (
            self.session.query(self.MainTable)
            .filter(
                self.MainTable.id == id,
            )
            .update(dataIn_update)
        )
        self.session.commit()
        return self.get(id)
