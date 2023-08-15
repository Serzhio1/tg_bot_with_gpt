from aiogram import Bot, Dispatcher, types, F
import asyncio
import logging
from aiogram.filters.command import Command, CommandObject
from aiogram import html
from datetime import datetime
from config import TOKEN_API
from keyboards import choose_category_keyboard, HELP_COMMAND, start_message, description_message

async def on_startup(_):
    print('бот был успешно запущен')

bot = Bot(token=TOKEN_API) # объект бота,
dp = Dispatcher() # диспетчер

@dp.message(Command('start'))
async def start(message: types.Message):
    await message.answer(text=start_message)

@dp.message(Command('description'))
async def cmd_description(message: types.Message):
    await message.reply(text=description_message)

@dp.message(Command('search_companies'))
async def cmd_choose_company(message: types.Message):
    await message.answer("Выберете интересующую вас область: ", reply_markup=choose_category_keyboard)

@dp.message(Command('help'))
async def cmd_help(message: types.Message):
    await message.answer(text=HELP_COMMAND, parse_mode='HTML')
@dp.message(F.text)

async def handle_user_message(message: types.Message):
    array_of_category = ['Развитие проекта', 'Подборки', 'Продвижение', 'Образование и наука', 'Финансы', 'Полезные материалы']
    if message.text in array_of_category:
        await message.answer("Отлично, теперь опишите подробнее ваш запрос в свободной форме.", reply_markup=types.ReplyKeyboardRemove())
    else:
        await message.answer("Категорию можно выбрать только из предложенного списка!")

async def main():
    await dp.start_polling(bot, on_startup=on_startup)


if __name__ == '__main__':
    asyncio.run(main())