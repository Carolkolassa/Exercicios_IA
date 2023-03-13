from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

chatbot = ChatBot('KolassaBot')

# Monta o treinador que será baseado em um "corpus"
trainer = ChatterBotCorpusTrainer(chatbot)
# Define o corpus para português
trainer.train('chatterbot.corpus.portuguese')

# Exporta o arquivo com o conteúdo treinado
trainer.export_for_training('./data.json')