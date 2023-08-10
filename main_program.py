from aiogram import Bot, Dispatcher, types, F
import asyncio
import logging
from aiogram.filters.command import Command, CommandObject
from aiogram import html
from datetime import datetime
from config import TOKEN_API

async def on_startup(_):
    print('бот был успешно зарущен')

bot = Bot(token=TOKEN_API) # объект бота
dp = Dispatcher() # диспетчер

@dp.message(Command('start'))
async def start(message: types.Message):
    await message.answer('Hello')

@dp.message(Command('help'))
async def help(message: types.Message):
    pass

@dp.message(F.text)
async def save_text(message: types.Message):
    pass

async def main():
    await dp.start_polling(bot, on_startup=on_startup)


if __name__ == '__main__':
    asyncio.run(main())