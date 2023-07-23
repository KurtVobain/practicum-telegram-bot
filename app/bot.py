import os

import telebot
from PIL import Image
from telebot import types

from config import Config

bot = telebot.TeleBot(Config.BOT_TOKEN)


@bot.message_handler(commands=['get_latest_photo'])
def get_latest_photo(message):
    photo = Image.open(
        os.path.join(os.getcwd(), 'data\\pictures\\selfie.jpg')
    )

    bot.send_message(message.chat.id, 'Одно из последних фото')
    bot.send_photo(message.chat.id, photo)


@bot.message_handler(commands=['get_high_school_photo'])
def get_high_school_photo(message):
    photo = Image.open(
        os.path.join(os.getcwd(), 'data\\pictures\\highschool.jpg')
    )

    bot.send_message(
        message.chat.id,
        'Фото брата, так как свое со школы не нашел)',
        )
    bot.send_photo(message.chat.id, photo)


@bot.message_handler(commands=['hobby'])
def get_hobby_descr(message):
    bot.send_message(message.chat.id, 'Текст о теннисе')


@bot.message_handler(commands=['repository'])
def get_repo_link(message):
    bot.send_message(message.chat.id, 'Ссылка')


@bot.message_handler(commands=['listen_audio'])
def get_audio_selection(message):
    keyboard = types.InlineKeyboardMarkup()
    first_audio_button = types.InlineKeyboardButton(
        text='Что такое GPT?', callback_data='1'
    )

    second_audio_button = types.InlineKeyboardButton(
        text='SQL и NoSQL - в чем разница?', callback_data='2'
    )

    third_audio_button = types.InlineKeyboardButton(
        text='Первая любовь', callback_data='3'
    )

    keyboard.add(first_audio_button, second_audio_button, third_audio_button)
    bot.send_message(message.chat.id, 'Аудио на выбор:', reply_markup=keyboard)


@bot.callback_query_handler(func=lambda call: True)
def callback_audio_choice(call):
    if call.data == '1':
        bot.send_message(call.message.chat.id, 'Audio 1')
    elif call.data == '2':
        bot.send_message(call.message.chat.id, 'Audio 2')
    elif call.data == '3':
        bot.send_message(call.message.chat.id, 'Audio 3')


if __name__ == '__main__':
    bot.infinity_polling()
