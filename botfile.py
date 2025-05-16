import asyncio
import logging

from aiogram import Bot, Dispatcher, F
from aiogram.filters import CommandStart, Command
from aiogram.types import Message

from config import TOKEN

bot = Bot(token=TOKEN)
dp = Dispatcher()


@dp.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer("Hi!")


@dp.message(Command('help'))
async def cmd_help(message: Message):
    await message.answer("Help")


@dp.message(F.text == 'How r u?')
async def cmd_how_r(message: Message):
    await message.answer("OK!")

#
@dp.message(F.photo)
async def get_id_photo(message: Message):
    await message.answer(f"ID Photo: {message.photo[-1].file_id}")

@dp.message(Command('get_photo'))
async def get_photo(message: Message):
    await message.answer_photo(photo='AgACAgIAAxkBAAIBimgm-qqj1GmgLdekXaTUBG-hdj-TAAKk6zEbCv04SQRKQggx7SRRAQADAgADeQADNgQ',
                               caption='This photo')

async def main():
    await dp.start_polling(bot)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        pass
