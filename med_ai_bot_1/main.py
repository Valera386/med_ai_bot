import os                                                                           #Сделать что то вроде дерева, где main.py - основной свол, а остальные предаточные

import logging 
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram import Update 
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler, CallbackQueryHandler
#from interface.buttons import buttons as b 
from interface.buttons import menu 

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
        text="I'm a bot, please talk to me!")

    reply_markup = menu()

    await update.message.reply_text("Please choose:", reply_markup=reply_markup)
        
        

async def buttons(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    if not query: 
        logger.warning("effectbve_chat is None") 
        return 
    await query.answer()

    await query.edit_message_text(text=f"Selected optionss: {query.data}")

         
if __name__ == '__main__': 
    application = ApplicationBuilder().token(TELEGRAM_BOT_TOKEN).build() 
     
    start_handler = CommandHandler('start', start) #Здест указываются команды бота
    application.add_handler(CallbackQueryHandler(buttons))
    application.add_handler(start_handler) 
     
    application.run_polling()

