import telebot
from random import randint

bot = telebot.TeleBot("5585824906:AAFbBSE57XYl_yvkFO7MK0ueOmZIlhKoMnY")

is_game_on = False
candies = 2021

def bots_move(message):
    global candies, is_game_on
    n = randint(1, 28)
    if n < candies:
        candies -= n
        bot.send_message(message.chat.id, f'Я забрал {n} конфет. Осталось {candies} конфет.')
    else:
        is_game_on = False
        bot.send_message(message.chat.id, 'Игра окончена. Я выйграл!')

@bot.message_handler(commands=['start'])
def send_welcome(message):
	bot.reply_to(message, "Привет, давай сыграем в игру 2021 конфета.\n\
Условие задачи: На столе лежит 2021 конфета.\n\
Играют два игрока (ты и я) делая ход друг после друга.\n\
Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет.\n\
Все конфеты оппонента достаются сделавшему последний ход.\n\
Отправь /ready, если готов, или /help, чтобы прочитать правила")

@bot.message_handler(commands=['help'])
def send_rules(message):
	bot.reply_to(message, "Привет, давай сыграем в игру 2021 конфета.\n\
Условие задачи: На столе лежит 2021 конфета.\n\
Играют два игрока (ты и я) делая ход друг после друга.\n\
Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет.\n\
Все конфеты оппонента достаются сделавшему последний ход.\n\
Отправь /ready, если готов.")

@bot.message_handler(commands=['ready'])
def game_init(message):
    global is_game_on, player1, player2, flag
    player1 = message.from_user.first_name
    player2 = "Bot"
    if not is_game_on:
        global candies
        is_game_on = True
        bot.send_message(message.chat.id, f"Привет, {player1}. Ты играешь против меня. Сейчас случайным образом определится, кто ходит первым.")
        flag = randint(0,2)
        if flag:
            bot.send_message(message.chat.id, f"Первым ходишь ты, {player1}")
            bot.send_message(message.chat.id, f"Возьми от 1 до 28 конфет")
        else:
            bot.send_message(message.chat.id, f"Первым хожу я")
            bots_move(message)
        if is_game_on: flag = not flag

@bot.message_handler(func = lambda _: is_game_on)
def players_move(message):
    global candies, is_game_on
    try:
        n = int(message.text)
        if n > 28:
            bot.send_message(message.chat.id, 'Ты не можешь взять больше 28 конфет. Попытайся ещё раз.')
        else:
            if n < candies:
                candies -= n
                bot.send_message(message.chat.id, f'Осталось {candies} конфет.')
                bots_move(message)
                if is_game_on: bot.send_message(message.chat.id,  'Возьми не более 28 конфет.')
            else:
                candies = 0
                is_game_on = False
                bot.send_message(message.chat.id, 'Игра окончена. Ты выйграл!')
    except:
        bot.send_message(message.chat.id, 'Введено не целое число или не число. Попытайся ещё раз.')

bot.infinity_polling()