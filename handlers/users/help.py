from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandHelp

from loader import dp


@dp.message_handler(CommandHelp())
async def bot_help(message: types.Message):
    text = ("Список команд: ",
            "/add - добавить балл",
            "/rm - снять балл",
            "/myscore - посмотреть свои баллы",
            "/allscore - посмотреть баллы всех людей")
    
    await message.answer("\n".join(text))
