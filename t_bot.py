import telebot
import requests
from keyboa import Keyboa

from get_temperature import get_temp
from datetime import datetime
from time import sleep

API_TOKEN = "5419870488:AAHzm909pIQMNmKkO0yGxFLkGvhOrjtZzj4"

bot = telebot.TeleBot(API_TOKEN)

city = ['Kyiv', 'Warsaw', 'Madrid', 'Milan', 'Lund']
keyboard_callback = str(telebot.types.InlineKeyboardMarkup)
keyboard = Keyboa(items=city, items_in_row=2, back_marker=keyboard_callback)

@bot.message_handler(commands=['help', 'start'])
def send_welcome(message):
    bot.reply_to(message, f"Hi {message.chat.id}. \nIt's a temperature bot from \n@Sanya_Kalash \nNow {datetime.now().strftime('%H:%M')} temperature is {get_temp('kyiv')}°C in Kyiv.")
    print(message.chat.id, datetime.now().strftime('%H:%M:%S'), str(telebot.types.User.full_name))
    bot.send_message(chat_id=message.chat.id, text="Choose city:", reply_markup=keyboard())

    @bot.callback_query_handler(func=lambda call: True)
    def answer(call):
        choosen_city = str(call.data).split('<')[0]
        send_regular_message(message.chat.id, choosen_city)

def send_regular_message(id, city):
    while True:
        bot.send_message(chat_id=id, text=f"{datetime.now().strftime('%H:%M')}, {str(get_temp(city.lower())) + '°C'} in {city}.")
        sleep(600)

bot.infinity_polling()