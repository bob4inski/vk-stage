from aiogram import types, Dispatcher
from aiogram.dispatcher.filters import Command


async def help(message: types.Message):
    # Отправляем приветственное сообщение
    text = [
        "/help - команда помощи утопающим",
        "/set - позволяет записать свой логин пароль для сервиса (для одного сервиса можно хранить много паролей)(единственное ограничение на вводимые данные - не должно быть нижних подчеркиваний)",
        "/del_all - удаляет все записи для сервиса (нужноо выбрать название сервиса и все удалится) P.S Используй аккуратно",
        "/del_one - удаляет конкретно одну запись",
        "/get - позволяет получить пароли от сервиса по его названию",
        "снова напоминаю про то, что в названии сервиса, логине и пароле не может присутствовать символ '_'"

    ]
      
    await message.answer('\n'.join(text))



def register_help(dp: Dispatcher):
    dp.register_message_handler(help, Command(['help']), state='*')
