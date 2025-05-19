from aiogram import F, Router
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, CallbackQuery
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext

import app.keyboards as kb
from app.middleware import TestMiddleware
import app.database.requests as rq

router = Router()

router.message.middleware(TestMiddleware())

class Registration(StatesGroup):
    name = State()
    number = State()

@router.message(CommandStart())
async def cmd_start(message: Message):
    await rq.set_user(message.from_user.id)
    await message.answer(f"Hi!\nYour ID: {message.from_user.id}\nName: {message.from_user.first_name}",
                         reply_markup=kb.main)


@router.message(Command('help'))
async def cmd_help(message: Message):
    await message.answer("Help")


@router.message(F.text == 'Каталог')
async def cmd_catalog(message: Message):
    await message.answer("Выберите категорию", reply_markup=kb.catalog)

#
@router.message(F.photo)
async def get_id_photo(message: Message):
    await message.answer(f"ID Photo: {message.photo[-1].file_id}")

@router.message(Command('get_photo'))
async def get_photo(message: Message):
    await message.answer_photo(photo='AgACAgIAAxkBAAIBimgm-qqj1GmgLdekXaTUBG-hdj-TAAKk6zEbCv04SQRKQggx7SRRAQADAgADeQADNgQ',
                               caption='This photo')

@router.callback_query(F.data == 'blue')
async def catalog_color(callback: CallbackQuery):
    await callback.answer("Выбран color", show_alert=True)
    await callback.message.answer("Вы нажали blue")
    # await callback.message.edit_text('Вы нажали blue', reply_markup=await kb.catalog)


@router.message(Command('reg'))
async def reg_handler(message: Message, state: FSMContext):
    await state.set_state(Registration.name)
    await message.answer('Введите ваше имя')


@router.message(Registration.name)
async def reg_numb_handler(message: Message, state: FSMContext):
    await state.update_data(name=message.text)
    await state.set_state(Registration.number)
    await message.answer("Введите номер телефона", reply_markup=kb.get_number)


@router.message(Registration.number, F.contact)
async def reg_success_handler(message: Message, state: FSMContext):
    await state.update_data(number=message.contact.phone_number)
    data = await state.get_data()
    await message.answer(f'Registration is Done.\nName: {data["name"]}\nNumber: {data["number"]}')
    await state.clear()