from aiogram import types, Dispatcher
from create_bot import dp, bot
from KeyBoards import kb_client

async def command_start(message: types.Message):
    await bot.send_message(message.from_user.id, 'Доброго дня', reply_markup=kb_client)

#@dp.message_handler(commands='add')
async def command_add(message: types.Message):
    await message.answer('функція додавання данних')

#@dp.message_handler(commands='statistic')
async def command_stat(message: types.Message):
    await message.answer('функція статистики')

def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(command_start, commands=['start'])
    dp.register_message_handler(command_add, commands=['add'])
    dp.register_message_handler(command_stat, commands=['statistic'])
