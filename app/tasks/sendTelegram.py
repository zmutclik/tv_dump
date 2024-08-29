from celery import shared_task
from sqlalchemy.orm import Session
from celery.utils.log import get_task_logger
from prettytable import PrettyTable

import requests
from datetime import datetime, date, timedelta

from app.core.database import engine_db
from app.repositories import SymbolRepository, BigVolumeRepository
from app.core.env import TELEGRAM_CHATID, TELEGRAM_TOKEN


celery_log = get_task_logger(__name__)


pesan = '''<b><u>Big Volume Detected .!</u></b>

<b>{}</b>
<code>open  : {}</code>
<code>high  : {}</code>
<code>low   : {}</code>
<code>close : {}</code>

'''


def get_pesan(db: Session, id_symbol: str):
    repo = SymbolRepository(db)
    symbol = repo.get(id_symbol)
    if symbol is None:
        return False
    _pesan = pesan.format(symbol.symbol, symbol.open, symbol.high, symbol.low, symbol.close)

    table = PrettyTable()
    table.field_names = ["days", "vol", "delta"]
    for x in range(8):
        last = repo.find(symbol.symbol, symbol.timeframe, (symbol.waktu_date - timedelta(days=x)), symbol.waktu_time)
        if last is not None:
            table.add_row([last.waktu_date.strftime("%a"), last.volume, last.volume_delta])

    _pesan = _pesan + table.get_string()
    return pesan


@shared_task(
    bind=True,
    autoretry_for=(Exception,),
    retry_backoff=True,
    retry_kwargs={"max_retries": 3},
    name="tv_dump:send_telegram",
)
def SendTelegramTasks(self, id_symbol: str):
    with engine_db.begin() as connection:
        with Session(bind=connection) as db:
            _pesan = get_pesan(db, id_symbol)
            if _pesan:
                botrespon = telegram_bot_sendtext(_pesan)
                BigVolumeRepository(db).update(id_symbol, {"message_id": botrespon["result"]["message_id"]})


@shared_task(
    bind=True,
    autoretry_for=(Exception,),
    retry_backoff=True,
    retry_kwargs={"max_retries": 3},
    name="tv_dump:update_telegram",
)
def UpdateTelegramTasks(self, id_symbol: str, message_id: int):
    with engine_db.begin() as connection:
        with Session(bind=connection) as db:
            _pesan = get_pesan(db, id_symbol)
            if _pesan:
                botrespon = telegram_bot_sendtext(_pesan, message_id)


def telegram_bot_sendtext(bot_message: str, message_id: str = None, reply_to_message_id: str = None):
    bot_token = TELEGRAM_TOKEN
    bot_chatID = TELEGRAM_CHATID

    url_param_1 = "sendMessage"
    url_param_2 = ""
    url_param_3 = ""

    if message_id is not None:
        url_param_1 = "editMessageText"
        url_param_2 = "&message_id={}".format(message_id)

    if reply_to_message_id is not None:
        url_param_1 = "sendMessage"
        url_param_2 = ""
        url_param_3 = "&reply_to_message_id={}".format(reply_to_message_id)

    send_url = "https://api.telegram.org/bot{}/{}?chat_id={}&parse_mode=html{}&text={}{}"
    send_text = send_url.format(bot_token, url_param_1, bot_chatID, url_param_2, bot_message, url_param_3)

    response = requests.get(send_text)

    return response.json()
