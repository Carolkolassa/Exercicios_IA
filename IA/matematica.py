from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer 

#Criamos o ChatBot chamado KolassaBot
chatbot = ChatBot('KolassaBot',
    logic_adapters=[
        "chatterbot.logic.MathematicalEvaluation",
        "chatterbot.logic.TimeLogicAdapter"
    ])

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