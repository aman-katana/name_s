from aiogram import types, Router, F
from aiogram.filters import CommandStart, Command
from keyboards import reply, inline

user_router = Router()


@user_router.message(CommandStart())
async def start_cmd(message: types.Message):
    await message.answer("""Добро пожаловать в волшебный книжный уголок!
    
Здесь вы найдёте все книги о Гарри Поттере — от классических изданий до коллекционных экземпляров.
Погрузитесь в атмосферу Хогвартса, магии и приключений вместе с нами 

Заклинайте хорошие цены и откройте для себя магический мир Дж. К. Роулинг""", reply_markup=reply.main_kb)


@user_router.message(F.text.lower() == "каталог")
@user_router.message(Command('catalog'))
async def catalog(message: types.Message):
    await message.answer("Привет, это Каталог!", reply_markup=reply.catalog_kb)


@user_router.message(F.text.lower() == 'про нас')
@user_router.message(Command('about'))
async def about(message: types.Message):
    await message.answer("Про нас")


@user_router.message(F.text.lower() == 'контакты')
@user_router.message(Command('contacts'))
async def contacts(message: types.Message):
    await message.answer("Контакты")


@user_router.message(F.text.lower() == 'филиалы')
@user_router.message(Command('addresses'))
async def addresses(message: types.Message):
    await message.answer("Адреса наши", reply_markup=inline.addresses_kb())


@user_router.callback_query(F.data.lower().startswith('addresses'))
async def addresses_info(callback: types.CallbackQuery):
    query = callback.data.split("_")[1]
    if query == '1':
        await callback.message.answer('Пункт выдачи 1')
    elif query == '2':
        await callback.message.answer('Пункт выдачи 2')
    elif query == '3':
        await callback.message.answer('Пункт выдачи 3')

    await callback.answer('Адрес отправлен')



@user_router.message(F.text.lower() == 'назад')
async def back_menu(message: types.Message):
    await message.answer("Главное меню", reply_markup=reply.main_kb)


# @user_router.message(F.text)
# @user_router.message(F.photo)
# @user_router.message(F.text.lower() == "доставка")
# @user_router.message(F.text.lower().contains("доставк"))
# @user_router.message(F.text.lower().startswith('как'))
# @user_router.message(F.text.lower().endswith("?"))
# @user_router.message(F.text.lower().startswith('как'), F.text.lower().endswith("?"))
# @user_router.message(F.text.lower().contains('цен') | F.text.lower().contains('стоимост'))
# @user_router.message(F.text)
# async def echo(message: types.Message):
#     await message.answer("Сработал магический фильтр")
#     user_text = message.text
#     await message.answer(user_text)
