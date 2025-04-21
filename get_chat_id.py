import logging
from telegram.ext import Updater, MessageHandler, Filters

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

TOKEN = "8173338125:AAHhqToLjhSy5Fd6xphq_iwaKNFF0CnJg1g"

def echo(update, context):
    chat_id = update.message.chat_id
    first_name = update.message.from_user.first_name
    print("\n" + "="*50)
    print(f"SUCCESS! Your Chat ID: {chat_id}")
    print(f"User: {first_name}")
    print("="*50 + "\n")
    update.message.reply_text(f"Your Chat ID is: {chat_id}")

updater = Updater(TOKEN)
updater.dispatcher.add_handler(MessageHandler(Filters.all, echo))
print("Bot is listening... Send ANY message to your bot in Telegram now!")
updater.start_polling()
updater.idle()