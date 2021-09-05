from music21 import *
import json as js
import random as rd
import util as ut
from scores import m21Score

class Counterpoint(m21Score):
	"A machine to make a random couterpoint"

	#Building an instance of a Counterpoint..
	def __init__(self, config):
		m21Score.__init__(self, config["title"], config["composer"], config["key_signature"],
							config["time_signature"], config["parts"])
		self.cycles = config["cycles"] #Number of cycles
		self.mode = config["mode"] #Texture mode: random, control, markov, bidimensional
		self.control_list = self.get_control_list(config["control"])
		self.t_unit = config["time_unit"]
		self.t_measure = config["time_measure"]
		self.t_set = int(self.t_measure / self.t_unit)
		self.midi_offset = config["midi_offset"]
		self.voice_offset = config["voice_offset"]
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
		elif self.mode == "bidimensional":
			self.add_bidimensional_cycle()

	#Functions to create random counterpoint...
	def add_random_cycle(self):
		for r in range(self.parts_count):
			self.parts[r].append(self.random_measure(r))

	#Creating a random measure...
	def random_measure(self, part):
		measure = []
		aux = []
		aux.append(rd.randint(1,self.t_set-1))
		aux.append(rd.randint(1,self.t_set-1))
		ps = rd.sample(range(1, self.t_set), min(aux))
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
		aux = []
		aux.append(rd.randint(1,self.t_set-1))
		aux.append(rd.randint(1,self.t_set-1))
		ps = rd.sample(range(1, self.t_set), min(aux))
		ps.sort()
		ps.insert(0,0)
		ps.append(self.t_set)
		for i in range(len(ps)-1):
			duration = self.t_unit * (ps[i+1] - ps[i])
			pitch = rd.choice(self.control_list) + self.midi_offset + self.voice_offset * part
			measure.append(self.create_note(pitch, duration))
		return measure

	#Functions to create bidimensional counterpoint...
	def add_bidimensional_cycle(self):
		for r in range(self.parts_count):
			self.parts[r].append(self.bidimensional_measure(r))

	#Creating a bidimensional measure...
	def bidimensional_measure(self, part):
		measure = []
		aux = []
		aux.append(rd.randint(1,self.t_set-1))
		aux.append(rd.randint(1,self.t_set-1))
		ps = rd.sample(range(1, self.t_set), min(aux))
		ps.sort()
		ps.insert(0,0)
		ps.append(self.t_set)
		for i in range(len(ps)-1):
			duration = self.t_unit * (ps[i+1] - ps[i])
			pitch = duration + self.midi_offset + self.voice_offset * part
			measure.append(self.create_note(pitch, duration))
		return measure

	def get_control_list(self, list):
		l = list.split(",")
		values = []
		for v in l:
			values.append(int(v))
		return values

	#Printing counterpoint information...
	def __str__(self):
		return "-- Hi, I am a random Counterpoint" + "\n" \
				+ "-- I have " + str(len(self.parts)) + " parts" + "\n" \
				+ "-- And " + self.get_notes_count() + " notes" + "\n" \
				+ "-- I think there is a chance you like me..."
