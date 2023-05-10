from aiogram import types, Dispatcher
from aiogram.dispatcher.filters import Command
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext

from bot.bd.connet import get_pg_connection

class MyStates_start(StatesGroup):
    wait_data = State()

async def start(message: types.Message):
    # Отправляем приветственное сообщение
    await message.answer('Привет! Я бот.')
    await message.answer('Вся справка есть в команде /help')
    # await message.answer('А сейчас предлагаю придумать пароль для удаления и изменения паролей')

    # await MyStates_start.wait_data.set()

# async def process_data_set(message: types.Message, state: FSMContext):
#     data = message.text
#     query = "insert into client(id,password) values (%s,%s)"
#     params = (message.from_user.id, data)

    
    



def register_start(dp: Dispatcher):
    dp.register_message_handler(start, Command(['start']))
    # dp.register_message_handler(process_data_set, state=MyStates_start.wait_data)