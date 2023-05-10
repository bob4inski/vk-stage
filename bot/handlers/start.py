from aiogram import types, Dispatcher
from aiogram.dispatcher.filters import Command


async def start(message: types.Message):
    # Отправляем приветственное сообщение
    await message.answer('Привет! Я бот.')
    await message.answer('Вся спарвка есть в команде /help')
    await message.answer('а меню доступно по этой команде /menu')
    



def register_start(dp: Dispatcher):
    dp.register_message_handler(start, Command(['start']), state='*')
