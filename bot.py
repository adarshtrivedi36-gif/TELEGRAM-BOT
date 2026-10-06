import os from telegram import Update from telegram.ext import Application, CommandHandler, ContextTypes BOT_TOKEN = os.getenv('BOT_TOKEN') async def start(update: Update, context: ContextTypes.DEFAULT_TYPE): await update.message.reply_text


'Welcome! Referral reward: ₹5 per successful referral. Minimum withdrawal: ₹50.'


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE): await update.message.reply_text 'Commands:\n/start - Start the bot\n/help - Help' def main(): if not BOT_TOKEN: raise RuntimeError 'BOT_TOKEN is not set' app = Application.builder .token(BOT_TOKEN) .build() app .add_handler (CommandHandler("start", start)) app .add_handler (CommandHandler("help", help_command)) app .run_polling() if **name** == '**main**': main()
