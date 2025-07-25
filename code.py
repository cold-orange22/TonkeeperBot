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
                text="Отправить сообщение",
                web_app=WebAppInfo(url="https://tonkeeper-bot.vercel.app/")
            )]
        ],
        resize_keyboard=True
    )
    await message.answer(
        "Нажмите кнопку ниже, чтобы отправить сообщение:",
        reply_markup=markup
    )

@dp.message(lambda message: message.web_app_data is not None)
async def handle_web_app_data(message: types.Message):
    web_app_data = message.web_app_data.data
    print(web_app_data)
    await message.answer(
        f"✅ Получено сообщение из WebApp:\n"
        f"`{web_app_data}`",
        parse_mode="Markdown"
    )

async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())