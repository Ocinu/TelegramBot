from aiogram import types
import keyboards as kb
from DB import DB
from storage import TextBase
from datetime import datetime


def create_log_date(call, section):
    user_id = int(call.message.chat.id)
    user_name = str(call.message.chat.first_name) + ' ' + str(call.message.chat.last_name)
    date = datetime.now()
    section = section
    return user_id, user_name, date, section


def set_html_bot(dp):
    db = DB('DB.db')

    @dp.callback_query_handler(text="html")
    async def get_text_messages(call: types.CallbackQuery):
        await call.message.reply(text=f'Для запуска бота или возврата в начало введите: /start\nВыберите раздел:',
                                 reply=False,
                                 reply_markup=kb.html_keyboard())

    @dp.callback_query_handler(text="html_video")
    async def get_text_messages(call: types.CallbackQuery):
        set_log_arg = create_log_date(call, "html_video")
        db.save_log(*set_log_arg)
        await call.message.reply(reply=False, text=TextBase.HTML_video)

    @dp.callback_query_handler(text="html_docs")
    async def get_text_messages(call: types.CallbackQuery):
        set_log_arg = create_log_date(call, "html_docs")
        db.save_log(*set_log_arg)
        await call.message.reply(reply=False, text=TextBase.HTML_docs)

    @dp.callback_query_handler(text="html_link")
    async def get_text_messages(call: types.CallbackQuery):
        set_log_arg = create_log_date(call, "html_docs")
        db.save_log(*set_log_arg)
        await call.message.reply(reply=False, text=TextBase.HTML_links)
