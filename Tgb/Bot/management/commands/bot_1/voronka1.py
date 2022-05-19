from admin_app.models import Profile, Massage
from telegram import Update

from telegram.ext import CallbackContext


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
            "name": update.message.from_user.first_name,
        }
    )
    try:
        mes1 = Massage.objects.all().first()
        name = update.message.from_user.first_name
        message1 = f"{name} {mes1}"
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
