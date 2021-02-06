from telegram import Update
from telegram import KeyboardButton
from telegram import ReplyKeyboardMarkup
from telegram import ReplyKeyboardRemove
from telegram.ext import Updater
from telegram.ext import CallbackContext
from telegram.ext import Filters
from telegram.ext import MessageHandler
from telegram.ext import CommandHandler

from config import TOKEN

button_HTML = 'HTML, CSS'
button_HTML_lesson = 'Список уроков\n по HTML5, CSS3'
button_HTML_docs = 'Общая документация\n по HTML5, CSS3'
button_HTML_links = 'Полезные ссылки\n по HTML5, CSS3'
button_JS = 'JavaScript'
button_JS_lesson = 'Список уроков\n по JS'
button_JS_docs = 'Общая документация\n по JS'
button_JS_links = 'Полезные ссылки\n по JS'
button_Python = 'Python'
button_Python_lesson = 'Список уроков\n по Python'
button_Python_docs = 'Общая документация\n по Python'
button_Python_links = 'Полезные ссылки\n по Python'



def log_error(f):
    def inner(*args, **kwargs):
        try:
            return f(*args, **kwargs)
        except Exception as e:
            print(f'ERROR: {e}')
            raise e

    return inner


def button_HTML_handler(update: Update, context: CallbackContext):
    update.message.reply_text(
        text='Справочник по разделу HTML5, CSS3',
        reply_markup=ReplyKeyboardMarkup(
            keyboard=[
                [
                    KeyboardButton(text=button_HTML_lesson),
                    KeyboardButton(text=button_HTML_docs),
                    KeyboardButton(text=button_HTML_links),
                ],
            ],
            resize_keyboard=True,
        )
    )


def button_JS_handler(update: Update, context: CallbackContext):
    update.message.reply_text(
        text='Справочник по разделу JavaScript',
        reply_markup=ReplyKeyboardMarkup(
            keyboard=[
                [
                    KeyboardButton(text=button_JS_lesson),
                    KeyboardButton(text=button_JS_docs),
                    KeyboardButton(text=button_JS_links),
                ],
            ],
            resize_keyboard=True,
        )
    )


def button_Python_handler(update: Update, context: CallbackContext):
    update.message.reply_text(
        text='Справочник по разделу Python',
        reply_markup=ReplyKeyboardMarkup(
            keyboard=[
                [
                    KeyboardButton(text=button_Python_lesson),
                    KeyboardButton(text=button_Python_docs),
                    KeyboardButton(text=button_Python_links),
                ],
            ],
            resize_keyboard=True,
        )
    )


def do_start(update: Update, context: CallbackContext):
    reply_markup = ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(text=button_HTML),
                KeyboardButton(text=button_JS),
                KeyboardButton(text=button_Python),
            ],
        ],
        resize_keyboard=True,
    )

    update.message.reply_text(
        text=f'Для запуска бота или возврата в начало введите: /start\nВыберите раздел:',
        reply_markup=reply_markup,
    )


@log_error
def message_handler(update: Update, context: CallbackContext):
    text = update.message.text
    if text == button_HTML:
        return button_HTML_handler(update=update, context=context)
    if text == button_JS:
        return button_JS_handler(update=update, context=context)
    if text == button_Python:
        return button_Python_handler(update=update, context=context)


def main():
    updater = Updater(
        token=TOKEN,
        use_context=True,
    )
    start_handler = CommandHandler("start", do_start)
    updater.dispatcher.add_handler(start_handler)
    updater.dispatcher.add_handler(MessageHandler(filters=Filters.text,
                                                  callback=message_handler))
    print(updater.bot.get_me())
    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
