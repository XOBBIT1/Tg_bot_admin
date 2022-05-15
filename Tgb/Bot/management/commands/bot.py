from django.core.management.base import BaseCommand
from telegram import Bot
from telegram import Update
from telegram.ext import CallbackContext, Filters, MessageHandler, Updater, CommandHandler
from telegram.utils.request import Request
from django.conf import settings
from admin_app.models import Profile, Massage


def log_errors(f):
    def inner(*args,**kwargs):
        try:
            return f(*args,**kwargs)
        except Exception as e:
            error_message = f"Произошла ошибка:{e}"
            print(error_message)
            raise e
    return inner

@log_errors
def start(update: Update, context: CallbackContext):
    chat_id = update.message.chat_id
    p, _ = Profile.objects.get_or_create(
        id=chat_id,
        defaults={
            "name": update.message.from_user.username,
        }
    )
    try:
        mes1 = Massage.objects.all().first()
        message1 = f"{mes1}"
        update.message.reply_text(message1)

    except Exception:
        print("")

@log_errors
def mes2(update: Update, context: CallbackContext):
    try:
        mes1 = Massage.objects.get(id=2)
        message1 = f"{mes1}"
        update.message.reply_text(message1)

    except Exception:
        print("")


@log_errors
def mes3(update: Update, context: CallbackContext):
    try:
        mes1 = Massage.objects.get(id=3)
        message1 = f"{mes1}"
        update.message.reply_text(message1)

    except Exception:
        print("")


@log_errors
def mes4(update: Update, context: CallbackContext):
    try:
        mes1 = Massage.objects.get(id=4)
        message1 = f"{mes1}"
        update.message.reply_text(message1)

    except Exception:
        print("")


@log_errors
def mes5(update: Update, context: CallbackContext):
    try:
        mes1 = Massage.objects.get(id=5)
        message1 = f"{mes1}"
        update.message.reply_text(message1)

    except Exception:
        print("")


@log_errors
def mes6(update: Update, context: CallbackContext):
    try:
        mes1 = Massage.objects.get(id=6)
        message1 = f"{mes1}"
        update.message.reply_text(message1)

    except Exception:
        print("")


@log_errors
def mes7(update: Update, context: CallbackContext):
    try:
        mes1 = Massage.objects.get(id=7)
        message1 = f"{mes1}"
        update.message.reply_text(message1)

    except Exception:
        print("")


@log_errors
def mes8(update: Update, context: CallbackContext):
    try:
        mes1 = Massage.objects.all().first()
        message1 = f"{mes1}"
        update.message.reply_text(message1)

    except Exception:
        print("")

@log_errors
def mes8(update: Update, context: CallbackContext):
    try:
        mes1 = Massage.objects.get(id=8)
        message1 = f"{mes1}"
        update.message.reply_text(message1)

    except Exception:
        print("")

@log_errors
def mes9(update: Update, context: CallbackContext):
    try:
        mes1 = Massage.objects.get(id=9)
        message1 = f"{mes1}"
        update.message.reply_text(message1)

    except Exception:
        print("")


@log_errors
def mes10(update: Update, context: CallbackContext):
    try:
        mes1 = Massage.objects.get(id=10)
        message1 = f"{mes1}"
        update.message.reply_text(message1)

    except Exception:
        print("")


class Command(BaseCommand):
    help = "Телеграм бот"

    def handle(self, *args, **options):
        request = Request(
            connect_timeout=0.5,
            read_timeout=1.0,
        )
        bot = Bot(
            request=request,
            token=settings.TOKEN,
        )
        print(bot.get_me())
        update = Updater(
            bot=bot,
            use_context=True,
        )

        message_handler = CommandHandler("start", start)
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


        update.start_polling()
        update.idle()
