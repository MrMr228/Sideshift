from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

bot = Bot(token="BOT_TOKEN")
dp = Dispatcher()

# Кнопки
buy_btn = InlineKeyboardButton(text="🛒 Купить", callback_data="buy")
details_btn = InlineKeyboardButton(text="🔍 Подробнее", url="https://t.me/sideshiftstore")

@dp.message(Command("start"))
async def start(message: types.Message):
    kb = InlineKeyboardMarkup(inline_keyboard=[[buy_btn, details_btn]])
    await message.answer(
        "🖤 Добро пожаловать в SIDESHIFT STORE!",
        reply_markup=kb
    )

if __name__ == "__main__":
    dp.run_polling(bot)