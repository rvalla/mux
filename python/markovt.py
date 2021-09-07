import random as rd

class Markovt():
	"A matrix to store Markov values"

	#Building an instance of a Markov matrix...
	def __init__(self, config):
		self.name = config["matrix"]
		self.first_note = config["firstnote"]
		self.data = self.build_data(config)

	#Loading data to the matrix...
	def build_data(self, config):
		data = []
		for r in range(12):
			input = config[str(r)].split(",")
			output = []
			for v in input:
				output.append(float(v))
			data.append(output)
		return data

	#Printing matrix information...
	def __str__(self):
		return "-- Hi, I am a matrix to store Markov values..."
