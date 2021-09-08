from music21 import *
import json as js
import random as rd
import util as ut
from markovt import Markovt
from scores import m21Score

class Counterpoint(m21Score):
	"A machine to make a random couterpoint"

	#Building an instance of a Counterpoint..
	def __init__(self, config):
		m21Score.__init__(self, config["title"], config["composer"], config["key_signature"],
							config["time_signature"], config["parts"])
		self.cycles = config["cycles"] #Number of cycles
		self.mode = config["mode"] #Texture mode: random, control, markov, conditional
		self.control_list = self.get_control_list(config["control"])
		self.t_unit = config["time_unit"]
		self.t_measure = config["time_measure"]
		self.t_set = int(self.t_measure / self.t_unit)
		self.midi_offset = config["midi_offset"]
		self.voice_offset = config["voice_offset"]
		if config["markov"]:
			markovc = js.load(open(config["markovt"]))
			self.markov_last = [0 for p in range(self.parts_count)]
			self.markov = Markovt(markovc)
		self.build_counterpoint()

	#Building initial counterpoint...
	def build_counterpoint(self):
		for i in range(self.cycles):
			self.add_cycle()

	#Adding a counterpoint cycle based on configuration...
	def add_cycle(self):
		if self.mode == "random":
			self.add_random_cycle()
		elif self.mode == "control":
			self.add_control_cycle()
		elif self.mode == "conditional":
			self.add_conditional_cycle()
		elif self.mode == "markov":
			self.markov_last = [self.markov.first_note for n in self.markov_last]
			self.add_markov_cycle()

	#Functions to create random counterpoint...
	def add_random_cycle(self):
		for r in range(self.parts_count):
			self.parts[r].append(self.random_measure(r))

	#Creating a random measure...
	def random_measure(self, part):
		measure = []
		ps = rd.sample(range(1, self.t_set), self.get_measure_cardinality())
		ps.sort()
		ps.insert(0,0)
		ps.append(self.t_set)
		for i in range(len(ps)-1):
			duration = self.t_unit * (ps[i+1] - ps[i])
			pitch = rd.randint(0,11) + self.midi_offset + self.voice_offset * part
			measure.append(self.create_note(pitch, duration))
		return measure

	#Functions to create random counterpoint...
	def add_control_cycle(self):
		for r in range(self.parts_count):
			self.parts[r].append(self.control_measure(r))

	#Creating a random measure...
	def control_measure(self, part):
		measure = []
		ps = rd.sample(range(1, self.t_set), self.get_measure_cardinality())
		ps.sort()
		ps.insert(0,0)
		ps.append(self.t_set)
		for i in range(len(ps)-1):
			duration = self.t_unit * (ps[i+1] - ps[i])
			pitch = rd.choice(self.control_list) + self.midi_offset + self.voice_offset * part
			measure.append(self.create_note(pitch, duration))
		return measure

	#Functions to create conditional counterpoint...
	def add_conditional_cycle(self):
		for r in range(self.parts_count):
			self.parts[r].append(self.conditional_measure(r))

	#Creating a conditional measure...
	def conditional_measure(self, part):
		measure = []
		ps = rd.sample(range(1, self.t_set), self.get_measure_cardinality())
		ps.sort()
		ps.insert(0,0)
		ps.append(self.t_set)
		for i in range(len(ps)-1):
			diff = ps[i+1] - ps[i]
			duration = self.t_unit * diff
			pitch = self.duration_to_pitch(diff) + self.midi_offset + self.voice_offset * part
			measure.append(self.create_note(pitch, duration))
		return measure

	def duration_to_pitch(self, diff):
		return 12 - round(diff * 12 / self.t_set)

	#Functions to create conditional counterpoint...
	def add_markov_cycle(self):
		for r in range(self.parts_count):
			self.parts[r].append(self.markov_measure(r))

	def markov_measure(self, part):
		measure = []
		ps = rd.sample(range(1, self.t_set), self.get_measure_cardinality())
		ps.sort()
		ps.insert(0,0)
		ps.append(self.t_set)
		for i in range(len(ps)-1):
			diff = ps[i+1] - ps[i]
			duration = self.t_unit * diff
			pitch_class = self.get_markov_pitch(self.markov_last[part])
			self.markov_last[part] = pitch_class
			pitch = pitch_class + self.midi_offset + self.voice_offset * part
			measure.append(self.create_note(pitch, duration))
		return measure

	def get_markov_pitch(self,input):
		r = rd.random()
		p = 0
		while self.markov.data[input][p] < r:
			p += 1
		return p

	#Printing counterpoint information...
	def __str__(self):
		return "-- Hi, I am a random Counterpoint" + "\n" \
				+ "-- I have " + str(len(self.parts)) + " parts" + "\n" \
				+ "-- And " + self.get_notes_count() + " notes" + "\n" \
				+ "-- I think there is a chance you like me..."

	def get_control_list(self, list):
		l = list.split(",")
		values = []
		for v in l:
			values.append(int(v))
		return values

	def get_measure_cardinality(self):
		c = []
		c.append(rd.randint(1,self.t_set-1))
		c.append(rd.randint(1,self.t_set-1))
		return min(c)
