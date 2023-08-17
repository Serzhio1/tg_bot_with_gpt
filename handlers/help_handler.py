from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command


HELP_COMMAND = """<em><b>/help</b> - помощь</em>\n
<em><b>/description</b> - описание бота</em>\n
<em><b>/start</b> - запуск бота</em>\n
<em><b>/search_companies</b> - найти подходящие компании</em>"""

router = Router()

@router.message(Command('help'))
async def cmd_help(message: Message):
    await message.reply(text=HELP_COMMAND, parse_mode='HTML')