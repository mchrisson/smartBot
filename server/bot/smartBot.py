# Bot Main code
'''

Note: In the following code, the term slotDictionary is used to refer to
the dictionary holding currently available values for its corresponding entities

The term 'entity' in intentsDictionary[intent]['entities'] must be same as 'slot_name' in Training Dataset

The 'entity' parameter in the Training Dataset is different from above mentioned
and it may have a value different. This value can be snips specific aka. 'Builtin Entity' (eg. 'snips/datetime', etc.)
which informs snipsNLU the type of data it needs to extract for that 'slot_name' (eg. a datetime type value when 'snips/datetime' is used)
if this value is not a snips specific type it is treated as 'Custom'

'''
from __future__ import unicode_literals, print_function
import random
import io
import json

from snips_nlu import SnipsNLUEngine

class SmartBot:
	def __init__(self, modelFilePath, action, intentsDictionary):
		self.modelFilePath = modelFilePath
		self.action = action
		self.intentsDictionary = intentsDictionary

		with io.open(self.modelFilePath) as f:
			model = json.load(f)

		self.nlu_engine = SnipsNLUEngine.from_dict(model)

	#Slot Missing Prompt
	def slotMissingPrompt( self, missingSlots ) :
		response = 'Sorry but you didn\'t specify '
		i = 0
		length = len(missingSlots)
		for slot in missingSlots :
			response += slot
			if ( length != 1 and i == length - 2 ) :
				response += ' and '
			elif ( length == 1 or i == length - 1 ) :
				response += ''
			else :
				response += ', '
			i = i + 1
		response += '. Please rephrase your question.'
		return response
	
	#Process Intent and provide response
	def getResponse( self, intent, entities, slotsDictionary ) :
		entityDict = {}
		for entity in entities :
			entityDict[entity["slotName"]] = entity["value"]["value"]
		
		#save slots
		for k, v in entityDict.items():
			slotsDictionary[k] = v
		
		#print(slotsDictionary)
		
		#logic to handle missing slots
		mandatoryEntities = {x for x, v in self.intentsDictionary[intent]['entities'].items() if v}
		#instead of '' we can check for valid list of values for that slot
		missingSlots = {x for x in mandatoryEntities if slotsDictionary[x] == ''}
		if len(missingSlots) != 0 :
			return self.slotMissingPrompt(missingSlots)
		
		#print(slotsDictionary)

		if self.intentsDictionary[intent]['actionProvidesResponse'] :
			#Action provides entire response
			response = self.action[self.intentsDictionary[intent]['action']](slotsDictionary)
		else :
			#select a response, Action provides only Action filled entities (eg. 'SalesVolume')
			response = random.choice(self.intentsDictionary[intent]['responses']).format(slotsDictionary, self.action[self.intentsDictionary[intent]['action']](slotsDictionary))
		
		return response

	def parseInput( self, text, intentsSubset, slotsDictionary ) :
		parsing = self.nlu_engine.parse(text, intentsSubset)
		#print(json.dumps(parsing, indent=1))
		if parsing["intent"] is None :
			return { 'message': 'I didn\'t get what you meant', 'intent': None, 'entities': None, 'intentsSubset': intentsSubset}

		intent = parsing["intent"]["intentName"]
		entities = parsing["slots"]
		intentsSubsetToReturn = self.intentsDictionary[intent]['outIntents']
		return  {
					'message': self.getResponse(intent, entities, slotsDictionary),
					'intent': intent,
					'entities': entities,
					'intentsSubset': intentsSubsetToReturn
				}

		

