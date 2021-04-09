from aiogram import types
from aiogram.dispatcher.filters import Command

from filters import IsGroup

from loader import dp, bot, db


@dp.message_handler(IsGroup(), Command(commands=["add"], prefixes="/"), is_reply=True, user_can_restrict_members=True)
async def add_score(message: types.Message):
    """ Добавляет один балл пользователю """

    member_username = message.reply_to_message.from_user.username
    member_id = message.reply_to_message.from_user.id

    await message.answer(f"Пользователю {member_username} добавлен 1 балл")

    db.add_score_user(member_id, member_username)

    await message.delete()


@dp.message_handler(IsGroup(), Command(commands=["rm"], prefixes="/"), is_reply=True, user_can_restrict_members=True)
async def remove_score(message: types.Message):
    """ Удаляет один балл пользователю """

    member_username = message.reply_to_message.from_user.username
    member_id = message.reply_to_message.from_user.id

    await message.answer(f"Пользователю {member_username} удалён 1 балл")

    db.take_score_user(member_id, member_username)

    await message.delete()


@dp.message_handler(IsGroup(), Command(commands=["allscore"], prefixes="/"), is_reply=True, user_can_restrict_members=True)
async def users_score(message: types.Message):
    """ Отправляет всех пользователей и их очки в чат """

    data = db.get_score_all_user()

    for username, score in data:
        text += f"@{username} - {score}\n"

    await message.answer(text)

    await message.delete()
