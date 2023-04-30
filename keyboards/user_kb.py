from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove

b1 = KeyboardButton("New booking")
kb_register = ReplyKeyboardMarkup(resize_keyboard=True)
kb_register.add(b1)
