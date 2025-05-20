import os
import telebot

# توکن از متغیر محیطی میاد
TOKEN = os.getenv("BOT_TOKEN")
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "سلام Ashkan! ✅ رباتت اجرا شد.")

@bot.message_handler(func=lambda m: True)
def echo_all(message):
    bot.reply_to(message, f"تو گفتی: {message.text}")

bot.infinity_polling()
