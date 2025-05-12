from aiogram import types, Router, F
from aiogram.types import FSInputFile

catalog_router = Router()


@catalog_router.message(F.text.lower() == 'книга 1')
async def book_1(message: types.Message):
    photo = FSInputFile(r'img\catalog\first.jpeg')
    text = """Гарри Поттер и философский камень\n
    
Фэнтезийный роман британской писательницы Джоан Роулинг. 
Первая часть в серии книг о Гарри Поттере и дебютный роман Роулинг.

Цена: 10 монет
"""
    await message.answer_photo(photo, caption=text)


@catalog_router.message(F.text.lower() == 'книга 2')
async def book_2(message: types.Message):
    photo = FSInputFile(r'img\catalog\second.jpg')
    text = """Гарри Поттер и Тайная комната\n
второй роман в серии книг про юного волшебника Гарри Поттера, написанный Джоан Роулинг. 
Книга рассказывает о втором учебном годе в школе чародейства и волшебства Хогвартс, 
на котором Гарри и его друзья — Рон Уизли и Гермиона Грейнджер — расследуют таинственные нападения на учеников школы, 
совершаемые неким «Наследником Слизерина».

Цена: 10 монет
"""
    await message.answer_photo(photo, caption=text)


@catalog_router.message(F.text.lower() == 'книга 3')
async def book_3(message: types.Message):
    photo = FSInputFile(r'img\catalog\third.jpeg')
    text = """Гарри Поттер и узник Азкабана\n
Третья книга Джоан Роулинг из серии романов о Гарри Поттере. 
В третьей книге Гарри Поттер, учащийся на третьем курсе школы чародейства и волшебства Хогвартс, 
вместе со своими друзьями Роном Уизли и Гермионой Грейнджер узнает историю Сириуса Блэка — бежавшего из тюрьмы Азкабан 
волшебника, который подозревается в работе на лорда Волан-де-Морта и о его роли в своей жизни.

Цена: 10 монет
    """
    await message.answer_photo(photo, caption=text)


@catalog_router.message(F.text.lower() == 'книга 4')
async def book_4(message: types.Message):
    photo = FSInputFile(r'img\catalog\fourths.jpeg')
    text = """Гарри Поттер и Кубок огня\n
Четвёртая книга о приключениях Гарри Поттера, написанная английской писательницей Джоан Роулинг. 
В Англии опубликована в 2000 году. По сюжету Гарри Поттер против своей воли вовлекается в участие в 
Турнире Трёх Волшебников, и ему предстоит не только сразиться с более опытными участниками, но и разгадать загадку того,
как он вообще попал на турнир вопреки правилам.

Цена: 10 монет"""
    await message.answer_photo(photo, caption=text)
