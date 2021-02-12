from datetime import datetime
from DB import DB
from aiogram import types
import keyboards as kb
from storage import TextBase


def create_log_date(call, section):
    user_id = int(call.message.chat.id)
    user_name = str(call.message.chat.first_name) + ' ' + str(call.message.chat.last_name)
    date = datetime.now()
    section = section
    return user_id, user_name, date, section


def set_python_bot(dp):
    db = DB('DB.db')

    @dp.callback_query_handler(text="python")
    async def get_text_messages(call: types.CallbackQuery):
        await call.message.reply(text=f'Для запуска бота или возврата в начало введите: /start\nВыберите раздел:',
                                 reply=False,
                                 reply_markup=kb.python_keyboard())

    @dp.callback_query_handler(text="python_video")
    async def get_text_messages(call: types.CallbackQuery):
        set_log_arg = create_log_date(call, "python_video")
        db.save_log(*set_log_arg)
        await call.message.reply(reply=False, text=TextBase.Python_video)

    @dp.callback_query_handler(text="python_docs")
    async def get_text_messages(call: types.CallbackQuery):
        set_log_arg = create_log_date(call, "python_docs")
        db.save_log(*set_log_arg)
        await call.message.reply(reply=False, text=TextBase.Python_docs)

    @dp.callback_query_handler(text="python_link")
    async def get_text_messages(call: types.CallbackQuery):
        set_log_arg = create_log_date(call, "python_link")
        db.save_log(*set_log_arg)
        await call.message.reply(reply=False, text=TextBase.Python_links)
