import logging
from telegram.ext import Updater, MessageHandler, Filters

# Set up logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                     level=logging.INFO)

# Define a function to handle incoming messages
def echo(update, context):
    """Echo the user message."""
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text=update.message.text)

def main():
    # Create an instance of the Updater class and replace 'YOUR_TOKEN' with your Telegram bot token
    updater = Updater(token='6976861078:AAFXIsy1dfum1-p2RHDb6d4Hc-ILP-qDuwE', use_context=True)

    # Get the dispatcher to register handlers
    dispatcher = updater.dispatcher

    # Register the echo function as a message handler
    echo_handler = MessageHandler(Filters.text & (~Filters.command), echo)
    dispatcher.add_handler(echo_handler)

    # Start the bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C or the process receives SIGINT, SIGTERM or SIGABRT
    updater.idle()

# Run the main function to start the bot
if __name__ == '__main__':
    main()
