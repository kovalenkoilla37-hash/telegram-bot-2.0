from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext
import asyncio

BOT_TOKEN = "8313231784:AAHjAafo4lU-M7gPrAdcEVfyY5GxeSncLeo"
GROUP_ID = -4849060567

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

class Form(StatesGroup):
    name = State()
    location = State()
    age = State()
    kd = State()
    source = State()
    communication = State()

@dp.message(Command("start"))
async def start(message: types.Message, state: FSMContext):
    await message.answer("Привет! Давай заполним заявку.\nКак тебя зовут?")
    await state.set_state(Form.name)

@dp.message(Form.name)
async def get_name(message: types.Message, state: FSMContext):
    await state.update_data(name=message.text)
    await message.answer("Откуда ты?")
    await state.set_state(Form.location)

@dp.message(Form.location)
async def get_location(message: types.Message, state: FSMContext):
    await state.update_data(location=message.text)
    await message.answer("Сколько тебе лет?")
    await state.set_state(Form.age)

@dp.message(Form.age)
async def get_age(message: types.Message, state: FSMContext):
    await state.update_data(age=message.text)
    await message.answer("Какой у тебя КД в игре?")
    await state.set_state(Form.kd)

@dp.message(Form.kd)
async def get_kd(message: types.Message, state: FSMContext):
    await state.update_data(kd=message.text)
    await message.answer("Откуда узнал о нас?")
    await state.set_state(Form.source)

@dp.message(Form.source)
async def get_source(message: types.Message, state: FSMContext):
    await state.update_data(source=message.text)
    await message.answer("На сколько ты общительный человек (1-10)?")
    await state.set_state(Form.communication)

@dp.message(Form.communication)
async def finish(message: types.Message, state: FSMContext):
    await state.update_data(communication=message.text)
    data = await state.get_data()
    text = (
        f"📋 *Новая заявка:*\n"
        f"👤 Имя: {data['name']}\n"
        f"🌍 Откуда: {data['location']}\n"
        f"🎂 Возраст: {data['age']}\n"
        f"🎯 КД: {data['kd']}\n"
        f"🗣️ Откуда узнал: {data['source']}\n"
        f"🤝 Общительность: {data['communication']}/10"
    )
    await bot.send_message(GROUP_ID, text, parse_mode="Markdown")
    await message.answer("✅ Спасибо! Твоя заявка отправлена.")
    await state.clear()

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
