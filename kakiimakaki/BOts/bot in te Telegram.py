import telebot
import datetime
from pyexpat.errors import messages

bot = telebot.TeleBot("7799775236:AAHYPJxOBWTQiGkxb5RtMCZ_FIGOnjCryWs")
keybord1 = telebot.types.ReplyKeyboardMarkup (True)
keybord1.row('Привет', 'Пока')
keybord1.row('Дата', 'Время', "День недели")
data_time = datetime.date.today()
@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, "Привет, давай начинать!", reply_markup=keybord1)
@bot.message_handler(content_types=['text'])
def send_text(message):
    if message.text.lower() == "привет":
        bot.send_message(message.chat.id, 'И тебе привет!')
    elif message.text.lower() == "пока":
        bot.send_message(message.chat.id, 'И тебе пока')
    elif message.text.lower() == "дата":
        bot.send_message(message.chat.id, datetime.datetime.today().strftime("%d.%m.%Y"))
    elif message.text.lower() == "время":
        bot.send_message(message.chat.id, datetime.datetime.today().strftime("%H:%M:%S"))
    elif message.text.lower() == "день недели":
        bot.send_message(message.chat.id, datetime.datetime.today().strftime("%A"))
bot.polling()
