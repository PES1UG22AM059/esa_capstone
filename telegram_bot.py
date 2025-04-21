import os
from telegram import Bot, Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
import logging
from datetime import datetime
import time

# Configuration
TOKEN = os.getenv('TELEGRAM_TOKEN', '8173338125:AAHhqToLjhSy5Fd6xphq_iwaKNFF0CnJg1g')
CHAT_ID = 1851147300  # Your verified chat ID
LOG_FILE = 'bot.log'

# Logging Setup
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler(LOG_FILE),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

def start(update: Update, context: CallbackContext):
    """Welcome message handler"""
    user = update.message.from_user
    logger.info(f"New user: {user.first_name} (ID: {user.id})")
    update.message.reply_text(
        "🟢 Elephant Detection Bot Activated!\n"
        "I will alert you when elephants are detected.\n\n"
        f"Your Chat ID: {update.message.chat_id}"
    )

def send_alert(image_path=None, caption="🚨 Elephant Detected!", max_retries=3):
    """Send alert with retry logic"""
    bot = Bot(token=TOKEN)
    for attempt in range(max_retries):
        try:
            if image_path and os.path.exists(image_path):
                with open(image_path, 'rb') as photo:
                    bot.send_photo(
                        chat_id=CHAT_ID,
                        photo=photo,
                        caption=f"{caption}\n{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
                    )
            else:
                bot.send_message(
                    chat_id=CHAT_ID,
                    text=f"{caption}\n{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
                )
            return True
        except Exception as e:
            logger.error(f"Attempt {attempt + 1} failed: {str(e)}")
            time.sleep(2)
    return False

def main():
    """Start the bot"""
    try:
        updater = Updater(TOKEN, use_context=True)
        dp = updater.dispatcher

        # Command handlers
        dp.add_handler(CommandHandler("start", start))
        dp.add_handler(CommandHandler("help", start))  # Reuse start for help

        logger.info("Bot started successfully")
        updater.start_polling()
        updater.idle()
    except Exception as e:
        logger.critical(f"Bot failed to start: {str(e)}")

if __name__ == "__main__":
    main()