import telebot

bot = telebot.TeleBot(token='#')

GROUPID = -100######

def voisins(lastNumbersTelegram):
    bot.send_message(GROUPID, 
                '\U000027a1 Repetição de *Tier e Orphelins* identificado!\n\U00002714 *Aposta feita.*\nOs numeros chamados foram: ' + str(lastNumbersTelegram), 
                 parse_mode= 'Markdown')

def gale():
    bot.send_message(GROUPID, 
                '\u2757 Gale!!', 
                 parse_mode= 'Markdown')

def green(numbers):
    bot.send_message(GROUPID, 
                '\u2705 Green!! \nOs números foram: ' + str(numbers), 
                 parse_mode= 'Markdown')
            
def inactive():
    bot.send_message(GROUPID, 
                'Ficou inativo, recarregado.', 
                 parse_mode= 'Markdown')
                
def dezonOne(numbers):
    bot.send_message(GROUPID, '\U0001F3B0 Roleta: *Auto Quantum Roulette*\n\U0001F48E Oportunidade encontrada!\n*Repetição na dúzia 1.*\nÚltimos numeros foram: ' + str(numbers), 
                 parse_mode= 'Markdown')

def dezonTwo(numbers):
    bot.send_message(GROUPID, '\U0001F3B0 Roleta: *Auto Quantum Roulette*\n\U0001F48E Oportunidade encontrada!\n*Repetição na dúzia 2.*\nÚltimos numeros foram: ' + str(numbers), 
                 parse_mode= 'Markdown')

def dezonThree(numbers):
    bot.send_message(GROUPID, '\U0001F3B0 Roleta: *Auto Quantum Roulette*\n\U0001F48E Oportunidade encontrada!\n*Repetição na dúzia 3.*\nÚltimos numeros foram: ' + str(numbers), 
                 parse_mode= 'Markdown')

def zero(number):
    bot.send_message(GROUPID, 'Caiu zero e seu número anterior foi: ' + str(number), 
                 parse_mode= 'Markdown')


# def martingale(number):
#     bot.send_message(-627920620, '\u2757 Martingale 1x, necessário cobrir a aposta.\nNúmeros chamados: ' + str(number), 
#                  parse_mode= 'Markdown')