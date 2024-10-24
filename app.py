import random
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler

def load_messages(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return [line.strip() for line in file if line.strip()]


messages = load_messages('messages.txt')


async def random_message(update: Update, context):
    await update.message.reply_text(random.choice(messages))


if __name__ == '__main__':
    app = ApplicationBuilder().token('7725384860:AAHRw2voiUxLjhj1ZdUhapAhBX5O8gEIkCc').build()
    app.add_handler(CommandHandler("random", random_message))
    app.run_polling()