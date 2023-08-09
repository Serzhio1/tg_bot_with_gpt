from aiogram import Bot, Dispatcher, types, F
import asyncio
import logging
from aiogram.filters.command import Command, CommandObject
from aiogram import html
from datetime import datetime

bot = Bot(token='6461558599:AAEzMAEkXheZCREbW7B1xnpJSrMq5Y88XZw') # объект бота
dp = Dispatcher() # диспетчер

@dp.message(Command('start'))
async def start(message: types.Message):
    await message.answer('Hello')

@dp.message(Command('help'))
async def help(message: types.Message):
    await message.reply('чем я могу тебе помочь')

@dp.message(F.text)
async def save_text(message: types.Message):
    pass

async def main():
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())