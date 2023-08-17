from aiogram import types


choose_category_kb = [
        [types.KeyboardButton(text='Развитие проекта')],
        [types.KeyboardButton(text='Продвижение')],
        [types.KeyboardButton(text='Образование и наука')],
        [types.KeyboardButton(text='Подборки')],
        [types.KeyboardButton(text='Финансы')],
        [types.KeyboardButton(text='Полезные материалы')]
    ]
choose_category_keyboard = types.ReplyKeyboardMarkup(
    keyboard=choose_category_kb,
    resize_keyboard=True,
    input_field_placeholder='выберете интересующую вас область'
)