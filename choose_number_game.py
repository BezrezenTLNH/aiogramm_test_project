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

# Dictionary that contains users and their data without DB
users = {}


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
    # If user used the bot at the first time and this user not in 'users' dictionary '
    # 'users - we will add him to this dict
    if message.from_user.id not in users:
        users[message.from_user.id] = {
            'in_game': False,
            'secret_number': None,
            'attempts': None,
            'total_games': 0,
            'wins': 0
        }


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
@dp.message(Command(commands='stat'))
async def process_start_command(message: Message):
    await message.answer(
        f"Total played games: {users[message.from_user.id]['total_games']}\n"
        f"Won games: {users[message.from_user.id]['wins']}"
    )


# This handler will trigger on command "/cancel"
@dp.message(Command(commands='cancel'))
async def process_cancel_command(message: Message):
    if users[message.from_user.id]['in_game']:
        users[message.from_user.id]['in_game'] = False
        await message.answer(
            "You're leave the game. If you want to play "
            "again - text me about it"
        )
    else:
        await message.answer(
            "We're not playing at this time. "
            "Let's start?"
        )


# This handler will trigger when user is agreed to play
@dp.message(F.text.lower().in_(['yes', 'ye', 'lets play', 'play',
                                'game', 'want to play']))
async def process_positive_answer(message: Message):
    if not users[message.from_user.id]['in_game']:
        users[message.from_user.id]['in_game'] = True
        users[message.from_user.id]['secret_number'] = get_random_number()
        users[message.from_user.id]['attempts'] = ATTEMPTS
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
@dp.message(F.text.lower().in_(['no', 'not', 'nope', "don't want"]))
async def process_negative_answer(message: Message):
    if not users[message.from_user.id]['in_game']:
        await message.answer(
            "It's a pity :(\n\nIf you want to play, just "
            "write about it"
        )
    else:
        await message.answer(
            "We're playing with you now. Please, "
            "send numbers from 1 to 100"
        )


# This handler will trigger on messages with number from 1 to 100 that user will send
@dp.message(lambda x: x.text and x.text.isdigit() and 1 <= int(x.text) <= 100)
async def process_numbers_answer(message: Message):
    print(users)
    if users[message.from_user.id]['in_game']:
        if int(message.text) == users[message.from_user.id]['secret_number']:
            users[message.from_user.id]['in_game'] = False
            users[message.from_user.id]['total_games'] += 1
            users[message.from_user.id]['wins'] += 1
            await message.answer(
                "Yay!!! You're right!\n\n"
                "Let's play again?"
            )
        elif int(message.text) > users[message.from_user.id]['secret_number']:
            users[message.from_user.id]['attempts'] -= 1
            await message.answer('My number is lower')
        elif int(message.text) < users[message.from_user.id]['secret_number']:
            users[message.from_user.id]['attempts'] -= 1
            await message.answer('My number is bigger')

        if users[message.from_user.id]['attempts'] == 0:
            users[message.from_user.id]['in_game'] = False
            users[message.from_user.id]['total_games'] += 1
            await message.answer(
                f"Unfortunately, you have no more "
                f"attempts. You lost :(\n\nMy number "
                f"was {users[message.from_user.id]['secret_number']}\n\nLet's "
                f'play again?'
            )
    else:
        await message.answer("We're not playing yet. Want to play?")


# This handler will trigger by other messages
@dp.message()
async def process_other_answers(message: Message):
    if users[message.from_user.id]['in_game']:
        await message.answer(
            "We're playing with you now. "
            "Please send numbers from 1 to 100"
        )
    else:
        await message.answer(
            "I'm a pretty limited bot, come on "
            "let's just play a game?"
        )


if __name__ == '__main__':
    dp.run_polling(bot)
