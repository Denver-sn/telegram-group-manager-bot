import time
import telebot
from telebot import types
import os

TOKEN = os.environ['TOKEN'] # > SET IT IN HEROKU VAR

bot = telebot.TeleBot(TOKEN)

markup_main = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
link = "Chat Link 🔗"
chat_id = "Chat ID 🌐"
markup_main.add(link, chat_id)

@bot.message_handler(commands=['start'])
def starting_point(message):
    markup = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    
    bot.send_message(message.chat.id, f"Hello welcome to Denver Assistant v2.0, i'm a Group Manager", reply_markup=markup_main)


@bot.message_handler(content_types=['text'])
def send_text(message):
    if "https://t.me/" in message.text: # CHECK IF MESSAGE IS A TELEGRAM CHAT LINK
        message_i = message.id
        bot.delete_message(message.chat.id, message_i)
    else:
        pass
    if message.text == 'Chat Link 🔗':
        chat_l= bot.get_chat(message.chat.id).invite_link
        print(chat_l)
        bot.reply_to(message, f"CHAT LINK: {chat_l}", parse_mode='HTML', reply_markup=markup_main)
        
    elif message.text == 'Chat ID 🌐':
        chat_l= message.chat.id
        bot.reply_to(message, f"<b>CHAT ID:</b>{chat_l}", parse_mode='HTML', reply_markup=markup_main)
 
while True:
    try:
        bot.polling(non_stop=True)
    except:
        time.sleep(30)
