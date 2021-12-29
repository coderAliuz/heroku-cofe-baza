import os
import logging
from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher.filters import Text
from aiogram.types import chat, message
from config import *
from flask import Flask, request



logging.basicConfig(level=logging.INFO)
bot = Bot(token=token)
dp = Dispatcher(bot)
@dp.message_handler(commands=['start','restart'])
async def send_welcome(message: types.Message):
    await message.reply(f"🤓Assalom aleykum✋\n{message.chat.full_name}\n🥤GulDU Coffee Clubga\n😍XUSH KELDINGIZ‼️")

if __name__=='__main__':
    executor.start_polling(dp, skip_updates=True)
