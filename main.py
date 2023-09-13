import telebot
import text 
import config
from additional import markups
from database import db_utils

token = config.token
# token for webfitness
# 6105304109:AAFDdyun3EeWayQoycbj2eHlP-du6emt5R8
bot = telebot.TeleBot(token)
print("Bot is working")


# Create handlers for interacting with users 
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.send_message(message.from_user.id, text.welcomeText)


@bot.message_handler(commands=['reg'])
def create_user(message):
    bot.send_message(message.from_user.id, text=text.regText, reply_markup=markups.phone_number_markup())

@bot.message_handler(content_types=['contact'])
def contact(message):
    # TODO: Request to db
    print("message: ", message)


@bot.message_handler(content_types=['text'])
def text_react(message):
    chat_id = message.from_user.id
    # Checking auth 
    if message.text in text.mainMarkupText:
        if message.text == "История операций":
            # TODO: Request to db 
            print("Not Done")
        if message.text == "Списать бонусы":
            #TODO : Request to db
            print("Not Done")
        if message.text == "Остаток бонусов":
            # TODO: Request to db
            print("Not Done")
    
    
    


bot.polling(none_stop=True)