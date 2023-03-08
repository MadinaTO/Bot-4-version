from aiogram import types, Dispatcher
from config import bot


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


def register_handlers_callback(dp: Dispatcher):
    dp.register_callback_query_handler(quiz_2, text='button_call_1')
