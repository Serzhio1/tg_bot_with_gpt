from aiogram import Router, F, types
from aiogram.fsm.context import FSMContext
from aiogram.types import Message
from aiogram.filters import Command
from keyboards.choose_category_kb import choose_category_keyboard
from aiogram.fsm.state import State, StatesGroup


text_choose_category_incorrectly = 'Категорию можно выбрать только из предложенного списка ниже'
array_of_category = ['Развитие проекта', 'Подборки', 'Продвижение', 'Образование и наука', 'Финансы', 'Полезные материалы']

subcategory_groups = {
    'Развитие проекта': ['Комплексная поддержка', 'Студентам', 'Акселерация', 'Выход на новые рынки', 'Развитие команды', 'Пилотирование', 'Предложения НТИ','Сообщества НТИ', 'Технологические конкурсы', 'Беспилотная авиация'],
    'Подборки': ['Студентам', 'Акселерация', 'Развитие команды', 'Предложения НТИ', 'Сообщества НТИ', 'Гранты', 'Инвестиции', 'Курсы', 'Живые дорожные карты НТИ', 'Настоящее будущее', 'Инфографика', 'Развитие технологий', 'Технологические конкурсы', 'Консультации экспертов', 'Данные', 'Интернет-ресурсы', 'Беспилотная авиация', 'Поиск партнеров', 'Субсидии', 'Продвижение', 'Льготы'],
    'Продвижение': ['Выход на новые рынки', 'Пилотирование', 'Продвижение', 'Поиск партнеров', 'Предложения НТИ', 'Сообщества НТИ', 'Беспилотная авиация'],
    'Образование и наука': ['Консультации экспертов', 'Проведение исследований', 'Предложения НТИ', 'Курсы', 'Студентам', 'Развитие технологий', 'Беспилотная авиация'],
    'Финансы': ['Гранты', 'Студентам', 'Предложения НТИ', 'Инвестиции', 'Субсидии', 'Льготы', 'Беспилотная авиация'],
    'Полезные материалы': ['Предложения НТИ', 'Живые дорожные карты НТИ', 'Настоящее будущее', 'Инфографика', 'Данные', 'Интернет-ресурсы', 'Беспилотная авиация', 'Навигатор']
}

class SearchCompaniesProcess(StatesGroup):
    choose_category_process = State()
    give_free_answer_process = State()

router = Router()

@router.message(Command('search_companies'))
async def cmd_search_companies(message: Message, state: FSMContext):
    await message.answer("Выберете интересующую вас категорию из списка: ", reply_markup=choose_category_keyboard)
    await state.set_state(SearchCompaniesProcess.choose_category_process)

@router.message(
    SearchCompaniesProcess.choose_category_process,
    F.text.in_(array_of_category)
)
async def cmd_choose_category(message: Message, state: FSMContext):
    await message.answer("Отлично, теперь опишите подробнее ваш запрос в свободной форме.", reply_markup=types.ReplyKeyboardRemove())
    await state.update_data(selected_category = message.text.lower()) # сохранили информацию
    await state.set_state(SearchCompaniesProcess.give_free_answer_process)

@router.message(SearchCompaniesProcess.choose_category_process)
async def cmd_choose_category_incorrectly(message: Message):
    await message.answer(text=text_choose_category_incorrectly, reply_markup=choose_category_keyboard)

@router.message(
    SearchCompaniesProcess.give_free_answer_process,
    F.text
)
async def cmd_answer(message: Message, state: FSMContext):
    await state.update_data(detailed_request= message.text.lower())
    user_data = await state.get_data()
    await message.answer(f"<b>Ваш запрос принят!</b>\n\n<b>Категория:</b> {user_data['selected_category']}\n\n<b>Подробный запрос:</b> {user_data['detailed_request']}\n\nСейчас я пришлю список карточек, подходящих вам компаний", parse_mode='HTML')
    await state.clear()




