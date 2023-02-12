from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram import types, Dispatcher
from aiogram.dispatcher.filters import Text
from KeyBoards import kb_fuel, kb_money
from data_base import sqlite_db


class FSMUserInfo(StatesGroup):
    name = State()
    car = State()
    fuel = State()
    money = State()

#Start dialog
#@dp.message_handler(commands='/start', state=None)
async def cm_start(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['user_id'] = message.from_user.id
    await FSMUserInfo.name.set()
    await message.reply('Введіть своє імʼя')

async def cancel_handler(message: types.Message, state: FSMContext):
    current_state = await state.get_state()
    if current_state is None:
        return
    await state.finish()
    await message.reply('OK')

#1st answer
#@dp.message_handler(state=FSMUserInfo.name)
async def load_name(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['name'] = message.text
    await FSMUserInfo.next()
    await message.reply('Введіть марку та модель вашого авто')

#2nd answer
#@dp.message_handler(state=FSMUserInfo.car)
async def load_car(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['car'] = message.text
    await FSMUserInfo.next()
    await message.reply('Введіть тип пального', reply_markup=kb_fuel)

#@dp.message_handler(state=FSMUserInfo.fuel)
async def load_fuel(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['fuel'] = message.text
    await FSMUserInfo.next()
    await message.reply('Введіть валюту розрахунку', reply_markup=kb_money)

#@dp.message_handler(state=FSMUserInfo.money)
async def load_money(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['money'] = message.text

    await sqlite_db.sql_add_command(state, message.from_user.id)
    await message.answer('Дуже добре, ваші данні збережено 👍')
    await state.finish()


def register_hendlers_user_info(dp: Dispatcher):
    dp.register_message_handler(cm_start, commands=['start'], state=None)
    dp.register_message_handler(cancel_handler, state="*", commands='скасування')
    dp.register_message_handler(cancel_handler, Text(equals='скасування', ignore_case=True), state="*")
    dp.register_message_handler(load_name, state=FSMUserInfo.name)
    dp.register_message_handler(load_car, state=FSMUserInfo.car)
    dp.register_message_handler(load_fuel, state=FSMUserInfo.fuel)
    dp.register_message_handler(load_money, state=FSMUserInfo.money)
