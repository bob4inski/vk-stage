
from aiogram import Bot, Dispatcher, executor, types, filters
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram import types, Dispatcher
from aiogram.dispatcher.filters import Command
from bot.bd.connet import get_pg_connection





class MyStates(StatesGroup):
    wait_data = State()


async def set(message: types.Message):
   
    text = [
        "Введите через пробел сервис, логин и пароль, анные от которого выхотите сохранить",
        "К примеру вот так",
        "```telegram bob4inski 47856434```"
    ]
    await message.answer('\n'.join(text))
    await MyStates.wait_data.set()


async def process_data(message: types.Message, state: FSMContext):
    # Получаем данные из сообщения
    data = message.text
    
    # Записываем данные в базу данных
    print('-' * 120)
    print(data)
    splited = data.split()
    a = message.from_user.id
    try:
        query = f"""
        insert into users (telegram_id, service, login, password)
        values (%s, %s, %s, %s)
        returning telegram_id, service, login, password
        """
        with get_pg_connection() as pg_conn, pg_conn.cursor() as cur:
            cur.execute(query, (a,splited[0],splited[1],splited[2]))
    except Exception as ex: 
        
        await message.answer('Данные не записаны в базу данных')


    await message.answer(data)
   
    # Сбрасываем состояние пользователя
    await state.finish()


def register_set(dp: Dispatcher):
    dp.register_message_handler(set, Command(['set']))
    dp.register_message_handler(process_data, state=MyStates.wait_data)