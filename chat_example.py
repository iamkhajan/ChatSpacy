from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from flask import Flask, render_template, request

app = Flask(__name__)
chatbot = ChatBot('Charlie')
trainer = ListTrainer(chatbot)
def clearChatbotData():
	chatbot.storage.drop()
#call this function when want to clear old data
#clearChatbotData()
trainer=ListTrainer(chatbot)

def train_from_text_file():
	data=open('chat_training_data.txt').read()
	conversations=data.strip().split('\n')
	trainer.train(conversations)

train_from_text_file()
response=chatbot.get_response('Who is prime minister of india?')

@app.route("/")
def home():
 return render_template("index.html")
@app.route("/get")
def get_bot_response():
 userText = request.args.get('msg')
 return str(chatbot.get_response(userText))
if __name__ == "__main__":
 app.run()


