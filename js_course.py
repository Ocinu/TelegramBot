from datetime import datetime
from aiogram import types
import keyboards as kb
from DB import DB
from storage import TextBase


def create_log_date(call, section):
    user_id = int(call.message.chat.id)
    user_name = str(call.message.chat.first_name) + ' ' + str(call.message.chat.last_name)
    date = datetime.now()
    section = section
    return user_id, user_name, date, section


def set_js_bot(dp):
    db = DB('DB.db')

    @dp.callback_query_handler(text="js")
    async def get_text_messages(call: types.CallbackQuery):
        await call.message.reply(text=f'Для запуска бота или возврата в начало введите: /start\nВыберите раздел:',
                                 reply=False,
                                 reply_markup=kb.js_keyboard())

    @dp.callback_query_handler(text="js_video")
    async def get_text_messages(call: types.CallbackQuery):
        set_log_arg = create_log_date(call, "js_video")
        db.save_log(*set_log_arg)
        await call.message.reply(reply=False, text=TextBase.JS_video)

    @dp.callback_query_handler(text="js_docs")
    async def get_text_messages(call: types.CallbackQuery):
        set_log_arg = create_log_date(call, "js_docs")
        db.save_log(*set_log_arg)
        await call.message.reply(reply=False, text=TextBase.JS_docs)

    @dp.callback_query_handler(text="js_link")
    async def get_text_messages(call: types.CallbackQuery):
        set_log_arg = create_log_date(call, "js_link")
        db.save_log(*set_log_arg)
        await call.message.reply(reply=False, text=TextBase.JS_links)
