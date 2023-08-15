from aiogram import types


description_message = """Привет! Я - ваш персональный помощник в поиске подходящих компаний-поддержки. Просто запустите работу, написав команду /search_companies, и я выведу результаты!\n
Карточки компаний содержат информацию о названии, ссылке на дополнительную информацию, принадлежности к категориям и подкатегориям, тегам рынка НТИ, индустрии и организациям.\n
Используйте команду /help для получения дополнительной информации о доступных командах и использовании бота."""

start_message = 'Привет! Я чат-бот, который найдет тебе подходящуюю компанию-помощника, опираясь на твои запросы и интересы. Для запуска работы напиши: /search_companies'

HELP_COMMAND = """<em><b>/help</b> - помощь</em>\n
<em><b>/description</b> - описание бота</em>\n
<em><b>/start</b> - запуск бота</em>\n
<em><b>/search_companies</b> - найти подходящие компании</em>"""

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