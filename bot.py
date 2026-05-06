import os
import logging
from PIL import Image
from dotenv import load_dotenv
from telegram import Update, ReplyKeyboardMarkup, KeyboardButton
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler, MessageHandler, filters
import qrcode
import base64


load_dotenv()

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

#/start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    button_hello = KeyboardButton("Сгенерировать qr")
    keyboard = ReplyKeyboardMarkup(
        [[button_hello]],
        resize_keyboard=True
    )
    await update.message.reply_text("Кидай ссылку, фото, файл или еще что нибудь и я сделаю qr", reply_markup=keyboard)

#get qr of text or links
async def text_to_qr(update:Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text
    img = qrcode.make(text)
    img.save("temp.png")
    await update.message.reply_photo(photo=open("temp.png","rb"))
    os.remove("temp.png")

#get qr of photo
async def photo_to_qr(update:Update, context: ContextTypes.DEFAULT_TYPE):
    pass
    

#unknown commands
async def unknown(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="Я такой команды не знаю") 

if __name__=='__main__':
    application = ApplicationBuilder().token(os.getenv("BOT_TOKEN")).build()

    start_handler = CommandHandler('start', start)
    unknown_handler = MessageHandler(filters.COMMAND, unknown)
    text_to_qr_handler = MessageHandler(filters.TEXT & (~filters.COMMAND), text_to_qr)
    photo_handler = MessageHandler(filters.PHOTO, photo_to_qr)

    application.add_handler(start_handler)
    application.add_handler(photo_handler)
    application.add_handler(text_to_qr_handler)
    application.add_handler(unknown_handler)

    application.run_polling()