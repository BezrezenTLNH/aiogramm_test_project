import os
import random

from aiogram import Bot, Dispatcher, F
from aiogram.filters import Command, CommandStart
from aiogram.types import Message
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv('TG_TOKEN')

# Create a bot and dispatcher objects
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

# Qty of tries that user can use
ATTEMPTS = 5

# Dictionary that contains user data without DB
user = {'in_game': False,
        'secret_number': None,
        'attempts': None,
        'total_games': 0,
        'wins': 0}


# Function that create a random number from 1 to 100
def get_random_number() -> int:
    return random.randint(1, 100)


# This handler will trigger on command "/start"
@dp.message(CommandStart())
async def process_start_command(message: Message):
    await message.answer(
        'Hi!\nLets play a game "Guess number"?\n\n'
        'To get a play rules and the list of a available'
        'commands - send command /help'
    )


# This handler will trigger on command "/help"
@dp.message(Command(commands='help'))
async def process_help_command(message: Message):
    await message.answer(
        f"Rules of the game:\n\nI guess a number from 1 to 100, "
        f"you need to guess it\nYou have {ATTEMPTS} "
        f"attempts\n\nAvailable commands:\n/help - rules "
        f"games and list of commands\n/cancel - quit the game\n"
        f"/stat - view statistics\n\nLet's play?")


# This handler will trigger on command "/start"
@dp.message(Command(commands='start'))
async def process_start_command(message: Message):
    await message.answer(
        f"Total played games: {user['total_games']}\n"
        f"Won games: {user['wins']}"
    )


# This handler will trigger on command "/cancel"
@dp.message(Command(commands='cancel'))
async def process_cancel_command(message: Message):
    if user['in_game']:
        user['in_game'] = False
        await message.answer(
            "You're leave the game. If you want to play "
            "again - text me about it"
        )
    else:
        await message.answer(
            "We're not playing at this time. "
            "Lets start?"
        )


# This handler will trigger when user is agreed to play
@dp.message(F.text.lower().in_(['yes', 'ye', 'lets play', 'play',
                                'game', 'want to play']))
async def process_positive_answer(message: Message):
    if not user['in_game']:
        user['in_game'] = True
        user['secret_number'] = get_random_number()
        user['attempts'] = ATTEMPTS
        await message.answer(
            'Hurray!\n\nI wished a number rom 1 to 100, '
            'try to guess!'
        )
    else:
        await message.answer(
            "While we're playing the game, I can"
            "only react to numbers from 1 to 100"
            "and the commands /cancel and /stat"
        )


# This handler will trigger if the user refuses to play the game
@dp.message(F.text.lower().in_(['нет', 'не', 'не хочу', 'не буду']))
async def process_negative_answer(message: Message):
    if not user['in_game']:
        await message.answer(
            "It's a pity :(\n\nIf you want to play, just "
            "write about it"
        )
    else:
        await message.answer(
            "We're playing with you now. Please, "
            "send numbers from 1 to 100"
        )

