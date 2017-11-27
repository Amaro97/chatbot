# -*- coding: utf-8 -*-
from chatterbot.trainers import ListTrainer
from chatterbot import ChatBot
from datetime import datetime

bot=ChatBot('Test')
dialogo_inicial = ['Oi','Olá','Olá, bom dia','bom dia','bom dia, como vai?','estou bem']
dialogo_entreterimento = ['Que filme você gosta?','Eu adoro assistir Ex Machina','Qual seu filme favorito?','Ahhh... É difícil escolher, mas IROM MAN é realmente muito bom!']
bot.set_trainer(ListTrainer)

bot.train(dialogo_inicial)
bot.train(dialogo_entreterimento)
now = datetime.now()



if(now.hour > 0 and  now.hour < 12):
    print('bom dia')
if(now.hour  > 12 and now.hour  < 18):
   print('Boa tarde')



while(True):
	quest = input('Você: ')
	response = bot.get_response(quest)
	print('Bot: ',response)
	# if float(response.confidence)>0.5:
	
	#else:
		#print('Bot: Sorry, não entendi.')

