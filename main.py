import Constants as keys
from telegram.ext import *
import Responses as R

print("Bot started...")


def start_command(update, context):
    update.message.reply_text('Hoşgeldiniz, Ben YKS sürecinde sana yardım etmek isteyen bir botum')


def my_id(update, context):
    update.message.reply_text('my_id komutu çalıştırıldı')("Gezme ceylan bu dağlarda gezme")


def help_command(update, context):
    update.message.reply_text('YKS sürecinde zorlandığın bir konu, unuttuğun bir formül olursa bana söyleyebilirsin')


def qaz_command(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="I'm a bot, please talk to me!")


def handle_message(update, context):
    text = str(update.message.text).lower()
    response = R.sample_responses(text)

    update.message.reply_text(response)


def error(update, context):
    print(f"Update {update} caused error {context.error}")


def main():
    updater = Updater(keys.API_KEY, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start_command))
    dp.add_handler(CommandHandler("help", help_command))
    dp.add_handler(CommandHandler("me", my_id))
    dp.add_handler(CommandHandler("stat", qaz_command))

    dp.add_handler(MessageHandler(Filters.text, handle_message))

    dp.add_error_handler(error)

    updater.start_polling(0)
    updater.idle()

main()

