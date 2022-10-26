from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import random

greeting = 'На столе лежит 150 конфет.\nИграют два игрока, делая ход друг после друга.\nПервый ход определяется жеребьёвкой.\nЗа один ход можно забрать не более чем 28 конфет.\nВсе конфеты оппонента достаются сделавшему последний ход.\nСколько конфет нужно взять первому игроку,\nчтобы забрать все конфеты у своего конкурента?\nДля начала игры введите команду /play'

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'{greeting}')

def get_number(): 
    number = random.randint(0,30)
    return number

async def send_message(update: Update, context: ContextTypes.DEFAULT_TYPE, text) -> None:
    await update.message.reply_text(text)

async def play(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    players = meeting_players(update.effective_user.first_name)
    n = 150    
    victory = await play_game(n, players, update)
    if not victory:
         await update.message.reply_text('Нет победителя!')
    else:
         await update.message.reply_text(f'Победил {victory}!')

def meeting_players(name):
    player1 = name
    player2 = 'Topazik_bot'
    return [player1, player2]

async def play_game(n, players, update):
    count = random.randint(0,1)
    await update.message.reply_text(f'В результате жеребьевки первым ходит игрок: {players[count]}.')

    while n > 0:
        if (count % 2) == 1:
            move = 150 % 28 + 1
            await update.message.reply_text(f'Второй игрок: Я забираю {move} конфет!')
            n = n - move
        else:
            await update.message.reply_text(f'{players[0]}, возьмите конфеты:')
            move = get_number()
            await update.message.reply_text(f'Вы взяли {move}')
            if move > 28:
                await update.message.reply_text(f'Можно взять не более 28 конфет, переход хода.')
            else:
                n = n - move
        if n > 0:
            await update.message.reply_text(f'Осталось {n} конфет!')
            count += 1
        else:
            await update.message.reply_text('Все конфеты разобраны.')
    return players[count % 2]
