import logging
import logger
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.utils import executor
from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import  ReplyKeyboardMarkup, KeyboardButton
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters import Text

from bot.handlers.set import  register_set
from bot.handlers.list import  register_list
from bot.handlers.start import  register_start

from aiogram.dispatcher.webhook import SendMessage, DeleteMessage

import  asyncio 

API_TOKEN = '6153330849:AAFHgaZ6cQQQSuF4Io7u0_3c7HXobSQbFvI'


logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)

def register_all_middlewares(dp):
    ...


def register_all_filters(dp):
    ...


def register_all_handlers(dp):
    register_start(dp)
    register_set(dp)
    register_list(dp)



register_all_handlers(dp)




# Создаем кнопки для меню
button1 = KeyboardButton('/start')
button2 = KeyboardButton('/help')
button3 = KeyboardButton('/set')
button4 = KeyboardButton('/list')

# Создаем меню и добавляем кнопки
menu = ReplyKeyboardMarkup(resize_keyboard=True).add(button1).add(button2).add(button3).add(button4)

# Отправляем меню пользователю
@dp.message_handler(commands=['menu'])
async def start_command(message: types.Message):
    # Отправляем приветственное сообщение
    await bot.send_message(message.chat.id, 'Выберите команду:', reply_markup=menu)

@dp.message_handler(commands=['delete'])
async def delete_message(message: types.Message):
    
    history = await bot.get_chat_history(chat_id=message.chat.id)

    # Получение id всех сообщений
    message_ids = [msg.message_id for msg in history]
    # Удаление всех сообщений пользователя
    for i in message_ids:
       await bot.delete_message(chat_id = message.chat.id, message_id = i)

if __name__ == '__main__':

    executor.start_polling(dp, skip_updates=True)