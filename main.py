import logging

from aiogram import Bot, Dispatcher, executor, types

from DB import DB
from config import TOKEN
import keyboards as kb
from html_course import set_html_bot
from js_course import set_js_bot
from python_course import set_python_bot

bot = Bot(token=TOKEN, parse_mode="HTML")
dp = Dispatcher(bot)

db = DB('DB.db')
logging.basicConfig(level=logging.INFO)


@dp.message_handler(commands=['subscribe'])
async def subscribe(message: types.Message):
    if not db.subscriber_exist(message.chat.id):
        db.add_subscriber(message.chat.id)
    else:
        db.update_subscription(message.chat.id, True)

    await message.answer(
        "Вы успешно подписались на рассылку!")


@dp.message_handler(commands=['unsubscribe'])
async def unsubscribe(message: types.Message):
    if not db.subscriber_exist(message.chat.id):
        db.add_subscriber(message.chat.id, False)
        await message.answer("Вы итак не подписаны.")
    else:
        db.update_subscription(message.chat.id, False)
        await message.answer("Вы успешно отписаны от рассылки.")


@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.reply(text=f'Для запуска бота или возврата в начало введите: /start\nВыберите раздел:',
                        reply=False,
                        reply_markup=kb.init_keyboard())


if __name__ == '__main__':
    set_js_bot(dp)
    set_html_bot(dp)
    set_python_bot(dp)
    executor.start_polling(dp, skip_updates=True)
