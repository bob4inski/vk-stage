
from aiogram import  Dispatcher, types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram import types, Dispatcher
from aiogram.dispatcher.filters import Command
from bot.bd.connet import get_pg_connection
import logging
import pandas as pd





class MyStates_get(StatesGroup):
    wait_data = State()


async def get(message: types.Message):
   
    text = [
        "Введите название сервиса от которого хотите получить log pass",
        "К примеру вот так",
        "telegram",
        "если не помнишь какие сохранял, то можно использовать команду /list"
    ]
    await message.answer('\n'.join(text))
    await MyStates_get.wait_data.set()


async def process_data_get(message: types.Message, state: FSMContext):
    # Получаем данные из сообщения
    data = message.text
    query = "select login, password from users where telegram_id = %s and service = %s"
    params = (message.from_user.id, data)
    try:

        with get_pg_connection() as pg_conn, pg_conn.cursor() as cur:
            df = pd.read_sql_query(query, pg_conn,params=params)
            if len(df):
                await message.answer(df.to_string(index=False))
            else:
                await message.answer('у вас нет сохранненых паролей для этого сервиса')
    except Exception as ex:
        logging.error(repr(ex), exc_info=True)
        await message.answer('Произошла какая-то ошибка')
    await state.finish()


def register_get(dp: Dispatcher):
    dp.register_message_handler(get, Command(['get']))
    dp.register_message_handler(process_data_get, state=MyStates_get.wait_data)