import logging
import  asyncio 
import pandas as pd
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.utils import executor
from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import  ReplyKeyboardMarkup, KeyboardButton
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters import Text

from bot.handlers.set import  register_set
from bot.handlers.start import  register_start
from bot.handlers.get import  register_get
from bot.handlers.help import  register_help
from bot.handlers.del_all import register_del_all
from bot.handlers.del_one import register_del_one
from bot.bd.connet import get_pg_connection



API_TOKEN = '6153330849:AAFHgaZ6cQQQSuF4Io7u0_3c7HXobSQbFvI'


logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)

def register_all_middlewares(dp):
    ...


def register_all_filters(dp):
    ...

#функции которые я импортирую из разных файлов чтобы все не писать в 1 файле
def register_all_handlers(dp):
    register_start(dp)
    register_set(dp)
    register_get(dp)
    register_help(dp)
    register_del_one(dp)
    register_del_all(dp)




register_all_handlers(dp)


@dp.callback_query_handler(lambda c: c.data and c.data.startswith('item_'))
async def process_callback_item(callback_query: types.CallbackQuery):
    # Получаем значение элемента из callback_data
    item = callback_query.data.split('_')[1]
    # Отправляем сообщение с выбранным элементом
    query = "DELETE FROM users WHERE telegram_id = %s and  service = %s ;"
    params = (callback_query.from_user.id, item)
    try:
        with get_pg_connection() as pg_conn, pg_conn.cursor() as cur:
            cur.execute(query, params)
        answer = True
    except Exception as ex:
        logging.error(repr(ex), exc_info=True)
        await  bot.send_message(callback_query.from_user.id, f"Произошла ошибка при удалении данных сервиса")
    if answer:
        await bot.send_message(callback_query.from_user.id, f"Успешно удалены данные для сервиса {item}")

@dp.callback_query_handler(lambda c: c.data and c.data.startswith('itemdel_'))
async def process_callback_delete(callback_query: types.CallbackQuery):
    # Получаем значение элемента из callback_data
    service = callback_query.data.split('_')[1]
    login = callback_query.data.split('_')[2] 
    password = callback_query.data.split('_')[3]
    # Отправляем сообщение с выбранным элементом,
    query = "DELETE FROM users WHERE telegram_id = %s and  service = %s  and login = %s and password = %s;"
    params = (callback_query.from_user.id, service,login,password)
    try:
        with get_pg_connection() as pg_conn, pg_conn.cursor() as cur:
            cur.execute(query, params)
        answer = True
    except Exception as ex:
        logging.error(repr(ex), exc_info=True)
        await  bot.send_message(callback_query.from_user.id, f"Произошла ошибка при удалении  одной записи")
    if answer:
        await bot.send_message(callback_query.from_user.id, f"Успешно удалена запись")
        

@dp.callback_query_handler(lambda c: c.data and c.data.startswith('itemget_'))
async def process_callback_get(callback_query: types.CallbackQuery):
    # Получаем значение элемента из callback_data
    item = callback_query.data.split('_')[1]
    query = "select service, login, password from users where telegram_id = %s and service = %s " 
    params = (callback_query.from_user.id, item)
    try:

        with get_pg_connection() as pg_conn, pg_conn.cursor() as cur:
            df = pd.read_sql_query(query, pg_conn,params=params)
            if len(df):
                delete_msg = await bot.send_message(callback_query.from_user.id,df.to_string(index=False))
                await asyncio.sleep(60)
                await delete_msg.delete()
            else:
                await bot.send_message(callback_query.from_user.id,'у вас нет сохранненых паролей для этого сервиса')
    except Exception as ex:
        logging.error(repr(ex), exc_info=True)
        await bot.send_message(callback_query.from_user.id,'Какая то ошибка произошла')


if __name__ == '__main__':

    executor.start_polling(dp, skip_updates=True)