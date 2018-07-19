from __future__ import unicode_literals, print_function

import io
import json
from os.path import dirname, abspath, join

from snips_nlu import SnipsNLUEngine, load_resources
from snips_nlu.default_configs import CONFIG_EN

SAMPLE_DATASET_PATH = join(dirname(abspath(__file__)), "training_data_2.json")
print(SAMPLE_DATASET_PATH)
with io.open(SAMPLE_DATASET_PATH) as f:
    sample_dataset = json.load(f)

load_resources("en")
nlu_engine = SnipsNLUEngine(config=CONFIG_EN)
nlu_engine.fit(sample_dataset)

json_model = nlu_engine.to_dict()
with io.open('model_output.json', 'w') as f:
	f.write(json.dumps(json_model, indent=2))

