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


    
    



def register_start(dp: Dispatcher):
    dp.register_message_handler(start, Command(['start']))
