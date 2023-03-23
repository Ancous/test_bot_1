from telebot.types import ReplyKeyboardMarkup, KeyboardButton


def my_keyboard_start():
    kb = ReplyKeyboardMarkup(resize_keyboard=True)
    button_1 = KeyboardButton(text="максимальная цена")
    button_2 = KeyboardButton(text="минимальная цена")
    button_3 = KeyboardButton(text="диапазон значений (цены, удаленности, срока аренды)")
    button_4 = KeyboardButton(text="история поиска")
    kb.add(button_1, button_2)
    kb.add(button_3)
    kb.add(button_4)
    return kb


def my_keyboard_max():
    kb = ReplyKeyboardMarkup(resize_keyboard=True)
    button_1 = KeyboardButton(text="1 000 000 рублей")
    button_2 = KeyboardButton(text="500 000 рублей")
    button_3 = KeyboardButton(text="Назад в главное меню")
    kb.add(button_1, button_2)
    kb.add(button_3)
    return kb


def my_keyboard_min():
    kb = ReplyKeyboardMarkup(resize_keyboard=True)
    button_1 = KeyboardButton(text="10 0000 рублей")
    button_2 = KeyboardButton(text="20 0000 рублей")
    button_3 = KeyboardButton(text="Назад в главное меню")
    kb.add(button_1, button_2)
    kb.add(button_3)
    return kb


def my_keyboard_range():
    kb = ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    button_1 = KeyboardButton(text="диапазон цены")
    button_2 = KeyboardButton(text="диапазон удаленности")
    button_3 = KeyboardButton(text="диапазон срока аренды")
    button_4 = KeyboardButton(text="Назад в главное меню")
    kb.add(button_1, button_2, button_3, button_4)
    return kb
