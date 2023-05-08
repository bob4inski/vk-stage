
from aiogram import Bot, Dispatcher, executor, types, filters
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram import types, Dispatcher
from aiogram.dispatcher.filters import Command
from bot.bd.connet import get_pg_connection
import json
import pandas as pd



class MyStates(StatesGroup):
    wait_data = State()


async def set(message: types.Message):
    await message.answer('Сейчас выведу список сервисов, которые вы записывали')
    # Устанавливаем состояние пользователя в 'wait_data'
    query = f'select service, login, password from users where telegram_id = {message.from_user.id}'
    try:

        with get_pg_connection() as pg_conn, pg_conn.cursor() as cur:
                # cur.execute(query)
                # rows = cur.fetchall()
            df = pd.read_sql_query(query, pg_conn)

        # result = json.dumps(rows,default=vars,ensure_ascii=False, indent = 2)
        
        await message.answer(df.to_string(index=True))
    except Exception as ex:
        await message.answer( {'message': repr(ex)})




def register_list(dp: Dispatcher):
    dp.register_message_handler(set, Command(['list']))
   