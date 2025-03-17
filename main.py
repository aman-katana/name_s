import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart

TOKEN = "7891539181:AAHqDuH1f05AjfJvvqPc7Q86tm6aez691do"

bot = Bot(token=TOKEN)
dp = Dispatcher()


@dp.message(CommandStart())
async def start_cmd(message: types.Message):
    await message.answer("Привет!\nЭто бот для продажи книг по Гарри Поттеру!")


@dp.message()
async def echo(message: types.Message):
    await message.answer("Бот пока находится в разработке")
    # user_text = message.text
    # await message.answer(user_text)


async def main():
    print("Бот запущен")
    await dp.start_polling(bot)


asyncio.run(main())
