from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update #Создать класс как дочерний

#class buttons:
#    def __init__():
#        self.reply_markup = InlineKeyboardMarkup(keyboard)
#
#    def menu():
#        keyboard = [
#            [
#                InlineKeyboardButton("Option 1", callback_data="1"),
#                InlineKeyboardButton("Option 2", callback_data="2"),
#            ],
#            [InlineKeyboardButton("Option 3", callback_data="3")],
#        ]
#
#        
#        return self.reply_markup 
#
#    def __getattribute__():
#        self.reply_markup = menu()

def menu():
    keyboard = [
        [
            InlineKeyboardButton("Option 1", callback_data="1"),
            InlineKeyboardButton("Option 2", callback_data="2"),
        ],
        [InlineKeyboardButton("Option 3", callback_data="3")],
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)

    return reply_markup    