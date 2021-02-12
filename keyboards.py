from aiogram import types


def init_keyboard():
    buttons = [
        types.InlineKeyboardButton(text="HTML, CSS", callback_data='html'),
        types.InlineKeyboardButton(text="JavaScript", callback_data='js'),
        types.InlineKeyboardButton(text="Python", callback_data='python'),
    ]
    keyboard = types.InlineKeyboardMarkup(row_width=3)
    keyboard.add(*buttons)
    return keyboard


def html_keyboard():
    buttons = [
        types.InlineKeyboardButton(text="Список видео по HTML, CSS", callback_data='html_video'),
        types.InlineKeyboardButton(text="Общая документация по HTML, CSS", callback_data='html_docs'),
        types.InlineKeyboardButton(text="Полезные ссылки по HTML, CSS", callback_data='html_link'),
    ]
    keyboard = types.InlineKeyboardMarkup(row_width=1)
    keyboard.add(*buttons)
    return keyboard


def js_keyboard():
    buttons = [
        types.InlineKeyboardButton(text="Список видео по JavaScript", callback_data='js_video'),
        types.InlineKeyboardButton(text="Общая документация по JavaScript", callback_data='js_docs'),
        types.InlineKeyboardButton(text="Полезные ссылки по JavaScript", callback_data='js_link'),
    ]
    keyboard = types.InlineKeyboardMarkup(row_width=1)
    keyboard.add(*buttons)
    return keyboard


def python_keyboard():
    buttons = [
        types.InlineKeyboardButton(text="Список видео по Python", callback_data='python_video'),
        types.InlineKeyboardButton(text="Общая документация по Python", callback_data='python_docs'),
        types.InlineKeyboardButton(text="Полезные ссылки по Python", callback_data='python_link'),
    ]
    keyboard = types.InlineKeyboardMarkup(row_width=1)
    keyboard.add(*buttons)
    return keyboard
