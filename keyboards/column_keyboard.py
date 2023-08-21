from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

def column_keyboard(items: list[str]) -> ReplyKeyboardMarkup:
    buttons = [KeyboardButton(text=item) for item in items]
    rows = [[button] for button in buttons]
    return ReplyKeyboardMarkup(keyboard=rows, resize_keyboard=True)

