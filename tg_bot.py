from haiku_bot import get_haiku
import telebot
import os

token = os.environ.get('TGTOKEN')
bot = telebot.TeleBot(token)


@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    haiku = get_haiku(message.text.lower())
    if haiku:
        bot.send_message(message.from_user.id, haiku)

bot.polling(none_stop=True)

