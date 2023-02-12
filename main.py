from aiogram.utils import executor
from create_bot import dp
from data_base import sqlite_db


def on_startup():
    print('Бот вийшов у онлайн')
    sqlite_db.sql_start()

from handlers import client, user_info_data

on_startup()
user_info_data.register_hendlers_user_info(dp)
client.register_handlers_client(dp)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
