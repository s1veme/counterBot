from aiogram import types
from aiogram.dispatcher.filters import BoundFilter


class IsReply(BoundFilter):

    async def check(self, message: types.Message):
        pass
