from aiogram import executor

from loguru import logger

from loader import dp, db
import middlewares
import filters

filters.setup(dp)
import handlers
from utils.notify_admins import on_startup_notify


async def on_startup(dispatcher):
    await on_startup_notify(dispatcher)
    
    try:
        db.create_table_users()
    except Exception as err:
        logger.error(err)
        

if __name__ == '__main__':
    executor.start_polling(dp, on_startup=on_startup)
