from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer 

#Criamos o ChatBot chamado KolassaBot
chatbot = ChatBot('KolassaBot')

#Criamos um "treinador" para o KolassaBot
trainer = ListTrainer(chatbot)

conversa = ['Oi', 'olá, tudo bem?',
'Tudo bem?','Tudo ótimo',
'Voce gosta de programar?', 'Sim, eu programo em python',
'Você torce para quem?', 'Somos colorados, perdemos o grenal... Colorado mesmo assim!']

#Executamos o treinamento do MadalBot com o conjunto de palavras/sentenças
trainer.train(conversa)

#Laço de repetições para a conversa acontecer
while True:
    #Solicita uma entrada de dados para o usuário 
    pergunta = input("Usuarios: ")
    #Busca uma resposta do KolassaBot
    resposta = chatbot.get_response(pergunta)

    #Se o grau de confiança do KolassaBot for inferior a 0.5, informa que não sabe o que responder 
    if float(resposta.confidence) > 0.5:
        print('KolassaBot: ', resposta)
    else:
        print('KolassaBot: Me desculpe! Não tenho uma resposta para essa pergunta')