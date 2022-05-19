from django.core.management.base import BaseCommand
from telegram import Bot
from telegram.ext import CommandHandler, MessageHandler, Filters, Updater
from telegram.utils.request import Request
from django.conf import settings
from .bot_9.voronka1 import *
from .bot_9.voronka4 import *
from .bot_9.voronka2 import *
from .bot_9.voronka3 import *
from .bot_9.voronka5 import *


class Command(BaseCommand):
    help = "Телеграм бот"

    def handle(self, *args, **options):
        request = Request(
            connect_timeout=0.5,
            read_timeout=1.0,
        )
        bot = Bot(
            request=request,
            token= settings.TOKEN9,
        )
        print(bot.get_me())
        update = Updater(
            bot=bot,
            use_context=True,
        )
        #voronka1
        message_handler = MessageHandler(Filters.text,  start)
        update.dispatcher.add_handler(message_handler)
        message_handler2 = CommandHandler("go", mes2)
        update.dispatcher.add_handler(message_handler2)
        message_handler2 = CommandHandler("ok", mes3)
        update.dispatcher.add_handler(message_handler2)
        message_handler2 = CommandHandler("mes4", mes4)
        update.dispatcher.add_handler(message_handler2)
        message_handler2 = CommandHandler("mes5", mes5)
        update.dispatcher.add_handler(message_handler2)
        message_handler2 = CommandHandler("mes6", mes6)
        update.dispatcher.add_handler(message_handler2)
        message_handler2 = CommandHandler("mes7", mes7)
        update.dispatcher.add_handler(message_handler2)
        message_handler2 = CommandHandler("mes8", mes8)
        update.dispatcher.add_handler(message_handler2)
        message_handler2 = CommandHandler("mes9", mes9)
        update.dispatcher.add_handler(message_handler2)
        message_handler2 = CommandHandler("mes10", mes10)
        update.dispatcher.add_handler(message_handler2)

        # voronka2
        message_handler2 = CommandHandler("Vor2_mes2", Vor2_mes2)
        update.dispatcher.add_handler(message_handler2)
        message_handler2 = CommandHandler("Vor2_mes3", Vor2_mes3)
        update.dispatcher.add_handler(message_handler2)
        message_handler2 = CommandHandler("Vor2_mes4", Vor2_mes4)
        update.dispatcher.add_handler(message_handler2)
        message_handler2 = CommandHandler("Vor2_mes5", Vor2_mes5)
        update.dispatcher.add_handler(message_handler2)
        message_handler2 = CommandHandler("Vor2_mes6", Vor2_mes6)
        update.dispatcher.add_handler(message_handler2)
        message_handler2 = CommandHandler("Vor2_mes7", Vor2_mes7)
        update.dispatcher.add_handler(message_handler2)
        message_handler2 = CommandHandler("Vor2_mes8", Vor2_mes8)
        update.dispatcher.add_handler(message_handler2)
        message_handler2 = CommandHandler("Vor2_mes9", Vor2_mes9)
        update.dispatcher.add_handler(message_handler2)
        message_handler2 = CommandHandler("Vor2_mes10", Vor2_mes10)
        update.dispatcher.add_handler(message_handler2)

        # voronka3
        message_handler2 = CommandHandler("Vor3_mes2", Vor3_mes2)
        update.dispatcher.add_handler(message_handler2)
        message_handler2 = CommandHandler("Vor3_mes3", Vor3_mes3)
        update.dispatcher.add_handler(message_handler2)
        message_handler2 = CommandHandler("Vor3_mes4", Vor3_mes4)
        update.dispatcher.add_handler(message_handler2)
        message_handler2 = CommandHandler("Vor3_mes5", Vor3_mes5)
        update.dispatcher.add_handler(message_handler2)
        message_handler2 = CommandHandler("Vor3_mes6", Vor3_mes6)
        update.dispatcher.add_handler(message_handler2)
        message_handler2 = CommandHandler("Vor3_mes7", Vor3_mes7)
        update.dispatcher.add_handler(message_handler2)
        message_handler2 = CommandHandler("Vor3_mes8", Vor3_mes8)
        update.dispatcher.add_handler(message_handler2)
        message_handler2 = CommandHandler("Vor3_mes9", Vor3_mes9)
        update.dispatcher.add_handler(message_handler2)
        message_handler2 = CommandHandler("Vor3_mes210", Vor3_mes10)
        update.dispatcher.add_handler(message_handler2)

        # voronka4
        message_handler2 = CommandHandler("Vor4_mes2", Vor4_mes2)
        update.dispatcher.add_handler(message_handler2)
        message_handler2 = CommandHandler("Vor4_mes3", Vor4_mes3)
        update.dispatcher.add_handler(message_handler2)
        message_handler2 = CommandHandler("Vor4_mes4", Vor4_mes4)
        update.dispatcher.add_handler(message_handler2)
        message_handler2 = CommandHandler("Vor4_mes5", Vor4_mes5)
        update.dispatcher.add_handler(message_handler2)
        message_handler2 = CommandHandler("Vor4_mes6", Vor4_mes6)
        update.dispatcher.add_handler(message_handler2)
        message_handler2 = CommandHandler("Vor4_mes7", Vor4_mes7)
        update.dispatcher.add_handler(message_handler2)
        message_handler2 = CommandHandler("Vor4_mes8", Vor4_mes8)
        update.dispatcher.add_handler(message_handler2)
        message_handler2 = CommandHandler("Vor4_mes9", Vor4_mes9)
        update.dispatcher.add_handler(message_handler2)
        message_handler2 = CommandHandler("Vor4_mes10", Vor4_mes10)
        update.dispatcher.add_handler(message_handler2)

        # voronka5
        message_handler2 = CommandHandler("Vor5_mes2", Vor5_mes2)
        update.dispatcher.add_handler(message_handler2)
        message_handler2 = CommandHandler("Vor5_mes3", Vor5_mes3)
        update.dispatcher.add_handler(message_handler2)
        message_handler2 = CommandHandler("Vor5_mes4", Vor5_mes4)
        update.dispatcher.add_handler(message_handler2)
        message_handler2 = CommandHandler("Vor5_mes5", Vor5_mes5)
        update.dispatcher.add_handler(message_handler2)
        message_handler2 = CommandHandler("Vor5_mes6", Vor5_mes6)
        update.dispatcher.add_handler(message_handler2)
        message_handler2 = CommandHandler("Vor5_mes7", Vor5_mes7)
        update.dispatcher.add_handler(message_handler2)
        message_handler2 = CommandHandler("Vor5_mes8", Vor5_mes8)
        update.dispatcher.add_handler(message_handler2)
        message_handler2 = CommandHandler("Vor5_mes9", Vor5_mes9)
        update.dispatcher.add_handler(message_handler2)
        message_handler2 = CommandHandler("Vor5_mes10", Vor5_mes10)
        update.dispatcher.add_handler(message_handler2)



        update.start_polling()
        update.idle()



