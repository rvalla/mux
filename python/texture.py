from music21 import *
import json as js
import random as rd
from scores import m21Score
from matrix import Matrix

class Texture(m21Score):
	"A machine to make a musical texture using a matrix"

	#Building an instance of a Texture..
	def __init__(self, config):
		m21Score.__init__(self, config["title"], config["composer"], config["key_signature"],
							config["time_signature"], config["parts"])
		self.matrix = Matrix(js.load(open(config["matrix_file"])))
		self.cycles = config["cycles"] #Number of cycles
		self.mode = config["mode"] #Texture mode: puntual, filled, mobile
		self.t_unit = config["time_unit"]
		self.t_measure = config["time_measure"]
		self.t_set = int(self.t_measure / self.t_unit)
		self.midi_offset = config["midi_offset"]
		self.voice_offset = config["voice_offset"]
		self.build_texture()

	#Building initial texture...
	def build_texture(self):
		for i in range(self.cycles):
			self.add_cycle()

	#Adding a texture cycle based on matrix...
	def add_cycle(self):
		if self.mode == "puntual":
			self.add_puntual_matrix()
		elif self.mode == "filled":
			self.add_filled_matrix()
		elif self.mode == "mobile":
			self.add_mobile_matrix()

	#Functions to create puntual texture...
	def add_puntual_matrix(self):
		h = self.matrix.h
		w = self.matrix.w
		for r in range(h):
			for c in range(w):
				self.parts[r].append(self.puntual_measure(self.matrix.get_cell(r, c), r))

	#Creating a puntual texture measure...
	def puntual_measure(self, cell, part):
		measure = []
		c = len(cell)
		if c > 0:
			ps = rd.sample(range(0, self.t_set), c)
			ps.sort()
			cp = 0
			for i in range(self.t_set):
				if ps[cp] == i:
					pitch = cell[cp] + self.midi_offset + self.voice_offset * part
					measure.append(self.create_note(pitch, self.t_unit))
					if cp < c - 1:
						cp += 1
				else:
					measure.append(self.create_note(-1, self.t_unit))
		else:
			measure.append(self.create_note(-1, self.t_measure))
		return measure

	#Functions to create filled texture...
	def add_filled_matrix(self):
		h = self.matrix.h
		w = self.matrix.w
		for r in range(h):
			for c in range(w):
				self.parts[r].append(self.filled_measure(self.matrix.get_cell(r, c), r))

	#Creating a filled texture measure...
	def filled_measure(self, cell, part):
		measure = []
		c = len(cell)
		if c > 0:
			ps = rd.sample(range(1, self.t_set), c - 1)
			ps.sort()
			ps.insert(0,0)
			ps.append(self.t_set)
			for i in range(c):
				duration = self.t_unit * (ps[i+1] - ps[i])
				pitch = cell[i] + self.midi_offset + self.voice_offset * part
				measure.append(self.create_note(pitch, duration))
		else:
			measure.append(self.create_note(-1, self.t_measure))
		return measure

	#Functions to create mobile texture...
	def add_mobile_matrix(self):
		h = self.matrix.h
		w = self.matrix.w
		for r in range(h):
			for c in range(w):
				self.parts[r].append(self.mobile_measure(self.matrix.get_cell(r, c), r))

	#Creating a mobile texture measure...
	def mobile_measure(self, cell, part):
		measure = []
		c = len(cell)
		if c > 0:
			for i in range(self.t_set):
				pitch = cell[i%c] + self.midi_offset + self.voice_offset * part
				measure.append(self.create_note(pitch, self.t_unit))
		else:
			measure.append(self.create_note(-1, self.t_measure))
		return measure

	#Printing texture information...
	def __str__(self):
		return "-- Hi, I am a Texture made with a matrix" + "\n" \
				+ "-- I have " + str(len(self.parts)) + " parts" + "\n" \
				+ "-- And " + self.get_notes_count() + " notes" + "\n" \
				+ "-- I think I sound consistent."
