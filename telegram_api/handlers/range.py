from telegram_api.activate_bot.activate import bot
from telegram_api.keyboard.key_board import my_keyboard_range
from telegram_api.commands.help import COMMANDS


BUTTON_RENGE = """
КНОПКИ
<b>диапазон цены</b> - выбрать диапазон поиска по цене
<b>диапазон удаленности</b> - выбрать диапазон поиска по удаленности
<b>диапазон срока аренды</b> - выбрать диапазон поиска по сроку аренды
<b>Назад в главное меню</b> - вернуться в главное меню
"""


@bot.message_handler(func=lambda message: message.text == "диапазон значений (цены, удаленности, срока аренды)")
def my_range(message):
    bot.send_message(
        chat_id=message.chat.id,
        parse_mode="HTML",
        text=f"{COMMANDS}{BUTTON_RENGE}\nДиапазон",
        reply_markup=my_keyboard_range()
    )
