
from aiogram import Bot, Dispatcher, executor, types, filters
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram import types, Dispatcher
from aiogram.dispatcher.filters import Command
from bot.bd.connet import get_pg_connection
import asyncio
import logging


class MyStates(StatesGroup):
    wait_data = State()


async def set(message: types.Message):
   
    text = [
        "Введите через пробел сервис, логин и пароль от которого выхотите сохранить",
        "К примеру вот так",
        "telegram bob4inski 47856434"
    ]
    await message.answer('\n'.join(text))
    await MyStates.wait_data.set()


async def process_data_set(message: types.Message, state: FSMContext):
    # Получаем данные из сообщения
    del_msg_from_set = message #записываем сообщение в переменную чтобы удалить 
    splited = message.text.split()
    a = message.from_user.id
    try:
        query = f"""
        insert into users (telegram_id, service, login, password)
        values (%s, %s, %s, %s)
        returning telegram_id, service, login, password
        """
        with get_pg_connection() as pg_conn, pg_conn.cursor() as cur:
            cur.execute(query, (a,splited[0],splited[1],splited[2]))

        await message.answer('Успешно записали данные')
        await state.finish() 

    except Exception as ex:
        logging.error(repr(ex), exc_info=True)
        await message.answer('Произошла какая-то ошибка ')
        await state.finish() 
    await asyncio.sleep(15)
    await del_msg_from_set.delete() # удаляем сообщение пользователя   
     
    


def register_set(dp: Dispatcher):
    dp.register_message_handler(set, Command(['set']))
    dp.register_message_handler(process_data_set, state=MyStates.wait_data)