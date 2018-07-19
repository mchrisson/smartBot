from os.path import dirname, abspath, join

from intentsDictionary import intent
from actions import action
from slots import slotsDictionary
from smartBot import SmartBot


modelFile = "../model_output.json"
modelPath = join(dirname(abspath(__file__)), modelFile)

bot = SmartBot(modelPath, action, intent) 

#Starting Point
print('ADA: Hi, my name is ADA. I am your digital assistant may I know your name?')

intentsSubset = ['I_Welcome_Name_Input']
while True :
	text = input('User: ')
	response = bot.parseInput( text, intentsSubset, slotsDictionary )
	print("######\n", response, "\n", slotsDictionary, "\n", intentsSubset, "\n######\n")
	intentsSubset = response['intentsSubset']

	
	print('ADA: ',response['message'])

	if response['intent'] == 'I_Goodbye_HEADER' :
		break

