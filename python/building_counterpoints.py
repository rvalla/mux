import json as js
from counterpoint import Counterpoint

#Example code to use matrix object to create a musical texture...
config_files = [js.load(open("config/threevoices_random_counterpoint.json")),
				js.load(open("config/threevoices_conditional_counterpoint.json")),
				js.load(open("config/threevoices_control_counterpoint.json")),
				js.load(open("config/threevoices_markov_counterpoint.json"))]

for c in config_files:
	for i in range(3):
		cp = Counterpoint(c)
		filename = c["counterpoint"] + str(i + 1) + ".xml"
		cp.save_score("xml/", filename, "xml")
		#cp.show_score()
