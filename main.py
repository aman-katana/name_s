import asyncio
from aiogram import Bot, Dispatcher, types

from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode

TOKEN = "7891539181:AAHqDuH1f05AjfJvvqPc7Q86tm6aez691do"

bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
dp = Dispatcher()

from handlers.user_privat import user_router
from handlers.user_group import group_router
from handlers.catalog import catalog_router
dp.include_router(user_router)
dp.include_router(catalog_router)
dp.include_router(group_router)



async def main():
    print("Бот запущен")
    await dp.start_polling(bot)


asyncio.run(main())
