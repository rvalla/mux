from music21 import *
from scores import m21Score

class LigetiStorm(m21Score):
	"A machine to make a Ligeti's storm"

	def __init__(self, config):
		m21Score.__init__(self, config["title"], config["composer"], config["key"], config["time_s"], config["parts"])
		self.notes = self.build_motif(self.get_list(config["pitches"], "int"), self.get_list(config["durations"], "float"))
		self.cycles = config["cycles"] #Number of cycles
		self.part_off = config["part_offset"]
		self.t_off = config["t_offset"] #The offset for each voice in the canon
		self.p_off = config["p_offset"] #Interval distance for the canon
		self.build_storm(self.t_off, self.p_off, self.cycles, self.part_off)
		print(self)

	def __str__(self):
		return "-- Hi, I am a Ligeti storm" + "\n" \
				+ "-- I have " + str(len(self.parts)) + " parts" + "\n" \
				+ "-- And " + self.get_notes_count() + " notes" + "\n" \
				+ "-- I think I sound difuse."

	#A little motif to begin with
	def build_motif(self, pitches, durations):
		notes = []
		for p, d in zip(pitches, durations):
			notes.append(self.create_note(p, d))
		return notes

	#A canon storm
	def build_storm(self, t_offset, p_offset, cycles, part_offset):
		for p in range(len(self.parts)):
			target = (p + part_offset)%self.parts_count
			if target != part_offset:
				self.parts[target].append(self.get_time_offset(p * t_offset))
			for c in range(cycles):
				self.add_motif_to_part(target, p_offset)

	#Adding a copy of the motif to the voice
	def add_motif_to_part(self, part, p_offset):
		for n in self.notes:
			self.parts[part].append(n.transpose(part * p_offset))

	#A function to calculate time offset for each voice
	def get_time_offset(self, distance):
		r = note.Rest()
		r.duration = duration.Duration(distance)
		return r

	#A function to create a list from configuration string
	def get_list(self, values, type):
		input = values.split(",")
		values = []
		for v in input:
			if type == "int":
				values.append(int(v))
			elif type == "float":
				values.append(float(v))
		return values
