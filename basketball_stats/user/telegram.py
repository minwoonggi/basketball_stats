import telegram
token = '5211083297:AAEdGA6PlkYa1OJFIpAV8MTqmvzCFgi62YA'
bot = telegram.Bot(token=token)
chat_id = 1933675096

def sendMsg(message):
    bot.sendMessage(chat_id=chat_id, text=message, parse_mode = 'Markdown', disable_web_page_preview=True)