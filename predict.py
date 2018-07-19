from __future__ import unicode_literals, print_function

import io
import json
from os.path import dirname, abspath, join

from snips_nlu import SnipsNLUEngine


MODEL_PATH = join(dirname(abspath(__file__)), "model_output.json")

with io.open(MODEL_PATH) as f:
    model = json.load(f)

nlu_engine = SnipsNLUEngine.from_dict(model)

text = input('Enter text: ')
parsing = nlu_engine.parse(text)
print(json.dumps(parsing, indent=2))
