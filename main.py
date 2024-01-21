import os
import telebot
from pytube import YouTube


TOKEN = '6765142766:AAF1x6U7NIR0rVIdZowyuZRFdsz8ba23-Tg'

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start'])
def handle_start(message):
    bot.send_message(message.chat.id, "Sup, send me your stupid video and may be I'll download them for ya..")


@bot.message_handler(func=lambda message: True)
def handle_message(message):
    try:

        video_url = message.text

        # downloadin' a fuckin funny cat video
        yt = YouTube(video_url)
        video = yt.streams.first()
        video.download()

        # sendin' video to user
        bot.send_video(message.chat.id, open(video.default_filename, 'rb'))

       
        os.remove(video.default_filename)

    except Exception as e:
        #an err scenario
        bot.reply_to(message, "Oops, an error appears while downloading. Try again please")

# Запускаем бота
bot.polling()