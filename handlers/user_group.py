from aiogram import types, Router, F
group_router = Router()


ban_w = ['hamster', 'cucumber', 'queue', 'hype', 'nigger', 'flower']


@group_router.message(F.text)
async def cleaner(message: types.Message):
    words_lst = message.text.split(' ')
    for word in words_lst:
        if word.lower() in ban_w:
            await message.answer(f"{message.from_user.first_name}, follow chat's rules")
            await message.delete()
            break





