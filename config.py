from aiogram import Bot, Dispatcher


COINGECKO_API_URL = 'https://api.coingecko.com/api/v3/simple/price?ids=litecoin&vs_currencies=usd'
TOKEN = "6516271885:AAHvGtK4sNnhobiN67IdJnfh7ERDy1O77-U"
bot = Bot(token=TOKEN)
dispatcher = Dispatcher(bot=bot)
