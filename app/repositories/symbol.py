from datetime import datetime, date, time
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordBearer
from app.models.symbol import SymbolTable


class SymbolRepository:
    def __init__(self, db_session: Session) -> None:
        self.session: Session = db_session
        self.MainTable = SymbolTable

    def get(self, id: str):
        return (
            self.session.query(self.MainTable)
            .filter(
                self.MainTable.id == id,
            )
            .first()
        )

    def parse_id(self, data):
        return data["symbol"] + "_" + str(data["timeframe"]) + "_" + str(int(data["waktu"].timestamp() * 1000))

    def find(self, symbol: str, timeframe: int, waktu_date: date, waktu_time: time):
        return (
            self.session.query(self.MainTable)
            .filter(
                self.MainTable.symbol == symbol,
                self.MainTable.timeframe == timeframe,
                self.MainTable.waktu_date == waktu_date,
                self.MainTable.waktu_time == waktu_time,
            )
            .order_by(self.MainTable.waktu.desc())
            .first()
        )

    def last(self, symbol: str, timeframe: int):
        return (
            self.session.query(self.MainTable)
            .filter(
                self.MainTable.symbol == symbol,
                self.MainTable.timeframe == timeframe,
            )
            .order_by(self.MainTable.waktu.desc())
            .first()
        )

    def create(self, dataIn):
        data = self.MainTable(**dataIn)
        data.id = self.parse_id(dataIn)
        data.waktu_date = data.waktu.date()
        data.waktu_time = data.waktu.time()
        self.session.add(data)
        self.session.commit()
        self.session.refresh(data)
        return data

    def update(self, id: str, dataIn: dict):
        dataIn_update = dataIn if type(dataIn) is dict else dataIn.__dict__
        (
            self.session.query(self.MainTable)
            .filter(
                self.MainTable.id == id,
            )
            .update(dataIn_update)
        )
        self.session.commit()
