
from aiogram import  Dispatcher, types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram import types, Dispatcher
from aiogram.dispatcher.filters import Command
from bot.bd.connet import get_pg_connection
import logging






class MyStates_del_one(StatesGroup):
    wait_data = State()


async def del_one(message: types.Message):
   
    text = [
        "Введите через пробел название сервиса, логин и пароль для записи которую вы хотите удалить",
        "К примеру:",
        "telegram aboba bob4inski"
    ]
    await message.answer('\n'.join(text))
    await MyStates_del_one.wait_data.set()


async def process_data_del_one(message: types.Message, state: FSMContext):
    # Получаем данные из сообщения
    data = message.text
    splited_data = data.split(" ")
    query = "DELETE FROM users WHERE telegram_id = %s and  service = %s and login = %s and password = %s ;"
    params = (message.from_user.id, splited_data[0],splited_data[1],splited_data[2])
    try:
        with get_pg_connection() as pg_conn, pg_conn.cursor() as cur:
            cur.execute(query, params)
        answer = True      
    except Exception as ex:
        logging.error(repr(ex), exc_info=True)
        await message.answer('Произошла какая-то ошибка')
    if answer:
        await message.answer("данные были успешно удалены")
    await state.finish()


def register_dell_one(dp: Dispatcher):
    dp.register_message_handler(del_one, Command(['del_one']))
    dp.register_message_handler(process_data_del_one, state=MyStates_del_one.wait_data)