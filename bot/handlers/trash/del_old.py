
from aiogram import  Dispatcher, types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram import types, Dispatcher
from aiogram.dispatcher.filters import Command
from bot.bd.connet import get_pg_connection
import logging






class MyStates_del_all(StatesGroup):
    wait_data = State()


async def del_all(message: types.Message):
   
    text = [
        "Введите название сервиса записи которого вы хотите удалить",
    ]
    await message.answer('\n'.join(text))
    await MyStates_del_all.wait_data.set()


async def process_data_del_all(message: types.Message, state: FSMContext):
    # Получаем данные из сообщения
    data = message.text
    query = "DELETE FROM users WHERE telegram_id = %s and  service = %s ;"
    params = (message.from_user.id, data)
    try:
        with get_pg_connection() as pg_conn, pg_conn.cursor() as cur:
            cur.execute(query, params)
        await message.answer("данные были успешно удалены")
    except Exception as ex:
        logging.error(repr(ex), exc_info=True)
        await message.answer('Произошла какая-то ошибка')
    
    await state.finish()


def register_dell_all(dp: Dispatcher):
    dp.register_message_handler(del_all, Command(['del_all']))
    dp.register_message_handler(process_data_del_all, state=MyStates_del_all.wait_data)