import os

import telebot
from PIL import Image
from telebot import types

from config import Config

bot = telebot.TeleBot(Config.BOT_TOKEN)


@bot.message_handler(commands=['get_latest_photo'])
def get_latest_photo(message):
    photo = Image.open(
        os.path.join(
            os.getcwd(),
            'data', 'pictures', 'selfie.jpg'
        )
    )

    bot.send_message(message.chat.id, 'Одно из последних фото')
    bot.send_photo(message.chat.id, photo)


@bot.message_handler(commands=['get_high_school_photo'])
def get_high_school_photo(message):
    photo = Image.open(
        os.path.join(
            os.getcwd(),
            'data', 'pictures', 'highschool.jpg'
        )
    )

    bot.send_message(
        message.chat.id,
        'Фото брата, так как свое со школы не нашел)',
        )
    bot.send_photo(message.chat.id, photo)


@bot.message_handler(commands=['hobby'])
def get_hobby_descr(message):
    bot.send_message(message.chat.id, Config.TENNIS)

    photo = Image.open(
        os.path.join(
            os.getcwd(),
            'data', 'pictures', 'tennis.jpg'
        )
    )
    bot.send_photo(message.chat.id, photo)


@bot.message_handler(commands=['repository'])
def get_repo_link(message):
    bot.send_message(message.chat.id, 'Исходный код можно глянуть тут:')
    bot.send_message(
        message.chat.id,
        'https://github.com/KurtVobain/practicum-telegram-bot'
    )


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
        voice = open(
            os.path.join(
                os.getcwd(),
                'data', 'audio', 'gpt.aac'
            ),
            'rb'
        )
        bot.send_voice(call.message.chat.id, voice, caption='Про ChatGPT')

    elif call.data == '2':
        voice = open(
            os.path.join(
                os.getcwd(),
                'data', 'audio', 'sqlnosql.aac'
            ),
            'rb'
        )
        bot.send_voice(call.message.chat.id, voice, caption='SQL vs NoSQL')

    elif call.data == '3':
        voice = open(
            os.path.join(
                os.getcwd(),
                'data', 'audio', 'love.aac'
            ),
            'rb'
        )
        bot.send_voice(call.message.chat.id, voice, caption='Первая любовь')


@bot.message_handler(commands=['send_message_to_evgenii'])
def send_message_to_evgenii(message):
    bot.send_message(Config.MY_CHAT_ID, message.text)
    bot.send_message(message.chat.id, 'Сообщение отправлено :)')


if __name__ == '__main__':
    bot.infinity_polling()
