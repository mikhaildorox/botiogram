from aiogram import F, Router
from aiogram.filters import CommandStart, Command
from aiogram.types import Message

router = Router()


@router.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer("Hi!")


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
