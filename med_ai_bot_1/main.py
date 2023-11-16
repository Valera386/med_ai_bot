import os                                                                           #Сделать что то вроде дерева, где main.py - основной свол, а остальные предаточные

import logging 
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram import Update 
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler, CallbackQueryHandler
#from interface.buttons import buttons as b 
from interface.buttons import menu, menu2  #кнопки
from database.text.lib_text import text_for_main_men,tz,ax #текста для сообщений

logging.basicConfig( 
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', 
    level=logging.INFO 
) 
 
logger = logging.getLogger(__name__) 
 
TELEGRAM_BOT_TOKEN =  "6424396908:AAGYBYrX7hUMWB7c9qWc_Lq5c5ojxPPwFno"
if not TELEGRAM_BOT_TOKEN: 
    exit("Specify TELEGRAM_BOT_TOKEN onv varible") 
 
 
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE): #функция отвечает за логику команды
    effective_chat = update.effective_chat 
    if not effective_chat: 
        logger.warning("effectbve_chat is None") 
        return 
    await context.bot.send_message(
        chat_id=effective_chat.id,  
        text=text_for_main_men) #можно изменять

    reply_markup = menu()

    await update.message.reply_text("Пожалуйста ответьте", reply_markup=reply_markup)

async def help(update: Update, context: ContextTypes.DEFAULT_TYPE):  # функция отвечает за логику команды
    effective_chat = update.effective_chat
    if not effective_chat:
        logger.warning("effectbve_chat is None")
        return
    await context.bot.send_message(
        chat_id=effective_chat.id,
        text="каков уровень экстренности?")  # можно изменять

    reply_markup = menu2()

    await update.message.reply_text("Пожалуйста выбери!:", reply_markup=reply_markup)

async def answer(update: Update, context: ContextTypes.DEFAULT_TYPE):  # функция отвечает за логику команды
    effective_chat = update.effective_chat
    if not effective_chat:
        logger.warning("effectbve_chat is None")
        return
    await context.bot.send_message(
        chat_id=effective_chat.id,
        text=tz)  # можно изменять

    reply_markup = menu2()

    await update.message.reply_text("Пожалуйста выбери!:", reply_markup=reply_markup)
async def buttons(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query #not
    print(query)
    if not query:
        logger.warning("effectbve_chat is None")
        return
    if query.data=="4":
        await query.answer() #not

        await query.edit_message_text(text=f"Selected optionss: {query.data}")
async def buttons2(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query #not
    if not query:
        logger.warning("effectbve_chat is None")
        return
    await query.answer() #not

    await query.edit_message_text(text=f"Selected optionss: {query.data}")

async def buttons3(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query #not
    if not query:
        logger.warning("effectbve_chat is None")
        return
    await query.answer(text=ax) #not

    await query.edit_message_text(text=ax)


if __name__ == '__main__': 
    application = ApplicationBuilder().token(TELEGRAM_BOT_TOKEN).build() 
     
    start_handler = CommandHandler('start', start) #Здест указываются команды бота
    help_handler = CommandHandler('help', help)  # Здест указываются команды бота
    answer_handler = CommandHandler('answer', answer)  # Здест указываются команды бота
    application.add_handler(CallbackQueryHandler(buttons))
    application.add_handler(CallbackQueryHandler(buttons2))
    application.add_handler(CallbackQueryHandler(buttons3))
    application.add_handler(start_handler)
    application.add_handler(help_handler)
    application.add_handler(answer_handler)
    application.run_polling()

