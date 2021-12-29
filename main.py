import os
import logging
from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher.filters import Text
from aiogram.types import chat, message
from config import *
from flask import Flask, request
import psycopg2
db_con=psycopg2.connect(db_baza, sslmode="require")
db_ob=db_con.cursor()


logging.basicConfig(level=logging.INFO)
bot = Bot(token=token)
dp = Dispatcher(bot)
@dp.message_handler(commands=['start','restart'])
async def send_welcome(message: types.Message):
    await message.reply(f"🤓Assalom aleykum✋\n{message.chat.full_name}\n🥤GulDU Coffee Clubga\n😍XUSH KELDINGIZ‼️")
    user_id=message.chat.id
    name=message.chat.full_name
    db_ob.execute(f"SELECT id FROM cofe_baza WHERE id={message.chat.id}")
    data = db_ob.fetchone()
    if data is None:
        db_ob.execute("INSERT INTO cofe_baza(id,username) VALUES (%s,%s)", (user_id, name))
        db_con.commit()
    else:
        await bot.delete_message(message.chat.id, message.message_id)
        await message.answer("🆘 Ushbu raqam foydalanuvchi raqamiga mos kelmadi❌❗️")

if __name__=='__main__':
    executor.start_polling(dp, skip_updates=True)
