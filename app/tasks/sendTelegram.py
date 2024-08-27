from celery import shared_task
from sqlalchemy.orm import Session
from celery.utils.log import get_task_logger

import requests

from app.core.database import engine_db
from app.repositories import SymbolRepository
from app.core.env import TELEGRAM_CHATID, TELEGRAM_TOKEN


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
            symbol = SymbolRepository(db).get(id_symbol)
            if symbol is not None:
                pesan = """--Big Volume Detected .!-- \n\n *{}* \n`open  : {}`\n`high  : {}`\n`low   : {}`\n`close : {}`\n`volume: {}` \n\n`volume MA    : {}`\n`volume delta : {}` """
                botrespon = telegram_bot_sendtext(
                    pesan.format(
                        symbol.symbol,
                        symbol.open,
                        symbol.high,
                        symbol.low,
                        symbol.close,
                        symbol.volume,
                        symbol.volume_ma,
                        symbol.volume_delta,
                    ),
                )


def telegram_bot_sendtext(bot_message):
    bot_token = TELEGRAM_TOKEN
    bot_chatID = TELEGRAM_CHATID
    send_text = (
        "https://api.telegram.org/bot"
        + bot_token
        + "/sendMessage?chat_id="
        + bot_chatID
        + "&parse_mode=Markdown&text="
        + bot_message
    )

    response = requests.get(send_text)

    return response.json()
