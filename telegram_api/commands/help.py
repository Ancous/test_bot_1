from telebot.types import ReplyKeyboardRemove

from telegram_api.activate_bot.activate import bot


COMMANDS = """
КОМАНДЫ
<b>start</b> - начало подбора арендного жилья
<b>help</b> - описание команд бота
"""


@bot.message_handler(commands=["help"])
def my_help(message):
    bot.send_message(
        chat_id=message.chat.id,
        parse_mode="HTML",
        text=COMMANDS,
        reply_markup=ReplyKeyboardRemove()
    )
