from aiogram import Bot, Dispatcher, types
from aiogram.types import WebAppInfo
from aiogram.filters import Command

bot = Bot(token="7226272471:AAH3dbbAQEXUiG5iqotyB3SXKuIjmBbl8JM")
dp = Dispatcher()

@dp.message(Command('start'))
async def start(message: types.Message):
    markup = types.ReplyKeyboardMarkup(
        keyboard=[
            [types.KeyboardButton(
                text="🔗 Connect Tonkeeper",
                web_app=WebAppInfo(url="https://tonkeeper-bot.vercel.app/")
            )]
        ],
        resize_keyboard=True
    )
    await message.answer(
        "Нажмите кнопку для авторизации:",
        reply_markup=markup
    )

@dp.message(lambda message: message.web_app_data is not None)
async def handle_web_app_data(message: types.Message):
    print(message)
    wallet_address = message.web_app_data.data
    await message.answer(f"✅ Кошелёк подключён: `{wallet_address}`", parse_mode="Markdown")

async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    import asyncio
    asyncio.run(main())