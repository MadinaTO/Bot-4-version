from aiogram import Bot, Dispatcher, types
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils import executor
from decouple import config
import logging

TOKEN = config('TOKEN')

bot = Bot(TOKEN)
dp = Dispatcher(bot=bot)


@dp.message_handler(commands=['start', 'help'])
async def start_handler(message: types.Message):
    await bot.send_message(chat_id=message.from_user.id, text=f"Hello {message.from_user.first_name}")
    await message.answer('Пока что все:)')
    # await message.reply('This is a reply method')


@dp.message_handler(commands=['quiz'])
async def quiz_1(message: types.Message):
    markup = InlineKeyboardMarkup()
    button_call_1 = InlineKeyboardButton('NEXT', callback_data='button_call_1')
    markup.add(button_call_1)

    question = 'Какой мем изображен на фото?'
    answers = [
        'Маленький Пепе',
        'Лягушонок Пепе',
        'Апу апустая',
        'Все ответы правильные'
    ]

    photo = open('media/img_1.png', 'rb')
    await bot.send_photo(message.from_user.id, photo=photo)

    await bot.send_poll(
        chat_id=message.from_user.id,
        question=question,
        options=answers,
        is_anonymous=False,
        type='quiz',
        correct_option_id=1,
        explanation='Все ответы правильные',
        open_period=20,
        reply_markup=markup
    )


@dp.callback_query_handler(text='button_call_1')
async def quiz_2(call: types.CallbackQuery):
    question = 'Где находится музей Лувр'
    answers = [
        'Рим',
        'Вена',
        'Париж',
        'Цюрих',
        'Барселона',
        'Амстердам'
    ]
    photo = open('media/ -11.jpg', 'rb')
    await bot.send_photo(call.from_user.id, photo=photo)

    await bot.send_poll(
        chat_id=call.from_user.id,
        question=question,
        options=answers,
        is_anonymous=False,
        type='quiz',
        correct_option_id=2,
        explanation='Париж',
        open_period=20
    )


@dp.message_handler()
async def echo(message: types.Message):
    await bot.send_message(message.from_user.id, message.text)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(dp, skip_updates=True)

