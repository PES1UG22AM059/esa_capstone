import logging
from telegram import Update
from telegram.ext import Updater, MessageHandler, Filters, CallbackContext

# SUPER-VERBOSE LOGGING SETUP
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('debug.log'),
        logging.StreamHandler()
    ]
)

TOKEN = "8173338125:AAHhqToLjhSy5Fd6xphq_iwaKNFF0CnJg1g"

def debug_message(update: Update, context: CallbackContext):
    chat_id = update.message.chat_id
    user = update.message.from_user
    
    # This will appear in BOTH console and debug.log file
    logging.info("\n" + "="*40)
    logging.info(f"SUCCESS! CHAT ID FOUND: {chat_id}")
    logging.info(f"User: {user.first_name} (ID: {user.id})")
    logging.info("="*40 + "\n")
    
    update.message.reply_text(
        f"🔍 Debug Info:\n"
        f"Chat ID: {chat_id}\n"
        f"Your Name: {user.first_name}\n"
        f"Full User: {user}"
    )

if __name__ == "__main__":
    print("=== DEBUG MODE ACTIVATED ===")
    print("1. Send ANY message to your bot in Telegram")
    print("2. Check both console AND debug.log file")
    print("="*30)
    
    updater = Updater(TOKEN)
    updater.dispatcher.add_handler(MessageHandler(Filters.all, debug_message))
    
    # Keep the window open
    updater.start_polling()
    input("Press Enter to stop the bot...\n")
    updater.stop()