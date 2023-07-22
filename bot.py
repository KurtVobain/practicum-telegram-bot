from PIL import Image

import telebot
from telebot import types

import config
import db_handler

bot = telebot.TeleBot(config.bot_token)


@bot.message_handler(commands=['get_latest_photo'])
def cmd_start(message):
        photo = Image.open('.\data\pictures\photo_5194960298715498148_y.jpg')
        bot.send_message(message.chat.id, 'Селфи не нашлось)')
        bot.send_photo(message.chat.id, photo)

@bot.message_handler(commands=['get_high_school_photo'])
def cmd_start(message):
        photo = Image.open('.\data\pictures\photo_5194960298715498148_y.jpg')
        bot.send_photo(message.chat.id, photo)

@bot.message_handler(commands=['hobby'])
def cmd_start(message):
    bot.send_message(message.chat.id, 'Текст о теннисе')

@bot.message_handler(commands=['repository'])
def cmd_start(message):
    bot.send_message(message.chat.id, 'Ссылка')

@bot.message_handler(commands=['listen_audio'])
def cmd_start(message):
    keyboard = types.InlineKeyboardMarkup()
    callback_button = types.InlineKeyboardButton(text='1', callback_data="1")
    callback_button_2 = types.InlineKeyboardButton(text='2', callback_data="2")
    callback_button_3 = types.InlineKeyboardButton(text='3', callback_data="3")
    keyboard.add(callback_button, callback_button_2, callback_button_3)
    bot.send_message(message.chat.id, 'Аудио на выбор:', reply_markup=keyboard)
    db_handler.set_state(message.chat.id, config.States.S_CHOSE_AUDIO.value)


@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    if call.data == '1':
        bot.send_message(call.message.chat.id, 'Audio 1')
    elif call.data == '2':
        bot.send_message(call.message.chat.id, 'Audio 2')
    elif call.data == '3':
        bot.send_message(call.message.chat.id, 'Audio 3')


if __name__ == '__main__':
    bot.infinity_polling()
