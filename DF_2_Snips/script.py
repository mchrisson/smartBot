import os
from os.path import dirname, abspath, join
import io
import json

path = 'DF_Intents'

output = {
	'intents': {},
	'entities': {},
	'language': 'en'
}

entityFormat = {
	'data': [],
	'use_synonyms': True,
	'automatically_extensible': True
}

entities = set()

for filename in os.listdir(path):
	print('Processing: ' + filename)
	file_path = path +'/' + filename
	intentName = filename.replace('_usersays_en.json','')
	with io.open(file_path) as f:
    		json_data = json.load(f)
	print(intentName)
	
	output['intents'][intentName] = {}
	output['intents'][intentName]['utterances'] = []
	for utterance in json_data:
		data = []
		for x in utterance['data']:
			frag = {}
			frag['text'] = x['text']
			if ( 'alias' in x ):
				entities.add(x['alias'])
				frag['entity'] = x['alias']
				frag['slot_name'] = x['alias']
			data.append(frag)

		output['intents'][intentName]['utterances'].append({'data': data})

	output['entities'] = { k:entityFormat for k in entities }


with io.open('processed_training_data.json', 'w') as f:
	f.write(json.dumps(output, indent=2))
