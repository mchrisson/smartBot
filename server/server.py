from flask import Flask, session, redirect, url_for, escape, request, jsonify
from datetime import timedelta
import copy
from os.path import dirname, abspath, join

from bot.intentsDictionary import intent
from bot.actions import action
from bot.slots import slotsDictionary
from bot.smartBot import SmartBot

modelFile = "model_output.json"
modelPath = join(dirname(abspath(__file__)), modelFile)

bot = SmartBot(modelPath, action, intent)

app = Flask(__name__)

# Set the secret key to some random bytes. Keep this really secret!
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

def getInitData() :
	return {
			'intentsSubset': ['I_Welcome_Name_Input'],
			'slotsDictionary': slotsDictionary
		}

@app.before_request
def make_session_permanent():
	session.permanent = True
	app.permanent_session_lifetime = timedelta(minutes=60)

@app.route('/process', methods=['POST'])
def process():
	if 'session-data' in session:
		sessionData = session['session-data']
		reqData = request.get_json()
		print(reqData)
		response = bot.parseInput( reqData['text'], sessionData['intentsSubset'], sessionData['slotsDictionary'] )
		sessionData['intentsSubset'] = response['intentsSubset']
		print(sessionData['slotsDictionary'])
		
		return jsonify(response)

	return redirect(url_for('init'))

@app.route('/init', methods=['GET'])
def init():
	session['session-data'] = copy.deepcopy(getInitData())
	return 'Session Initialized'

@app.route('/end')
def end():
	# remove the session-data from the session if it's there
	session.pop('session-data', None)
	return 'Session ended'

app.run(host="0.0.0.0", port="5001")
