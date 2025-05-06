import os
import telebot
from flask import Flask, request

TOKEN = os.getenv("BOT_TOKEN")
bot = telebot.TeleBot(TOKEN)
app = Flask(__name__)

@bot.message_handler(commands=["start"])
def send_welcome(message):
    bot.send_message(message.chat.id, "Привет! Я Telegram-бот на Render 🚀")

@app.route("/", methods=["GET", "POST"])
def webhook():
    if request.method == "POST":
        bot.process_new_updates([telebot.types.Update.de_json(request.stream.read().decode("utf-8"))])
        return "ok", 200
    return "Hello from bot!", 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
