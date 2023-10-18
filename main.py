import telebot
from extensions import CurrencyExchange, ConversionException
from config import keys, TOKEN

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(content_types=['photo', ])
def say_lmao(message: telebot.types.Message):
    bot.reply_to(message, 'Вот это прикол XDD')

@bot.message_handler(content_types=["voice",])
def function_name(message):
    bot.send_message(message.chat.id, "У тебя красивый голос!")

@bot.message_handler(content_types=['document', 'audio'])
def handle_docs_audio(message):
    pass



@bot.message_handler(commands=['start', 'help'])
def help(message: telebot.types.Message):
    text = ('Чтобы начать работу введите команду боту в следующем формате:\n<имя валюты>\
<в какую валюту перевести>\
<количество переводимой валюты>\nУвидить список всех доступеых валют: /values')
    bot.reply_to(message, text)

@bot.message_handler(commands=['values'])
def values(message: telebot.types.Message):
    text = "Доступные валюты:"
    for key in keys.keys():
        text = '\n'.join((text, key, ))
    bot.reply_to(message, text)

@bot.message_handler(content_types=['text',])
def convert(message: telebot.types.Message):
    values = message.text.split(' ')

    if len(values) != 3:
        raise ConversionException('Слишком много параметров')
    else:
        quote, base, amount = values
        total_base = CurrencyExchange.convert(quote, base, amount)
        text = f'Цена {amount} {quote} в {base} - {total_base}'
        bot.send_message(message.chat.id, text)

bot.polling()
