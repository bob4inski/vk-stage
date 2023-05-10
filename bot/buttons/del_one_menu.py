from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

def keyboard(items):
# Создаем список кнопок
    buttons = []
    for item in items:
        button = InlineKeyboardButton(text=f'{item[0]}:{item[1]}:{item[2]}', callback_data=f"itemdel_{item[0]}_{item[1]}_{item[2]}")
        buttons.append(button)

    # Создаем InlineKeyboardMarkup
    result = InlineKeyboardMarkup(row_width=2)
    result.add(*buttons)
    return result