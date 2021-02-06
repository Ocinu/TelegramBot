from telegram import Update
from telegram import KeyboardButton
from telegram import ReplyKeyboardMarkup
from telegram import ReplyKeyboardRemove
from telegram.ext import Updater
from telegram.ext import CallbackContext
from telegram.ext import Filters
from telegram.ext import MessageHandler
from telegram.ext import CommandHandler
from data import TextBase
from config import TOKEN

textInsert = TextBase

button_HTML = 'HTML, CSS'
button_HTML_video = 'Список видео\n по HTML5, CSS3'
button_HTML_docs = 'Общая документация\n по HTML5, CSS3'
button_HTML_links = 'Полезные ссылки\n по HTML5, CSS3'
button_JS = 'JavaScript'
button_JS_video = 'Список видео\n по JS'
button_JS_docs = 'Общая документация\n по JS'
button_JS_links = 'Полезные ссылки\n по JS'
button_Python = 'Python'
button_Python_video = 'Список видео\n по Python'
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
                    KeyboardButton(text=button_HTML_video),
                    KeyboardButton(text=button_HTML_docs),
                    KeyboardButton(text=button_HTML_links),
                ],
            ],
            resize_keyboard=True,
        )
    )


def button_html_video(update: Update, context: CallbackContext, ):
    update.message.reply_text(
        text=textInsert.HTML_video,
        reply_markup=ReplyKeyboardRemove(),
    )


def button_html_docs(update: Update, context: CallbackContext, ):
    update.message.reply_text(
        text=textInsert.HTML_docs,
        reply_markup=ReplyKeyboardRemove(),
    )


def button_html_links(update: Update, context: CallbackContext, ):
    update.message.reply_text(
        text=textInsert.HTML_links,
        reply_markup=ReplyKeyboardRemove(),
    )


def button_JS_handler(update: Update, context: CallbackContext):
    update.message.reply_text(
        text='Справочник по разделу JavaScript',
        reply_markup=ReplyKeyboardMarkup(
            keyboard=[
                [
                    KeyboardButton(text=button_JS_video),
                    KeyboardButton(text=button_JS_docs),
                    KeyboardButton(text=button_JS_links),
                ],
            ],
            resize_keyboard=True,
        )
    )


def button_js_video(update: Update, context: CallbackContext, ):
    update.message.reply_text(
        text=textInsert.JS_video,
        reply_markup=ReplyKeyboardRemove(),
    )


def button_js_docs(update: Update, context: CallbackContext, ):
    update.message.reply_text(
        text=textInsert.JS_docs,
        reply_markup=ReplyKeyboardRemove(),
    )


def button_js_links(update: Update, context: CallbackContext, ):
    update.message.reply_text(
        text=textInsert.JS_links,
        reply_markup=ReplyKeyboardRemove(),
    )


def button_python_video(update: Update, context: CallbackContext, ):
    update.message.reply_text(
        text=textInsert.Python_video,
        reply_markup=ReplyKeyboardRemove(),
    )


def button_python_docs(update: Update, context: CallbackContext, ):
    update.message.reply_text(
        text=textInsert.Python_docs,
        reply_markup=ReplyKeyboardRemove(),
    )


def button_python_links(update: Update, context: CallbackContext, ):
    update.message.reply_text(
        text=textInsert.Python_links,
        reply_markup=ReplyKeyboardRemove(),
    )


def button_Python_handler(update: Update, context: CallbackContext):
    update.message.reply_text(
        text='Справочник по разделу Python',
        reply_markup=ReplyKeyboardMarkup(
            keyboard=[
                [
                    KeyboardButton(text=button_Python_video),
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
    if text == button_HTML_video:
        return button_html_video(update=update, context=context)
    if text == button_HTML_docs:
        return button_html_docs(update=update, context=context)
    if text == button_HTML_links:
        return button_html_links(update=update, context=context)
    if text == button_JS_video:
        return button_js_video(update=update, context=context)
    if text == button_JS_docs:
        return button_js_docs(update=update, context=context)
    if text == button_JS_links:
        return button_js_links(update=update, context=context)
    if text == button_Python_video:
        return button_python_video(update=update, context=context)
    if text == button_Python_docs:
        return button_python_docs(update=update, context=context)
    if text == button_Python_links:
        return button_python_links(update=update, context=context)


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
