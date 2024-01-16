import os

from aiogram import Bot, Dispatcher
from aiogram.filters import Command
from aiogram.types import Message
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv('TG_TOKEN')

# Create a bot and dispatcher objects
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()


# This handler will raise on command "/start"
@dp.message(Command(commands=["start"]))
async def process_start_command(message: Message):
    await message.answer('Hello!\nMy name is Echo-Bot!\nSend me something')

    # If you want to send message for any other chats of for some contacts you should use:
    # await bot.send_message(chat_id='ID or chat name', text='Some text')
    # To the same chat:
    # await bot.send_message(message.chat.id, message.text)


# This handler will raise on command "/help"
@dp.message(Command(commands=['help']))
async def process_help_command(message: Message):
    await message.answer(
        'Send me something and as my answer'
        'I will send your message to you'
    )


# This handler will raise on any of your text messages,
# exclude commands "/start" и "/help"
@dp.message()
async def send_echo(message: Message):
    await message.reply(text=message.text)


if __name__ == '__main__':
    dp.run_polling(bot)
