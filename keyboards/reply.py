from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

main_kb = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Каталог"),
            KeyboardButton(text="Про нас")
        ],

        [
            KeyboardButton(text="Контакты"),
            KeyboardButton(text="Филиалы")
        ]
    ],
    resize_keyboard=True,
    input_field_placeholder="Что хотите?"
)

catalog_kb = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Книга 1'),
            KeyboardButton(text='Книга 2')],
        [
            KeyboardButton(text='Книга 3'),
            KeyboardButton(text='Книга 4')
        ]
    ],
    resize_keyboard=True
)
