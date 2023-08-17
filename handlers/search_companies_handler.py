from aiogram import Router, F, types
from aiogram.fsm.context import FSMContext
from aiogram.types import Message
from aiogram.filters import Command
from keyboards.choose_category_kb import choose_category_keyboard
from aiogram.fsm.state import State, StatesGroup

text_choose_category_incorrectly = 'Категорию можно выбрать только из предложенного списка ниже'
array_of_category = ['Развитие проекта', 'Подборки', 'Продвижение', 'Образование и наука', 'Финансы', 'Полезные материалы']

class SearchCompaniesProcess(StatesGroup):
    choose_category_process = State()
    give_free_answer_process = State()

router = Router()

@router.message(Command('search_companies'))
async def cmd_search_companies(message: Message, state: FSMContext):
    await message.answer("Выберете интересующую вас категорию из списка: ", reply_markup=choose_category_keyboard)
    await state.set_state(SearchCompaniesProcess.choose_category_process)

@router.message(
    SearchCompaniesProcess.give_free_answer_process,
    F.text
)
async def cmd_answer(message: Message, state: FSMContext):
    await message.answer(f"Я принял ваш запрос: {message.text}\n\nСейчас я пришлю список, подходящих вам компаний")
    await state.clear()

@router.message(
    SearchCompaniesProcess.choose_category_process,
    F.text.in_(array_of_category)
)
async def cmd_choose_category(message: Message, state: FSMContext):
    await message.answer("Отлично, теперь опишите подробнее ваш запрос в свободной форме.", reply_markup=types.ReplyKeyboardRemove())
    await state.set_state(SearchCompaniesProcess.give_free_answer_process)

@router.message(SearchCompaniesProcess.choose_category_process)
async def cmd_choose_category_incorrectly(message: Message):
    await message.answer(text=text_choose_category_incorrectly, reply_markup=choose_category_keyboard)


