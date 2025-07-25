from aiogram import Bot, Dispatcher, types
from aiogram.types import WebAppInfo
from aiogram.filters import Command
import asyncio
import config

bot = Bot(token=config.BOT_TOKEN)
dp = Dispatcher()

@dp.message(Command('start'))
async def start(message: types.Message):
    markup = types.ReplyKeyboardMarkup(
        keyboard=[
            [types.KeyboardButton(
                text="🔗 Connect Tonkeeper",
                web_app=WebAppInfo(url="https://your-vercel-app.vercel.app/")
            )]
        ],
        resize_keyboard=True
    )
    await message.answer(
        "Нажмите кнопку для подключения Tonkeeper:",
        reply_markup=markup
    )

@dp.message(lambda message: message.web_app_data is not None)
async def handle_web_app_data(message: types.Message):
    wallet_address = message.web_app_data.data
    await message.answer(
        f"✅ Кошелёк успешно подключен!\n"
        f"Адрес: `{wallet_address}`",
        parse_mode="Markdown"
    )
    # Здесь можно добавить логику работы с кошельком

async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())