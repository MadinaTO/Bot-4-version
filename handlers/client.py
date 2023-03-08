from aiogram import types, Dispatcher
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from config import bot
from keybords.client_kb import start_markup


async def start_handler(message: types.Message):
    await bot.delete_message(message.from_user.id, message.message_id)
    await bot.send_message(chat_id=message.from_user.id, text=f"Hello {message.from_user.first_name}",
                           reply_markup=start_markup)
    # await message.answer('Пока что все:)')
    # await message.reply('This is a reply method')


async def info_handler(message: types.Message):
    await message.answer('Its your problems!')


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
        correct_option_id=3,
        explanation='Все ответы правильные',
        open_period=20,
        reply_markup=markup
    )


def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(start_handler, commands=['start'])
    dp.register_message_handler(quiz_1, commands=['quiz'])
    dp.register_message_handler(info_handler, commands=['info'])
