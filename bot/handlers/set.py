
from aiogram import Bot, Dispatcher, executor, types, filters
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram import types, Dispatcher
from aiogram.dispatcher.filters import Command


class MyStates(StatesGroup):
    wait_data = State()

async def set(message: types.Message):
    await message.answer('Сейчас выведу список сервисов, которые вы записывали')
    # Устанавливаем состояние пользователя в 'wait_data'
    await MyStates.wait_data.set()

async def process_data(message: types.Message, state: FSMContext):
    # Получаем данные из сообщения
    data = message.text
    # Записываем данные в базу данных
    print(data)
    # Отправляем сообщение об успешной записи данных
    await message.answer(data)
    await message.answer('Данные успешно записаны в базу данных')
    # Сбрасываем состояние пользователя
    await state.finish()


def register_set(dp: Dispatcher):
    dp.register_message_handler(set, Command(['set']))
    dp.register_message_handler(process_data, state=MyStates.wait_data)