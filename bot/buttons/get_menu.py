from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

def get_keyboard(items):
# Создаем список кнопок
    buttons = []
    for item in items:
        button = InlineKeyboardButton(text=item, callback_data=f"itemget_{item}")
        buttons.append(button)

    # Создаем InlineKeyboardMarkup
    result = InlineKeyboardMarkup(row_width=2)
    result.add(*buttons)
    return result