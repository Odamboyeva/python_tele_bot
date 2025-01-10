import asyncio
import logging
import sys
from aiogram import Bot, Dispatcher, F
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import Command
from aiogram.types import Message,CallbackQuery
from config import BOT_TOKEN as token
from botton import *
bot = Bot(token=token, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
dp = Dispatcher()

@dp.message(Command('start'))
async def StartCommand(message: Message):
    await message.answer_photo(photo="")

@dp.callback_query(F.data == 'Fronted')
async def StartCommand(message: Message):
   await message.answer(text="Fromnted darslari", reply_markup=html)


@dp.callback_query(F.data == 'HTML')
async def StartCommand(message: Message):
   await message.answer(text="Html darslari", reply_markup=Html)


@dp.callback_query(F.data == '1-dars')
async def StartCommand(message: Message):
   await message.answer_video(video='https://t.me/botvideo12/7', reply_markup=Html)

@dp.callback_query(F.data == '2-dars')
async def StartCommand(message: Message):
   await message.answer_video(video='https://t.me/botvideo12/8', reply_markup=Html)

@dp.callback_query(F.data == '3-dars')
async def StartCommand(message: Message):
   await message.answer_video(video='https://t.me/botvideo12/9', reply_markup=Html)


@dp.callback_query(F.data == '4-dars')
async def StartCommand(message: Message):
   await message.answer_video(video='https://t.me/botvideo12/10', reply_markup=Html)


@dp.callback_query(F.data == '5-dars')
async def StartCommand(message: Message):
   await message.answer_video(video='https://t.me/botvideo12/11', reply_markup=Html)


@dp.callback_query(F.data == '6-dars')
async def StartCommand(message: Message):
   await message.answer_video(video='https://t.me/botvideo12/12', reply_markup=Html)



@dp.callback_query(F.data == '7-dars')
async def StartCommand(message: Message):
   await message.answer_video(video='https://t.me/botvideo12/13', reply_markup=Html)


@dp.callback_query(F.data == '8-dars')
async def StartCommand(message: Message):
   await message.answer_video(video='https://t.me/botvideo12/14', reply_markup=Html)


@dp.callback_query(F.data == '9-dars')
async def StartCommand(message: Message):
   await message.answer_video(video='https://t.me/botvideo12/15', reply_markup=Html)



@dp.callback_query(F.data == '10-dars')
async def StartCommand(message: Message):
   await message.answer_video(video='https://t.me/botvideo12/16', reply_markup=Html)

#css
@dp.message(F.data == "1 -dars")
async def StartCommand(message: Message):
   await message.answer_video(video='https://t.me/botvideo12/17',reply_markup=csss)

@dp.message(F.data == "2 -dars")
async def StartCommand(message: Message):
   await message.answer_video(video='https://t.me/botvideo12/18',reply_markup=csss)


@dp.message(F.data == "3 -dars")
async def StartCommand(message: Message):
   await message.answer_video(video='https://t.me/botvideo12/19',reply_markup=csss)


@dp.message(F.data == "4 -dars")
async def StartCommand(message: Message):
   await message.answer_video(video='https://t.me/botvideo12/20',reply_markup=csss)


@dp.message(F.data == "5 -dars")
async def StartCommand(message: Message):
   await message.answer_video(video='https://t.me/botvideo12/21',reply_markup=csss)


@dp.message(F.data == "6 -dars")
async def StartCommand(message: Message):
   await message.answer_video(video='https://t.me/botvideo12/22',reply_markup=csss)


@dp.message(F.data == "7 -dars")
async def StartCommand(message: Message):
   await message.answer_video(video='https://t.me/botvideo12/23',reply_markup=csss)


@dp.message(F.data == "8 -dars")
async def StartCommand(message: Message):
   await message.answer_video(video='https://t.me/botvideo12/24',reply_markup=csss)


@dp.message(F.data == "9 -dars")
async def StartCommand(message: Message):
   await message.answer_video(video='https://t.me/botvideo12/25',reply_markup=csss)

@dp.message(F.data == "10 -dars")
async def StartCommand(message: Message):
   await message.answer_video(video='https://t.me/botvideo12/26',reply_markup=csss)


@dp.message(F.data == "Bakent")
async def StartCommand(message: Message):
   await message.answer(text="Python darslari", reply_markup=fron)
#python
@dp.message(F.data== "Python")
async def StartCommand(message: Message):
   await message.answer(text="python darslari", reply_markup=pyton)


@dp.message(F.data== "1 - dars")
async def StartCommand(message: Message):
   await message.answer(text="https://t.me/botvideo12/26", reply_markup=pyton)


@dp.message(F.data== "2 - dars")
async def StartCommand(message: Message):
   await message.answer(text="https://t.me/botvideo12/27", reply_markup=pyton)


@dp.message(F.data== "3 - dars")
async def StartCommand(message: Message):
   await message.answer(text="https://t.me/botvideo12/28", reply_markup=pyton)


@dp.message(F.data== "4 - dars")
async def StartCommand(message: Message):
   await message.answer(text="https://t.me/botvideo12/29", reply_markup=pyton)


@dp.message(F.data== "5 - dars")
async def StartCommand(message: Message):
   await message.answer(text="https://t.me/botvideo12/30", reply_markup=pyton)


@dp.message(F.data== "6 - dars")
async def StartCommand(message: Message):
   await message.answer(text="https://t.me/botvideo12/30", reply_markup=pyton)


@dp.message(F.data== "7 - dars")
async def StartCommand(message: Message):
   await message.answer(text="https://t.me/botvideo12/31", reply_markup=pyton)




async def main():
  await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())