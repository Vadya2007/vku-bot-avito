import os
import threading
import telebot
from flask import Flask

# =====================
# 1️⃣ TELEGRAM BOT
# =====================
TOKEN = os.getenv("TOKEN")
if not TOKEN:
    raise ValueError("Telegram TOKEN не найден! Проверь переменные окружения.")

bot = telebot.TeleBot(TOKEN)

# Пример команды
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.send_message(message.chat.id, "Привет! Бот работает ✅")

# =====================
# 2️⃣ FLASK PING-SERVER
# =====================
app = Flask("")

@app.route("/")
def home():
    return "Bot is running!"

def run_flask():
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)

# =====================
# 3️⃣ ЗАПУСК ОБОИХ
# =====================
# Flask в отдельном потоке
threading.Thread(target=run_flask).start()

# Телеграм-бот
bot.infinity_polling()
