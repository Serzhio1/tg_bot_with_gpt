from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command


start_message = 'Привет! Я чат-бот, который найдет тебе подходящуюю компанию-помощника, опираясь на твои запросы и интересы. Для запуска работы напиши: /search_companies'

router = Router()
@router.message(Command('start'))
async def cdm_start(message: Message):
    await message.answer(text=start_message)