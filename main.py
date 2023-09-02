from aiogram import types, Bot, Dispatcher, executor
from config import TOKEN
import time
# from parsing_data import data
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton
from test_code import fetch_random_quote

bot = Bot(TOKEN)
dp = Dispatcher(bot)

keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
btn1 = types.KeyboardButton(text='Получить цитату сейчас')
keyboard.add(btn1)
btn2 = types.KeyboardButton(text='Получать цитаты каждые 30 минут')
keyboard.add(btn2)


@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    await message.reply("Привет!\n Я бот Цитатник", reply_markup=keyboard)


@dp.message_handler(text='Получить цитату сейчас')
async def cmd_get_citata(message: types.Message):
    await message.answer(fetch_random_quote())

@dp.message_handler(text='Получать цитаты каждые 30 минут')
async def cmd_await30(message: types.Message):
    nowtime = countdown(5)
    await message.answer(nowtime)



def countdown(time_sec):
    while time_sec:
        mins, secs = divmod(time_sec, 60)
        time.sleep(1)
        time_sec -= 1

        if time_sec == 0:
            cmd_await30()

# countdown(4)


if __name__ == '__main__':
    executor.start_polling(dp)


















