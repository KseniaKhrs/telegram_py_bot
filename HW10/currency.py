import telebot
import random

bot = telebot.TeleBot('5910801471:AAEZHLzTRPRAjYVtLC9ZKVpmeOxstDF48Ic')


import requests

@bot.message_handler(commands=['currency'])
def start_bot(message):
    res = requests.get('https://www.cbr-xml-daily.ru/daily_json.js').json()
    bot.send_message (message.chat.id, str('Выберите нужную валюту из списка и введите трехбуквенное обозначение'))
    bot.send_message (message.chat.id, (', '.join(res['Valute'].keys())))



@bot.message_handler(content_types=['text'])
def start1_bot(message):
    res = requests.get('https://www.cbr-xml-daily.ru/daily_json.js').json()
    result = res['Valute']["USD"]['Value']
    bot.send_message (message.chat.id, f'{result} RUB')

bot.infinity_polling()
