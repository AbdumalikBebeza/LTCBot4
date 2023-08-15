from aiogram import Bot, Dispatcher


ADMINS = [908379438, 5517017632]
COINGECKO_API_URL = 'https://api.coingecko.com/api/v3/simple/price?ids=litecoin&vs_currencies=usd'
TOKEN = "6601435375:AAGTCWP_1tD0zm3lP1A2qLGkeVw2YU-R908"
bot = Bot(token=TOKEN)
dispatcher = Dispatcher(bot=bot)
