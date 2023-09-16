import telebot
from text import mainMarkupText, registerButtonText


def phone_number_markup():
    keyboard = telebot.types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    button_phone = telebot.types.KeyboardButton(text="Отправить номер", request_contact=True)
    keyboard.add(button_phone)
    return keyboard


def menu_markup():
    values = mainMarkupText
    keyboard = telebot.types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    for value in values:
        button = telebot.types.KeyboardButton(text=value)
        keyboard.add(button)
    return keyboard\
    

def register_martkup():
    # values = ["Зарегистрироваться"]
    # keyboard = telebot.types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    # for value in values:
    #     button = telebot.types.KeyboardButton(text=value)
    #     keyboard.add(button)
    # return keyboard
    keyboard = telebot.types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    button_reg = telebot.types.KeyboardButton(text=registerButtonText)
    keyboard.add(button_reg)
    return keyboard
