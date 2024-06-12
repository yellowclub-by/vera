from aiogram import Router, types, F
from aiogram.types import FSInputFile

cat_router = Router()


@cat_router.message(F.text.lower() == 'cactus')
async def cat_cactus(message: types.Message):
    photo = FSInputFile('img\catalog\cactus.jpg')
    await message.answer_photo(photo, caption='Cactus this is')


@cat_router.message(F.text.lower() == 'mini cactus')
async def cat_mini(message: types.Message):
    photo = FSInputFile('img\catalog\mini cactus.jpg')
    await message.answer_photo(photo, caption='Mini cactus this is')


@cat_router.message(F.text.lower() == 'coloured cactus')
async def cat_coloured(message: types.Message):
    photo = FSInputFile('img\catalog\coloured cactuses.jpg')
    await message.answer_photo(photo, caption='Coloured cactus this is')


@cat_router.message(F.text.lower() == 'succulent')
async def cat_succulent(message: types.Message):
    photo = FSInputFile('img\catalog\succulent.jpg')
    await message.answer_photo(photo, caption='Succulent this is')


@cat_router.message(F.text.lower() == 'ripsalis')
async def cat_coloured(message: types.Message):
    photo = FSInputFile(r'img\catalog\ripsalis.jpg')
    await message.answer_photo(photo, caption='Ripsalis this is')


@cat_router.message(F.text.lower() == 'opuntia')
async def cat_coloured(message: types.Message):
    photo = FSInputFile('img\catalog\opuntia.jpg')
    await message.answer_photo(photo, caption='Opuntia this is')









