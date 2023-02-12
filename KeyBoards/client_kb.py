from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

b1 = KeyboardButton('/add')
b2 = KeyboardButton('/statistic')

kb_client = ReplyKeyboardMarkup(resize_keyboard=True)

kb_client.add(b1).insert(b2)

a95 = KeyboardButton('A95')
a92 = KeyboardButton('A92')
dizel = KeyboardButton('ДП')
lpg = KeyboardButton('ГАЗ')

kb_fuel = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
kb_fuel.add(a95).insert(a92).add(dizel).insert(lpg)

hrivna = KeyboardButton('UAH')
zlotiy = KeyboardButton('PLZ')
dollar = KeyboardButton('USD')

kb_money = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
kb_money.row(hrivna, zlotiy, dollar)
