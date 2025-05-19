from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


def addresses_kb():
    builder = InlineKeyboardBuilder()
    builder.row(
        InlineKeyboardButton(text="Пункт выдачи 1", callback_data="addresses_1"),
        InlineKeyboardButton(text='Пункт выдачи 2', callback_data='addresses_2'),
        InlineKeyboardButton(text='Пункт выдачи 3', callback_data='addresses_3'),
        width=1
    )

    return builder.as_markup()


links_kb = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Сайт', url='https://yellowclub.by/online/'),
            InlineKeyboardButton(text="Телеграм", url='tg://resolve?domain=Python_Yellow_Club')
        ]
    ]
)
