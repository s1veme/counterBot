from aiogram import types
from aiogram.dispatcher.filters import Command

from loader import dp


@dp.message_handler(Command(commands=['add'], prefix='/'))
async def add_score(message: Message):
    pass
