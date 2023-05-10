from aiogram import types, Dispatcher
from aiogram.dispatcher.filters import Command
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext

from bot.bd.connet import get_pg_connection

class MyStates_start(StatesGroup):
    wait_data = State()

async def start(message: types.Message):
    # Отправляем приветственное сообщение
    await message.answer('Привет! Я бот, который умеет хранить пароли.')
    await message.answer('Вся справка есть в команде /help')
    await message.answer('А еще через какое-то время все сообщения с паролями удаляются, не пугайтесь')


    
    



def register_start(dp: Dispatcher):
    dp.register_message_handler(start, Command(['start']))
