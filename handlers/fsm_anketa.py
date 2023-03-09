from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.filters.state import State, StatesGroup
from keybords import client_kb


class FSMAdmin(StatesGroup):
    name = State()
    age = State()
    gender = State()
    region = State()


async def fsm_start(message: types.Message):
    if message.chat.type == 'private':
        await FSMAdmin.name.set()
        await message.answer('Name?', reply_markup=client_kb.cancel_markup)
    else:
        await message.answer('Talk face to face')


async def load_name(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['id'] = message.from_user.id
        data['username'] = message.from_user.username
        data['name'] = message.text
        print(data)
    await FSMAdmin.next()
    await message.answer('Age?')


async def load_age(message: types.Message, state: FSMContext):
    if not message.text.isdigit():
        await message.answer("Only numbers!")
    elif not 17 < int(message.text) < 100:
        await message.answer("Access is restricted!")
    else:
        async with state.proxy() as data:
            data['age'] = message.text
        await FSMAdmin.next()
        await message.answer("Gender?",
                             reply_markup=client_kb.gender_markup)


async def load_gender(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['gender'] = message.text
    await FSMAdmin.next()
    await message.answer("Where are u from?", reply_markup=client_kb.cancel_markup)


async def load_region(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['region'] = message.text


def register_handlers_anketa(dp: Dispatcher):
    dp.register_message_handler(fsm_start, commands=['reg'])
    dp.register_message_handler(load_name, state=FSMAdmin.name)
    dp.register_message_handler(load_age, state=FSMAdmin.age)
    dp.register_message_handler(load_gender, state=FSMAdmin.gender)
    dp.register_message_handler(load_region, state=FSMAdmin.region)


