from aiogram import types, Router
from aiogram.filters import CommandStart, Command

user_router = Router()


@user_router.message(CommandStart())
async def start(message: types.Message):
    await message.answer('Hello.')


@user_router.message(Command('catalog'))
async def catalog(message: types.Message):
    await message.answer("Here's what we have")


@user_router.message(Command('about'))
async def about(message: types.Message):
    await message.answer('What you need to know about us')


@user_router.message(Command('contacts'))
async def contacts(message: types.Message):
    await message.answer('Our contacts')


@user_router.message(Command('addresses'))
async def addresses(message: types.Message):
    await message.answer('Our addresses')


@user_router.message()
async def echo(message: types.Message):
    await message.answer('Bot is still being worked on')
    user_text = message.text
    await message.answer(user_text)





