import os
import time

import requests
from dotenv import load_dotenv

load_dotenv()

API_URL = 'https://api.telegram.org/bot'
API_dogS_URL = 'https://api.thedogapi.com/v1/images/search'
API_DOGS_URL = 'https://random.dog/woof.json'
BOT_TOKEN = os.getenv('TG_TOKEN')
ERROR_TEXT = 'Здесь должна была быть картинка с котиком :('

offset = -2
timeout = 100
updates: dict


def do_something() -> None:
    print('Был апдейт')


while True:
    start_time = time.time()
    updates = requests.get(f'{API_URL}{BOT_TOKEN}/getUpdates?offset={offset + 1}&timeout={timeout}').json()

    if updates['result']:
        for result in updates['result']:
            offset = result['update_id']
            do_something()

    end_time = time.time()
    print(f'Время между запросами к Telegram Bot API: {end_time - start_time}')
