from aiogram import types, Router, F
from aiogram.filters import CommandStart, Command
from keyboards import reply

user_router = Router()


@user_router.message(CommandStart())
async def start(message: types.Message):
    await message.answer('Hello.', reply_markup=reply.start_kb)


@user_router.message(F.text.lower() == 'catalog')
@user_router.message(Command('catalog'))
async def catalog(message: types.Message):
    await message.answer("Here's what we have", reply_markup=reply.catalog_kb)


@user_router.message(F.text.lower() == 'about')
@user_router.message(Command('about'))
async def about(message: types.Message):
    await message.answer('What you need to know about us')


@user_router.message(F.text.lower() == 'contacts')
@user_router.message(Command('contacts'))
async def contacts(message: types.Message):
    await message.answer('Our contacts')


@user_router.message(F.text.lower() == 'addresses')
@user_router.message(Command('addresses'))
async def addresses(message: types.Message):
    await message.answer('Our addresses')


# @user_router.message(F.text)
# @user_router.message(F.photo)
# @user_router.message(F.text.lower() == 'delivery')
# @user_router.message(F.text.lower().contains('deliver'))
# @user_router.message(F.text.lower().startswith('how'))
# @user_router.message(F.text.endswith('?'))
# @user_router.message(F.text.lower().startswith('how'), F.text.endswith('?'))

# @user_router.message((F.text.lower().contains('cost')) | (F.text.lower().contains('price')))
# async def echo(message: types.Message):
#     await message.answer('Magic filter: activated')






