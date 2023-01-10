import telebot
from cfg import TOKEN
import random

bot = telebot.TeleBot(TOKEN)
candys = 117
gameover = 0
turn = int()
enable_game = dict()
# @bot.message_handler(func=lambda message: True)
# def echo_all(message):
#     global candys
#     taken = int(message.text)
#     candys -= taken
#     bot.send_message(message.chat.id, str('Оставшееся число конфет: ', candys))


def game_proccess(message):
    global gameover
    if gameover == 0:
        return True
    else:
        return False



@bot.message_handler(commands=['start'])
def game_start(message):
    global candys, gameover, turn
    bot.send_message (message.chat.id, "ОЧЕРЕДНОСТЬ ИГРОКОВ ОПРЕДЕЛЯЕТСЯ РАНДОМНО")
    candys = 117    
    turn = random.randint(0,1)
    if turn == 0:
        bot.send_message (message.chat.id, "ВЫ ХОДИТЕ ПЕРВЫМ")
    else:
        bot.send_message (message.chat.id, "ПЕРВЫМ ХОДИТ БОТ")
    gameover = 0

@bot.message_handler(func=game_proccess)
def game_body(message):
    global candys, gameover, turn
    max_qnt = candys if candys < 28 else 28
    bot.send_message (message.chat.id, str("Оставшееся число конфет:", candys))
    if turn == 0 and candys > 0:
        bot.send_message (message.chat.id,'ВАШ ХОД')
        bot.send_message (message.chat.id,'Введите число конфет, которые Вы забираете со стола (число не должно превышать 28)')
        taken = int(message.text)
        candys = candys - taken
        turn = 1
    elif turn == 1 and candys > 0:
        bot.send_message (message.chat.id,'ХОД БОТА')
        taken = random.randint(1,max_qnt)
        bot.send_message (message.chat.id, str("Число конфет, которые забирает бот:", taken))
        count = candys - taken
        turn = 0
    else:
        gameover = 1 
    if gameover == 1 and turn == 1:
        bot.send_message (message.chat.id,'ВЫ ВЫИГРАЛИ!')
    elif gameover == 1 and turn == 0:
        bot.send_message (message.chat.id,'ВЫИГРАЛ БОТ')

bot.infinity_polling()