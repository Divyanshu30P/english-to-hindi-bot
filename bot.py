import telebot
import requests
import os

TOKEN = os.getenv("BOT_TOKEN")
bot = telebot.TeleBot(TOKEN)

# MyMemory free translation API
def translate_en_to_hi(text):
    url = f"https://api.mymemory.translated.net/get?q={text}&langpair=en|hi"
    r = requests.get(url).json()
    return r["responseData"]["translatedText"]

@bot.message_handler(commands=['start'])
def welcome(msg):
    bot.reply_to(msg, "👋 Send any English message and I'll translate it to Hindi!")

@bot.message_handler(func=lambda m: True)
def translate(msg):
    en_text = msg.text
    hi_text = translate_en_to_hi(en_text)
    bot.reply_to(msg, f"🇮🇳 *Hindi Translation:*\n{hi_text}", parse_mode="Markdown")

bot.polling(none_stop=True)
