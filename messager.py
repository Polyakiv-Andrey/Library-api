import os

import requests

from Customer.models import TelegramChat, User


def get_chat_user_id(user: User) -> int:
    get_model_telegram_chat = TelegramChat.objects.get(user=user)
    chat_id = get_model_telegram_chat.chat_id
    return chat_id


def send_to_telegram(message, user: User):

    apiToken = os.environ.get("TELEGRAM_TOKEN")
    chatID = get_chat_user_id(user)
    apiURL = f'https://api.telegram.org/bot{apiToken}/sendMessage'

    try:
        response = requests.post(apiURL, json={'chat_id': chatID, 'text': message})
        print(response.text)
    except Exception as e:
        print(e)
