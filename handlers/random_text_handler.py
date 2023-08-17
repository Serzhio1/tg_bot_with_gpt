from aiogram import Router, F
from aiogram.types import Message
from aiogram.filters import Command

ANSWER_TO_RANDOM_QUESTION = 'Для взаимодействия с ботом пользуйтесь только теми командами, которые вы можете увидеть, набрав команду: /help'

router = Router()

@router.message(F.text)
async def cmd_random_text(message: Message):
    await message.answer(text=ANSWER_TO_RANDOM_QUESTION)