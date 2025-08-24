from telegram import Update
from telegram.ext import ContextTypes


async def get_data(update: Update, context: ContextTypes.DEFAULT_TYPE):
     user_data = {
        "telegram_id": str(update.effective_user.id),
        "username": update.effective_user.username,
        "first_name": update.effective_user.first_name,
        "last_name": update.effective_user.last_name,
        "chat_id": str(update.effective_chat.id)
        }
     return user_data