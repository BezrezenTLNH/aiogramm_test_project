import os

from aiogram import Bot, Dispatcher, F
from aiogram.filters import BaseFilter
from aiogram.types import Message
from aiogram.types import PhotoSize
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv('TG_TOKEN')

# Create a bot and dispatcher objects
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()


# def custom_filter(some_list):
#     return sum([x for x in some_list if isinstance(x, int) and x % 7 == 0]) <= 83

# anonymous_filter = lambda s: s.lower().count('я') >= 23

# @dp.message(lambda msg: msg.text == '/start')
# async def process_start_command(message: Message):
#     await message.answer(text='Это команда /start')
#
#
# if __name__ == '__main__':
#     dp.run_polling(bot)
#
# admin_ids: list[int] = [111111111]
#
#
# class IsAdmin(BaseFilter):
#     def __init__(self, admin_ids: list[int]) -> None:
#         self.admin_ids = admin_ids
#
#     async def __call__(self, message: Message) -> bool:
#         return message.from_user.id in self.admin_ids
#
#
# # This handler will trigger if he will catch update from admin
# @dp.message(IsAdmin(admin_ids))
# async def answer_if_admins_update(message: Message):
#     await message.answer(text="You're admin")
#
#
# # This handler will trigger if he will catch update not from admin
# @dp.message()
# async def answer_if_not_admins_update(message: Message):
#     await message.answer(text="You're not admin")


# This handler will check negative numbers in user's messages and make a list from them


# This handler will trigger if the user's message
# starts with the phrase "find the numbers" and has numbers in it

class NumbersInMessage(BaseFilter):
    async def __call__(self, message: Message) -> bool | dict[str, list[int]]:
        numbers = []
        for word in message.text.split():
            normalized_word = word.replace('.', '').replace(',', '').strip()
            if normalized_word.isdigit():
                numbers.append(int(normalized_word))
        if numbers:
            return {'numbers': numbers}
        return False

@dp.message(F.text.lower().startswith('find the numbers'), NumbersInMessage())
# In addition to the Message type object, we accept a list of numbers from the filter into the handler
async def process_if_numbers(message: Message, numbers: list[int]):
    await message.answer(
        text=f'Found it: {", ".join(str(num) for num in numbers)}')


# This handler will trigger if the user's message
# starts with the phrase "find the numbers", but there are no numbers in it
@dp.message(F.text.lower().startswith('find the numbers'))
async def process_if_not_numbers(message: Message):
    await message.answer(
        text="Not found:(")


@dp.message(F.photo[0].as_('photo_min'))
async def process_photo_send(message: Message, photo_min: PhotoSize):
    print(photo_min)


if __name__ == '__main__':
    dp.run_polling(bot)
