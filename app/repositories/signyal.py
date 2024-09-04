from datetime import datetime
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordBearer
from app.models.signyals import SignyalTable


class SignyalRepository:
    def __init__(self, db_session: Session) -> None:
        self.session: Session = db_session
        self.MainTable = SignyalTable

    def get(self, id: str):
        return (
            self.session.query(self.MainTable)
            .filter(
                self.MainTable.id == id,
            )
            .first()
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
