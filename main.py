import asyncio
from aiogram import Bot, Dispatcher

TOKEN = '7192849705:AAFCoJJGa8wYWW18HN6tb0AQSgBq2KA0SQc'

bot = Bot(token=TOKEN, parse_mode='HTML')
dp = Dispatcher()


from handlers.user_privat import user_router
dp.include_router(user_router)

from handlers.catalog import cat_router
dp.include_router(cat_router)

from handlers.user_group import group_router
dp.include_router(group_router)


async def main():
    await dp.start_polling(bot)


asyncio.run(main())

