
from aiogram import  Dispatcher, types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram import types, Dispatcher
from aiogram.dispatcher.filters import Command
from bot.bd.connet import get_pg_connection
import logging
import asyncio
from bot.buttons.del_one_menu import keyboard





class MyStates_del_one(StatesGroup):
    wait_data = State()


async def del_one(message: types.Message):
   
    # text = [
    #     "Введите через пробел название сервиса, логин и пароль для записи которую вы хотите удалить",
    #     "К примеру:",
    #     "telegram aboba bob4inski"
    # ]
    # await message.answer('\n'.join(text))
    # await MyStates_del_one.wait_data.set()

    await message.answer('Сейчас выведу список сервисов, которые вы записывали, выберите какой удалить')
    # Устанавливаем состояние пользователя в 'wait_data'
    query = f'select * from users where telegram_id = {message.from_user.id};'
    services = []
    try:

        with get_pg_connection() as pg_conn, pg_conn.cursor() as cur:
            cur.execute(query)
            rows = cur.fetchall()
            services = []
            for row in rows:
                service = []
                service.append(row['service'])
                service.append(row['login'])
                service.append(row['password'])
                services.append(service)

        del_msg_from_del_one = await message.answer("Выберите запись которую вы хотите удалить:", reply_markup=keyboard(services))
           
    except Exception as ex:
        logging.error(repr(ex), exc_info=True)
        await message.answer('Произошла какая-то ошибка')

    await asyncio.sleep(360) # так как тут выводятся пароли в открытом виде, то нужно будет сообщение удалить
    await del_msg_from_del_one.delete()  

# async def process_data_del_one(message: types.Message, state: FSMContext):
#     # Получаем данные из сообщения
#     data = message.text
#     splited_data = data.split(" ")
#     query = "DELETE FROM users WHERE telegram_id = %s and  service = %s and login = %s and password = %s ;"
#     params = (message.from_user.id, splited_data[0],splited_data[1],splited_data[2])
#     try:
#         with get_pg_connection() as pg_conn, pg_conn.cursor() as cur:
#             cur.execute(query, params)
#         await message.answer("данные были успешно удалены") 
#     except Exception as ex:
#         logging.error(repr(ex), exc_info=True)
#         await message.answer('Произошла какая-то ошибка')
        
#     await state.finish()


def register_del_one(dp: Dispatcher):
    dp.register_message_handler(del_one, Command(['del_one']))
    # dp.register_message_handler(process_data_del_one, state=MyStates_del_one.wait_data)