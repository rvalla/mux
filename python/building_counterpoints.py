import json as js
from counterpoint import Counterpoint

#Example code to use matrix object to create a musical texture...
config_files = [js.load(open("config/twovoices_counterpoint.json"))]

for c in config_files:
	for i in range(1):
		cp = Counterpoint(c)
		filename = c["counterpoint"] + str(i + 3) + ".xml"
		#cp.save_score("xml/", filename, "xml")
		cp.show_score()
