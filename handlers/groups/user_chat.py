from aiogram import types
from aiogram.dispatcher.filters import Command

from filters import IsGroup

from loader import dp, bot, db


@dp.message_handler(IsGroup(), Command(commands=["myscore"], prefixes="/"))
def my_score(message: types.Message):
    """ Отправляет количество очков пользователя """

    member_id = message.from_user.id

    username, score = db.get_score_user(member_id)[0]

    if score > 0:
        text = "У @{username} - {score} баллов"
    else:
        text = "У @{username} пока что нет баллов"
    
    await message.answer(text)
    await message.delete()
