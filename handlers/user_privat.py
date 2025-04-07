from aiogram import types, Router
from aiogram.filters import CommandStart, Command

user_router = Router()


@user_router.message(CommandStart())
async def start_cmd(message: types.Message):
    await message.answer("Привет!\nЭто бот для продажи книг по Гарри Поттеру!")


@user_router.message(Command('catalog'))
async def catalog(message: types.Message):
    await message.answer("Привет, это Каталог!")


@user_router.message(Command('about'))
async def about(message: types.Message):
    await message.answer("Про нас")


@user_router.message(Command('contacts'))
async def contacts(message: types.Message):
    await message.answer("Контакты")


@user_router.message(Command('addresses'))
async def addresses(message: types.Message):
    await message.answer("Адреса наши")


@user_router.message()
async def echo(message: types.Message):
    await message.answer("Бот пока находится в разработке")
    # user_text = message.text
    # await message.answer(user_text)
