import asyncio
from aiogram import Bot, Dispatcher, types

TOKEN = '7192849705:AAFCoJJGa8wYWW18HN6tb0AQSgBq2KA0SQc'

bot = Bot(token=TOKEN)
dp = Dispatcher()


from handlers.user_privat import user_router
dp.include_router(user_router)


async def main():
    await dp.start_polling(bot)


asyncio.run(main())






















