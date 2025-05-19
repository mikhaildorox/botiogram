from aiogram.types import (ReplyKeyboardMarkup, KeyboardButton,
                           InlineKeyboardMarkup, InlineKeyboardButton)

from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder

main = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='Каталог')],
    [KeyboardButton(text="Корзина"), KeyboardButton(text="Контакты")]
],
    resize_keyboard=True, input_field_placeholder='Choose your keyboard')


catalog = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Blue', callback_data='blue')],
    [InlineKeyboardButton(text="Red", callback_data='red'),
     InlineKeyboardButton(text="Green", callback_data='green')],
])


get_number = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text='Отправить номер', request_contact=True)]], resize_keyboard=True)

# settings = InlineKeyboardMarkup(inline_keyboard=[
#     [InlineKeyboardButton(text='Rutube', url='https://rutube.org')],
# ])

# colors = ['Red', 'Green', 'Blue']


# async def inline_colors():
#     keyboard = InlineKeyboardBuilder()
#     for color in colors:
#         keyboard.add(InlineKeyboardButton(text=color, url='https://rutube.org'))
#     return keyboard.adjust(2).as_markup()
