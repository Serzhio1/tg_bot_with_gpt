from aiogram import Router, F, types
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, ReplyKeyboardRemove
from aiogram.filters import Command
from keyboards.choose_category_kb import choose_category_keyboard
from keyboards.column_keyboard import column_keyboard
from aiogram.fsm.state import State, StatesGroup
from add_materials.data.data_structure import dict_category

text_choose_category_incorrectly = 'Категорию можно выбрать только из предложенного списка ниже'
text_choose_subcategory_incorrectly = 'Подкатегорию можно выбрать только из предложенного списка ниже'

class SearchCompaniesProcess(StatesGroup):
    choose_category_process = State()
    choose_subcategory_process = State()
    getting_data_process = State()

router = Router()

# пользователю предоставляется возможность выбора категории, к которой относится компания
@router.message(Command('search_companies'))
async def cmd_search_companies(message: Message, state: FSMContext):
    await message.answer("Выберете интересующую вас категорию из списка: ", reply_markup=choose_category_keyboard)
    await state.set_state(SearchCompaniesProcess.choose_category_process)

# пользователь выбрал одну из предложенных категорий
@router.message(
    SearchCompaniesProcess.choose_category_process,
    F.text.in_(dict_category.keys())
)
async def cmd_choose_category(message: Message, state: FSMContext):
    # предоставляем возможность выбрать подкатегорию, которая относится к компании
    await message.answer("Отлично, теперь выберете подкатегорию из списка ниже:", reply_markup=column_keyboard(dict_category[message.text]))
    await state.update_data(select_category = message.text) # сохранили информацию о выбранной категории
    await state.set_state(SearchCompaniesProcess.choose_subcategory_process) # пользователь начинает выбирать подкатегорию

# пользователь не выбрал ни одну из предложенных категорий, а написал свой вариант
@router.message(SearchCompaniesProcess.choose_category_process)
async def cmd_choose_category_incorrectly(message: Message):
    await message.answer(text=text_choose_category_incorrectly, reply_markup=choose_category_keyboard)

# пользователю выбрал подкатегорию из предложенного списка
@router.message(
    SearchCompaniesProcess.choose_subcategory_process
)
async def cmd_choose_subcategory(message: Message, state: FSMContext):
    user_data = await state.get_data()
    if message.text in dict_category.get(user_data['select_category'], []):
        await state.update_data(select_subcategory = message.text.lower()) # сохранили информацию о выбранной подкатеогрии
        user_data['select_subcategory'] = message.text
        await message.answer(f"Ваш запрос принят:\n\nКатегория: {user_data['select_category']}\n\nПодкатегория: {user_data['select_subcategory']}", reply_markup=ReplyKeyboardRemove())
        await state.set_state(SearchCompaniesProcess.getting_data_process) # теперь пользователь ожидает получения списка карточек организаций по его запросу
    # пользователь не выбрал ни одну из подкатекорий в предложенном списке, а написал свой вариант
    else:
        await message.answer(text=text_choose_subcategory_incorrectly, reply_markup=column_keyboard(dict_category[user_data['select_category']]))



