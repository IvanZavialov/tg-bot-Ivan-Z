

from telegram.ext import Updater, MessageHandler, Filters, CommandHandler
from wiki import search_wiki

token = '5734165676:AAHXrKiZ90GUG7BE_07R2CLl_t-Xg2UwjqM'

def echo(update, context):
    text = update.message.text
    if text.lower() in ['ку', 'приветствую']:
        text = "здравствуйте!"

    update.message.reply_text(f"{text}")


def help(update, context):
    update.message.reply_text("Список доступных команд \n • /help - вывод помощи")


def start(update, context):
    update.message.reply_text("ку! \n набери /help, чтобы чекнуть список команд")


def wiki(update, context):
    print(context.args)
    word = "".join(context.args)
    if word:
        update.message.reply_text(f"Ищем {word}")
        summary, url = search_wiki(word)
        update.message.reply_text(summary+url)
    else:
        update.message.reply_text("Запрос не должен быть null")

def main():
    updater = Updater(token, use_context=True)
    dp = updater.dispatcher
    print("Бот запущен")

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help))
    dp.add_handler(CommandHandler('wiki', wiki))

    dp.add_handler(MessageHandler(Filters.text, echo))

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()

