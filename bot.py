from aiogram import Bot, types, Dispatcher
import asyncio
from config import token
from aiogram.filters import Command


HELP_COMMAND = """ 
/help - список команд
/start - начало работы с ботом
/click - СЕКРЕТНАЯ ИНФОРМАЦИЯ!!!
/picture = СЕКРЕТНАЯ КАРТИНКА!!!
"""

bot = Bot(token)
dp = Dispatcher()


@dp.message(Command("help"))
async def help_command(message: types.Message):
    await message.reply(text=HELP_COMMAND)

@dp.message(Command('start'))
async def help_command(message: types.Message):
    await message.answer(text="hello artem novakovski")
    await message.delete()
    
@dp.message(Command('click'))
async def help_command(message: types.Message):
    await message.answer (text=
"""
28.09.2025, 08:21:13
ip
37.30.36.92
browser
Chrome 140
platform
Android 15
isp
T-Mobile Poland
useragent
Mozilla/5.0 (Linux; Android 15; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.7339.155 Mobile Safari/537.36
country
Польша
city
Kobylnica
state
Greater Poland
referer
HTTP-Referer пуст
bot
Нет
latitude
52.44600000000000000
longitude
17.07640000000000000
accuracy
ip
accuracy-radius
IP
""")

@dp.message(Command('picture'))
async def send_picture(message: types.Message):
      await message.answer_photo(
        photo="https://i.ytimg.com/vi/oMxOuGU72vM/hq720.jpg?sqp=-oaymwEhCK4FEIIDSFryq4qpAxMIARUAAAAAGAElAADIQj0AgKJD&rs=AOn4CLCvMWqVVnS0VRYfJ0ce59_Vbkr7-w")

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
