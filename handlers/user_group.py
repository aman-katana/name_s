from aiogram import types, Router, F

group_router = Router()

restricted_words = ['персик', 'шоколад', 'фурри']


@group_router.message(F.text)
async def cleaner(message: types.Message):
    words_lst = message.text.split(" ")
    for word in words_lst:
        if word in restricted_words:
            await message.answer(f"{message.from_user.first_name} соблюдайте правила чата!")
            # await message.answer(f"@{message.from_user.username}")
            await message.delete()
            break
