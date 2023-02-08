import re

import django
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
django.setup()
from asgiref.sync import sync_to_async
from Customer.models import User, TelegramChat


bot = Bot(token="5627000647:AAEP93ZnHzH_xAG8nYQW-q0yTSZyw4HhO3Y")
dp = Dispatcher(bot)


@sync_to_async
def get_users(msg):
    return list(
        User.objects.filter(email=msg.text)
    )


@sync_to_async
def create_telegram_chat(chat_id, list_users):
    return TelegramChat.objects.create(chat_id=chat_id, user=list_users)


@sync_to_async
def delete_telegram_chat(chat_id):
    chat = TelegramChat.objects.get(chat_id=chat_id.from_user.id)
    chat.delete()


@dp.message_handler(commands=['start'])
async def process_start_command(msg):
    await bot.send_message(msg.from_user.id, "Hello, \ngive the email address for Library.com")


@dp.message_handler(regexp=re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+'))
async def login(msg: types.Message):
    results = await get_users(msg)
    if results:
        await bot.send_message(
            msg.from_user.id,
            "Thank you for registering, you will receive information about your loans at Library.com"
        )
        await create_telegram_chat(msg.from_user.id, results[0])
    else:
        await bot.send_message(msg.from_user.id, "Sorry, you are not registered with Library.com")


@dp.message_handler(commands=['logout'])
async def logout_command(message: types.Message):
    try:
        await delete_telegram_chat(message)
        await bot.send_message(message.from_user.id, "logged out")
    except Exception as e:
        print(e)
        await bot.send_message(message.from_user.id, "not login yet")


if __name__ == '__main__':
    executor.start_polling(dp)

