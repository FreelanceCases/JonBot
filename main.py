import telebot
import threading
import text 
import config
from additional import markups
from database import db_utils
from prettier import bonus_balance_formatter, bonus_history_formatter


token = config.token
bot = telebot.TeleBot(token)
print("Bot is working")




    


# Create handlers for interacting with users d
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.send_message(message.from_user.id, text.welcomeText, reply_markup=markups.register_martkup())


@bot.message_handler(commands=['reg'])
def create_user(message):
    bot.send_message(message.from_user.id, text=text.regText, reply_markup=markups.phone_number_markup())

@bot.message_handler(content_types=['contact'])
def contact(message):
    if message.contact.phone_number:
        number = message.contact.phone_number
        chat_id = message.from_user.id
        if db_utils.check_user(number=number) == False:
            db_utils.create_user(number=number, chat_id=chat_id)
            bot.send_message(chat_id=chat_id, text=text.nonauthText, reply_markup=markups.menu_markup())
        else:
            bot.send_message(chat_id=chat_id, text=text.authText + message.contact.first_name + "!", reply_markup=markups.menu_markup())


@bot.message_handler(content_types=['text'])
def text_react(message):
    if message.text == text.registerButtonText:
        bot.send_message(message.from_user.id, text=text.regText, reply_markup=markups.phone_number_markup())

    chat_id = message.from_user.id
    # Checking auth 
    if db_utils.check_user_by_chat_id(chat_id=chat_id) is None:
        bot.send_message(chat_id=chat_id, text="Пожалуйста, дождитесь подтверждения администратора!", reply_markup=markups.menu_markup())
    else:
        if message.text in text.mainMarkupText:
            
            if message.text == "История операций":
                bot.send_message(chat_id=chat_id, text=bonus_history_formatter(db_utils.bonus_history(chat_id)), reply_markup=markups.menu_markup())
            
            if message.text == "Остаток бонусов":
                bot.send_message(chat_id=chat_id, text=bonus_balance_formatter(db_utils.bonus_balance(chat_id)), reply_markup=markups.menu_markup())



def code_sender():
    arr = db_utils.get_codes()
    for (id, code, date) in arr:
        if date is None:
            chat_id = db_utils.get_chat_id_by_id(id)
            db_utils.update_timestamp(id)
            bot.send_message(chat_id=chat_id, text="Код подтверждения: " + str(code), reply_markup=markups.menu_markup())


def broadcast_sender():
    arr = db_utils.get_broadcast()
    for (id, date, body, image) in arr:
        if date is None:
            chat_id = db_utils.get_chat_id_by_id(id)
            if image is None:
                bot.send_message(chat_id=chat_id, text=body, reply_markup=markups.menu_markup())
            else: 
                bot.send_photo(chat_id=chat_id, photo=image, caption=body)
            db_utils.update_timestamp_for_broadcast(id)


# For multythreading
def t1_func():
    while True:
        code_sender()

def t2_func():
    bot.polling(none_stop=True)


def t3_func():
    while True:
        broadcast_sender()


t1 = threading.Thread(target=t1_func)
t2 = threading.Thread(target=t2_func)
t3 = threading.Thread(target=t3_func)


t1.daemon = True
t3.daemon = True
t1.start()
t2.start()
t3.start()









