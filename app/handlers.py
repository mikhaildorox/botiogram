from aiogram import F, Router
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, CallbackQuery
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext

import app.keyboards as kb

router = Router()


class Registration(StatesGroup):
    name = State()
    number = State()

@router.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer(f"Hi!\nYour ID: {message.from_user.id}\nName: {message.from_user.first_name}",
                         reply_markup=kb.main)


@router.message(Command('help'))
async def cmd_help(message: Message):
    await message.answer("Help")


@router.message(F.text == 'How r u?')
async def cmd_how_r(message: Message):
    await message.answer("OK!")

#
@router.message(F.photo)
async def get_id_photo(message: Message):
    await message.answer(f"ID Photo: {message.photo[-1].file_id}")

@router.message(Command('get_photo'))
async def get_photo(message: Message):
    await message.answer_photo(photo='AgACAgIAAxkBAAIBimgm-qqj1GmgLdekXaTUBG-hdj-TAAKk6zEbCv04SQRKQggx7SRRAQADAgADeQADNgQ',
                               caption='This photo')

@router.callback_query(F.data == 'catalog')
async def catalog_handler(callback: CallbackQuery):
    await callback.answer("Выбран каталог")
    await callback.message.edit_text('Вы в каталоге', reply_markup=await kb.inline_colors())


@router.message(Command('reg'))
async def reg_handler(message: Message, state: FSMContext):
    await state.set_state(Registration.name)
    await message.answer('Введите ваше имя')


@router.message(Registration.name)
async def reg_numb_handler(message: Message, state: FSMContext):
    await state.update_data(name=message.text)
    await state.set_state(Registration.number)
    await message.answer("Введите номер телефона")


@router.message(Registration.number)
async def reg_success_handler(message: Message, state: FSMContext):
    await state.update_data(number=message.text)
    data = await state.get_data()
    await message.answer(f'Registration is Done.\nName: {data["name"]}\nNumber: {data["number"]}')
    await state.clear()