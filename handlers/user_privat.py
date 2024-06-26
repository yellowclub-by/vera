from aiogram import types, Router, F
from aiogram.filters import CommandStart, Command
from keyboards import reply, inline

user_router = Router()


@user_router.message(CommandStart())
async def start(message: types.Message):
    await message.answer('<b>Hello.</b> This is telegram bot of <b>cactus.by</b>. How can I help you? ',
                         reply_markup=reply.start_kb)


@user_router.message(F.text.lower() == 'catalog')
@user_router.message(Command('catalog'))
async def catalog(message: types.Message):
    await message.answer("<b>Here's what we have</b>", reply_markup=reply.catalog_kb)


@user_router.message(F.text.lower() == 'about')
@user_router.message(Command('about'))
async def about(message: types.Message):
    await message.answer('<strong>What you need to know about us</strong>', reply_markup=inline.links_kb)


@user_router.message(F.text.lower() == 'contacts')
@user_router.message(Command('contacts'))
async def contacts(message: types.Message):
    await message.answer('<b>Our contacts</b>', reply_markup=inline.contacts_kb())


@user_router.callback_query(F.data.lower().startswith('contact'))
async def contacts_types(callback: types.CallbackQuery):
    query = callback.data.split('_')[1]
    if query == '1':
        await callback.message.answer('cactus.by')
    else:
        await callback.message.answer('+357(44)7568345')
    await callback.answer()


@user_router.message(F.text.lower() == 'addresses')
@user_router.message(Command('addresses'))
async def addresses(message: types.Message):
    await message.answer('<b>Our addresses</b>', reply_markup=inline.addresses_kb())


@user_router.callback_query(F.data.lower().startswith('addresses'))
async def addresses_types(callback: types.CallbackQuery):
    query = callback.data.split('_')[1]
    if query == '1':
        await callback.message.answer('Surganova, 2B')
    elif query == '2':
        await callback.message.answer('This Street')
    else:
        await callback.message.answer('The Other Street')
    await callback.answer()


@user_router.message(F.text.lower() == 'back')
async def back_com(message: types.Message):
    await message.answer('<b>Main menu</b>', reply_markup=reply.start_kb)


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
