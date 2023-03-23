from telegram_api.activate_bot.activate import bot
from telegram_api.commands.help import my_help
from telegram_api.handlers.start import my_start
from telegram_api.handlers.max_price import my_maximum
from telegram_api.handlers.min_price import my_minimum
from telegram_api.handlers.range import my_range


if __name__ in "__main__":
    bot.infinity_polling()
