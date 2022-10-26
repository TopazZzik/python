from telegram import Update, Chat, Bot
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes,  MessageHandler, filters
from bot_commands import *

app = ApplicationBuilder().token("5742593421:AAGOqKo_h8YtCP4tvx3R-56HSdMMb5mhQ24").build()

app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("play", play))

app.run_polling()