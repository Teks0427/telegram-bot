from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # Check if there's a custom parameter
    if context.args:
        if context.args[0] == '88gtchat':
            # Send the message with a hyperlink using HTML
            await update.message.reply_text(
                '<a href="https://bit.ly/88gtchat"><strong>Click here for 88GT Support</a></strong>',
                parse_mode='HTML'
            )
        else:
            await update.message.reply_text("Unknown command.")
    else:
        await update.message.reply_text("Hello! Please click on HELP ME! to proceed")

# Initialize the Application with your bot token
application = Application.builder().token("7406758697:AAG7Ix-8psDbKqpB7-EY95n_61cutcGCuHs").build()

# Register the start command handler
application.add_handler(CommandHandler("start", start))

# Start the Bot
application.run_polling()
