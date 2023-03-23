from telegram_api.activate_bot.activate import bot
from telegram_api.keyboard.key_board import my_keyboard_start
from telegram_api.commands.help import COMMANDS


BUTTON_START = """
КНОПКИ
<b>минимальная цена</b> - поиск стоимости самой низкой арены
<b>максимальная цена</b> - поиск стоимости самой высокой арены
<b>диапазон значений</b> - можно выбрать диапазон значений поиска по цене, расстоянию, сроку аренды
<b>история поиска</b> - история последних пяти запросов
"""


@bot.message_handler(commands=["start"])
@bot.message_handler(func=lambda message: message.text == "Назад в главное меню")
def my_start(message):
    bot.send_message(
        chat_id=message.chat.id,
        parse_mode="HTML",
        text=f"{COMMANDS}{BUTTON_START}\nПривет {message.from_user.first_name}\nВыберите категорию фильтрации",
        reply_markup=my_keyboard_start()
    )
