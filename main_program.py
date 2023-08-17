from aiogram import Bot, Dispatcher, types, F
import asyncio
import logging
from aiogram.filters.command import Command, CommandObject
from aiogram import html
from datetime import datetime
from config import TOKEN_API
from handlers import start_handler, decription_handler, help_handler, search_companies_handler, random_text_handler


async def main():
    bot = Bot(token=TOKEN_API)
    dp = Dispatcher()

    dp.include_router(start_handler.router)
    dp.include_router(decription_handler.router)
    dp.include_router(help_handler.router)
    dp.include_router(search_companies_handler.router)
    dp.include_router(random_text_handler.router)

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())




