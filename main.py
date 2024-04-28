import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart

TOKEN = '7192849705:AAFCoJJGa8wYWW18HN6tb0AQSgBq2KA0SQc'

bot = Bot(token=TOKEN)
dp = Dispatcher()


@dp.message(CommandStart())
async def start(message: types.message):
    await message.answer('Hello.')


@dp.message()
async def echo(message: types.message):
    await message.answer('Bot is still being worked on')
    user_text = message.text
    await message.answer(user_text)


async def main():
    await dp.start_polling(bot)


asyncio.run(main())
