from aiogram.types import (ReplyKeyboardMarkup, KeyboardButton,
                           InlineKeyboardMarkup, InlineKeyboardButton)

from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder

# main = ReplyKeyboardMarkup(keyboard=[
#     [KeyboardButton(text='Каталог')],
#     [KeyboardButton(text="Корзина"), KeyboardButton(text="Контакты")]
# ],
#     resize_keyboard=True, input_field_placeholder='Choose your keyboard')


main = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Каталог', callback_data='catalog')],
    [InlineKeyboardButton(text="Корзина", callback_data='basket'),
     InlineKeyboardButton(text="Контакты", callback_data='contacts')],
])

settings = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Rutube', url='https://rutube.org')],
])

colors = ['Red', 'Green', 'Blue']


async def inline_colors():
    keyboard = InlineKeyboardBuilder()
    for color in colors:
        keyboard.add(InlineKeyboardButton(text=color, url='https://rutube.org'))
    return keyboard.adjust(2).as_markup()
