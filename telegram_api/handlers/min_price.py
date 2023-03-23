from telegram_api.activate_bot.activate import bot
from telegram_api.keyboard.key_board import my_keyboard_min
from telegram_api.commands.help import COMMANDS


BUTTON_MIN = """
КНОПКИ
<b>20 000 рублей</b> - посмотреть подробнее жильё за 20 0000 рублей
<b>10 000 рублей</b> - посмотреть подробнее жильё за 10 0000 рублей
<b>Назад в главное меню</b> - вернуться в главное меню
"""


@bot.message_handler(func=lambda message: message.text == "минимальная цена")
def my_minimum(message):
    bot.send_message(
        chat_id=message.chat.id,
        parse_mode="HTML",
        text=f"{COMMANDS}{BUTTON_MIN}\nДёшево",
        reply_markup=my_keyboard_min()
    )
