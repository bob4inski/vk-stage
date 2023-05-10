
from aiogram import Dispatcher, types
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram import types, Dispatcher
from aiogram.dispatcher.filters import Command
import logging


from bot.bd.connet import get_pg_connection
from bot.buttons.del_menu import keyboard




class MyStates_del_all(StatesGroup):
    wait_data = State()


async def del_all(message: types.Message):
    await message.answer('Сейчас выведу список сервисов, которые вы записывали, выберите какой удалить')
    # Устанавливаем состояние пользователя в 'wait_data'
    query = f'select service from users where telegram_id = {message.from_user.id} group by service;'
    services = []
    try:

        with get_pg_connection() as pg_conn, pg_conn.cursor() as cur:
            cur.execute(query)
            rows = cur.fetchall()
            services = []
            for row in rows:
                service_name = row['service']
                services.append(service_name)

        await message.answer("Выберите сервис,данные которого вы хотите удалить:", reply_markup=keyboard(services))

    except Exception as ex:
        logging.error(repr(ex), exc_info=True)
        await message.answer('Произошла какая-то ошибка')
        




def register_del_all(dp: Dispatcher):
    dp.register_message_handler(del_all, Command(['del_all']))
   