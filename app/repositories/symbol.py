from datetime import datetime
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordBearer


class SymbolRepository:
    def __init__(self, db_session: Session, MainTable) -> None:
        self.session: Session = db_session
        self.MainTable = MainTable

    def get(self, waktu: int):
        return (
            self.session.query(self.MainTable)
            .filter(
                self.MainTable.waktu == waktu,
            )
            .first()
        )

    def last(self):
        return (
            self.session.query(self.MainTable)
            .order_by(self.MainTable.waktu.desc())
            .first()
        )

    def create(self, dataIn):
        data = self.MainTable(**dataIn)
        self.session.add(data)
        self.session.commit()
        self.session.refresh(data)
        return data

    def update(self, waktu: datetime, dataIn: dict):
        dataIn_update = dataIn if type(dataIn) is dict else dataIn.__dict__
        (
            self.session.query(self.MainTable)
            .filter(
                self.MainTable.waktu == waktu,
            )
            .update(dataIn_update)
        )
        self.session.commit()
