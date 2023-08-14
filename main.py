from aiogram.utils import executor
import logging
from config import bot, dispatcher, COINGECKO_API_URL
import requests
from aiogram import types


@dispatcher.message_handler(commands=['start'])
async def start(message: types.Message):
    await message.reply(
        "Привет! Я бот для отслеживания цены Litecoin. Используйте команду "
        "/price, чтобы получить текущую цену Litecoin, или отправьте мне количество Litecoin для конвертации в USD.")


@dispatcher.message_handler(commands=['price'])
async def get_litecoin_price(message: types.Message):
    response = requests.get(COINGECKO_API_URL)
    if response.status_code == 200:
        data = response.json()
        litecoin_price = data.get('litecoin', {}).get('usd', 'N/A')
        await message.reply(f"Текущая цена Litecoin.: ${litecoin_price}")
    else:
        await message.reply("Не удалось получить цену Litecoin. Пожалуйста, попробуйте позже.")


@dispatcher.message_handler()
async def convert_to_usd(message: types.Message):
    try:
        litecoin_amount = float(message.text)
        response = requests.get(COINGECKO_API_URL)
        if response.status_code == 200:
            data = response.json()
            litecoin_price = data.get('litecoin', {}).get('usd', 'N/A')
            usd_value = int(litecoin_amount * litecoin_price * 454) + 600
            await message.reply(f"{usd_value:,}")
        else:
            await message.reply("Не удалось получить цену Litecoin. Пожалуйста, попробуйте снова позже.")
    except ValueError:
        await message.reply("Неверный ввод. Пожалуйста, введите правильное количество Litecoin.")


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(dispatcher, skip_updates=True)
