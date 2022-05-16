from admin_app.models import ProfileVor3, MassageVor3
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
def Vor3_mes2(update: Update, context: CallbackContext):
    try:
        mes1 = MassageVor3.objects.get(id=1)
        message1 = f"{mes1}"
        update.message.reply_text(message1)

    except Exception:
        print("")


@log_errors
def Vor3_mes3(update: Update, context: CallbackContext):
    try:
        mes1 = MassageVor3.objects.get(id=2)
        message1 = f"{mes1}"
        update.message.reply_text(message1)

    except Exception:
        print("")


@log_errors
def Vor3_mes4(update: Update, context: CallbackContext):
    try:
        mes1 = MassageVor3.objects.get(id=3)
        message1 = f"{mes1}"
        update.message.reply_text(message1)

    except Exception:
        print("")


@log_errors
def Vor3_mes5(update: Update, context: CallbackContext):
    try:
        mes1 = MassageVor3.objects.get(id=4)
        message1 = f"{mes1}"
        update.message.reply_text(message1)

    except Exception:
        print("")


@log_errors
def Vor3_mes6(update: Update, context: CallbackContext):
    try:
        mes1 = MassageVor3.objects.get(id=5)
        message1 = f"{mes1}"
        update.message.reply_text(message1)

    except Exception:
        print("")


@log_errors
def Vor3_mes7(update: Update, context: CallbackContext):
    try:
        mes1 = MassageVor3.objects.get(id=6)
        message1 = f"{mes1}"
        update.message.reply_text(message1)

    except Exception:
        print("")

@log_errors
def Vor3_mes8(update: Update, context: CallbackContext):
    try:
        mes1 = MassageVor3.objects.get(id=7)
        message1 = f"{mes1}"
        update.message.reply_text(message1)

    except Exception:
        print("")

@log_errors
def Vor3_mes9(update: Update, context: CallbackContext):
    try:
        mes1 = MassageVor3.objects.get(id=8)
        message1 = f"{mes1}"
        update.message.reply_text(message1)

    except Exception:
        print("")


@log_errors
def Vor3_mes10(update: Update, context: CallbackContext):
    try:
        mes1 = MassageVor3.objects.get(id=9)
        message1 = f"{mes1}"
        update.message.reply_text(message1)

    except Exception:
        print("")