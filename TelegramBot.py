import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler
from CheckWebsite import getModifiedTime

# INSTALL pip install python-telegram-bot --upgrade

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

time = getModifiedTime()

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="Moro moro")

async def date(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text=time)


if __name__ == '__main__':
    application = ApplicationBuilder().token('').build()
    
    start_handler = CommandHandler('start', start)
    application.add_handler(start_handler)

    date_handler = CommandHandler('date', date)
    application.add_handler(date_handler)
    
    application.run_polling()