from telegram_api.activate_bot.activate import bot
from telegram_api.keyboard.key_board import my_keyboard_max
from telegram_api.commands.help import COMMANDS


BUTTON_MAX = """
КНОПКИ
<b>1 000 000 рублей</b> - посмотреть подробнее жильё за 1 000 0000 рублей
<b>500 000 рублей</b> - посмотреть подробнее жильё за 500 0000 рублей
<b>Назад в главное меню</b> - вернуться в главное меню
"""


@bot.message_handler(func=lambda message: message.text == "максимальная цена")
def my_maximum(message):
    bot.send_message(
        chat_id=message.chat.id,
        parse_mode="HTML",
        text=f"{COMMANDS}{BUTTON_MAX}\nДорого",
        reply_markup=my_keyboard_max()
    )
