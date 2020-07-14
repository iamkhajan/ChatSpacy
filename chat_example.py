from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

chatbot = ChatBot('Charlie')
trainer = ListTrainer(chatbot)
def clearChatbotData():
	chatbot.storage.drop()
#call this function when want to clear old data
#clearChatbotData()
trainer=ListTrainer(chatbot)

def train_from_text_file():
	data=open('chattrain.txt').read()
	conversations=data.strip().split('\n')
	trainer.train(conversations)

train_from_text_file()
response=chatbot.get_response('Who is prime minister of india?')
print(response)

