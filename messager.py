import os

import requests

from Customer.models import TelegramChat, User


def get_chat_user_id(user: User) -> int:
    get_model_telegram_chat = TelegramChat.objects.get(user=user)
    chat_id = get_model_telegram_chat.chat_id
    return chat_id


def send_to_telegram(message, user: User):

    api_token = os.environ.get("TELEGRAM_TOKEN")
    chat_id = get_chat_user_id(user)
    api_url = f'https://api.telegram.org/bot{api_token}/sendMessage'

    try:
        response = requests.post(
            api_url,
            json={'chat_id': chat_id, 'text': message}
        )
        print(response.text)
    except Exception as e:
        print(e)
