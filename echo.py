from telebot.async_telebot import AsyncTeleBot
import asyncio

API_TOKEN = "5419870488:AAHzm909pIQMNmKkO0yGxFLkGvhOrjtZzj4"

bot = AsyncTeleBot(API_TOKEN)

@bot.message_handler(commands=['help', 'start'])
async def send_welcome(message):
    await bot.reply_to(message, """\
Hi there, I am EchoBot.
I am here to echo your kind words back to you. Just say anything nice and I'll say the exact same thing to you!\
""")


# Handle all other messages with content_type 'text' (content_types defaults to ['text'])
@bot.message_handler(func=lambda message: True)
async def echo_message(message):
    await bot.reply_to(message, message.text)

bot.polling()