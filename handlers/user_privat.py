from aiogram import types, Router, F
from aiogram.filters import CommandStart, Command
from keyboards import reply, inline

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
    await message.answer('Our addresses', reply_markup=inline.addresses_kb())


@user_router.callback_query(F.data.lower().startswith('addresses'))
async def addresses_types(callback: types.CallbackQuery):
    query = callback.data.split('_')[1]
    if query == '1':
        await callback.message.answer('address 1 this is')
    elif query == '2':
        await callback.message.answer('address 2 this is')
    else:
        await callback.message.answer('address 3 this is')
    await callback.answer()


@user_router.message(F.text.lower() == 'back')
async def back_com(message: types.Message):
    await message.answer('Main menu', reply_markup=reply.start_kb)




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
