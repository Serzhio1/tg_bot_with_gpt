from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command


description_message = """Привет! Я - ваш персональный помощник в поиске подходящих компаний-поддержки. Просто запустите работу, написав команду /search_companies, и я выведу результаты!\n
Карточки компаний содержат информацию о названии, ссылке на дополнительную информацию, принадлежности к категориям и подкатегориям, тегам рынка НТИ, индустрии и организациям.\n
Используйте команду /help для получения дополнительной информации о доступных командах и использовании бота."""

router = Router()

@router.message(Command('description'))
async def cmd_description(message: Message):
    await message.answer(text=description_message)
