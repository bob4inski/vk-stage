
from aiogram import Bot, Dispatcher, executor, types, filters
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram import types, Dispatcher
from aiogram.dispatcher.filters import Command
from bot.bd.connet import get_pg_connection
from bot.buttons.get_menu import get_keyboard
import logging



class MyStates(StatesGroup):
    wait_data = State()


async def get(message: types.Message):
    await message.answer('Сейчас выведу список сервисов, которые вы записывали')
    query = f'select service from users where telegram_id = {message.from_user.id}'
    try:

        with get_pg_connection() as pg_conn, pg_conn.cursor() as cur:
            cur.execute(query)
            rows = cur.fetchall()
            services = []
            for row in rows:
                service_name = row['service']
                services.append(service_name)  
        if len(services):
            await message.answer("Выберите сервис,данные которого вы хотите посмотреть:(через минуту сообщение с паролем удалится)", reply_markup=get_keyboard(services))
        else:
            await message.answer("У вас нет сохраненных паролей")
        # result = json.dumps(rows,default=vars,ensure_ascii=False, indent = 2)
        
    except Exception as ex:
        logging.error(repr(ex), exc_info=True)
        await message.answer('Произошла какая-то ошибка')
        

def register_get(dp: Dispatcher):
    dp.register_message_handler(get, Command(['get']))

   