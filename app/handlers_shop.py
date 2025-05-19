from gc import callbacks

from aiogram import F, Router
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, CallbackQuery
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext

import app.keyboards as kb
import app.database.requests as rq

router = Router()


@router.message(CommandStart())
async def cmd_start(message: Message):
    await rq.set_user(message.from_user.id)
    await message.answer(f"Hi!\nIt's a shop!", reply_markup=kb.main)


@router.message(F.text == 'Каталог')
async def cmd_shop(message: Message):
    await message.answer('Выберите категорию товара', reply_markup=await kb.categories())


@router.callback_query(F.data.startswith('category_'))
async def category_handler(callback: CallbackQuery):
    await callback.answer(f"Вы выбрали категорию")
    await callback.message.answer('Выберите товар в категории',
                                  reply_markup=await kb.items(callback.data.split('_')[1]))


@router.callback_query(F.data.startswith('item_'))
async def item_handler(callback: CallbackQuery):
    item_data = await rq.get_item(callback.data.split('_')[1])
    await callback.answer(f"Вы выбрали товар")
    await callback.message.answer(
        f'Название: {item_data.name}\nОписание: {item_data.description}\nЦена: {item_data.price}',
        reply_markup=await kb.items(callback.data.split('_')[1]))
