from aiogram import types, Router, F
from aiogram.types import FSInputFile

catalog_router = Router()


@catalog_router.message(F.text.lower() == 'книга 1')
async def book_1(message: types.Message):
    photo = FSInputFile(r'img\catalog\first.jpeg')
    await message.answer_photo(photo, caption="Первая книга")



@catalog_router.message(F.text.lower() == 'книга 2')
async def book_2(message: types.Message):
    photo = FSInputFile(r'img\catalog\second.jpg')
    await message.answer_photo(photo, caption="Вторая книга")



@catalog_router.message(F.text.lower() == 'книга 3')
async def book_3(message: types.Message):
    photo = FSInputFile(r'img\catalog\third.jpeg')
    await message.answer_photo(photo, caption="Третья книга")



@catalog_router.message(F.text.lower() == 'книга 4')
async def book_4(message: types.Message):
    photo = FSInputFile(r'img\catalog\fourths.jpeg')
    await message.answer_photo(photo, caption="Четвёртая книга")

