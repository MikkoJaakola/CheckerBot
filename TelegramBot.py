import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler
from CheckWebsite import getModifiedTime
import time

# INSTALL pip install python-telegram-bot --upgrade

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)



async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="Moro moro")

async def date(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="TOAS status checking started...")
    time_date = getModifiedTime()
    while True:
        time.sleep(60)
        current_date = getModifiedTime()
        print("***************")
        print("***************")
        print("old date:")
        print(time_date)
        print(" ********** ")
        print("new accuired date:")
        print(current_date)
        print("***************")
        print("***************")

        if current_date != time_date:
            await context.bot.send_message(chat_id=update.effective_chat.id, text=current_date)
            await context.bot.send_message(chat_id=update.effective_chat.id, text="site has been updated")
            print("***************")
            print("***************")
            print("TG message sent")
            print("***************")
            print("***************")
            time_date = current_date
            time.sleep(10)


            


if __name__ == '__main__':
    application = ApplicationBuilder().token('TOKEN_HERE').build()
    
    start_handler = CommandHandler('start', start)
    application.add_handler(start_handler)

    date_handler = CommandHandler('date', date)
    application.add_handler(date_handler)

    testloop_handler = CommandHandler('testloop', testloop)
    application.add_handler(testloop_handler)
    
    application.run_polling()