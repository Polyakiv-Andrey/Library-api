from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
import django
from asgiref.sync import sync_to_async

django.setup()

from Customer.models import User

bot = Bot(token="5627000647:AAEP93ZnHzH_xAG8nYQW-q0yTSZyw4HhO3Y")
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    await message.reply("Hello, \ngive the email address for Library.com")


@sync_to_async
def get_users(msg):
    return list(
        User.objects.filter(email=msg.text)
    )


@dp.message_handler()
async def echo_message(msg: types.Message):
    results = await get_users(msg)
    if results:
        await bot.send_message(msg.from_user.id, "Cпасибо за регистрацию, вы будете получать информацию о ваших займах в Library.com ")
    else:
        await bot.send_message(msg.from_user.id, "Sorry, you are not registered with Library.com")


@dp.message_handler(commands=['logout'])
async def process_end_command(message: types.Message):
    await message.reply("Hello, \ngive the email address for Library.com")

if __name__ == '__main__':
    executor.start_polling(dp)