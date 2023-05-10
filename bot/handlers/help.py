from aiogram import types, Dispatcher
from aiogram.dispatcher.filters import Command


async def help(message: types.Message):
    # Отправляем приветственное сообщение
    text = [
        "/help - команда помощи утопающим",
        "/menu - один раз нужно ее прописать и у вас всегда будет доступно меню со всеми командами",
        "/list - выводит список сервисов, для которых записаны пароли",
        "/set - позволяет записать свой логин пароль для сервиса (для одного сервиса можно хранить много паролей)",
        "/del_all - удаляет все записи для сервиса (нужноо написать имя сервиса и удалит все записи) Используй аккуратно",
        "/del_piece - удаляет конкретно одну запись",
        "/get - позволяет получить пароли от сервиса по его названию",

    ]
      
    await message.answer('\n'.join(text))



def register_help(dp: Dispatcher):
    dp.register_message_handler(help, Command(['help']), state='*')
