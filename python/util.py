from music21 import *

#Some useful functions

#A function to create a melody from a list
def list_stream(notes, center, duration_v):
	d = duration.Duration(duration_v)
	s = stream.Stream()
	for n in notes:
		new_note = note.Note(n + center)
		new_note.duration = d
		s.append(new_note)
	return s

#Function to create different duration values
def get_duration_values(count):
	durations_list = []
	for i in range(count):
		durations_list.append(duration.Duration((i+1)/4))
	return durations_list

#A function to create a totally random melody
def random_stream(notes_count, durations, low_limit, high_limit):
	duration_values = get_duration_values(durations)
	note_stream = stream.Stream()
	for n in range(notes_count):
		n = note.Note(random.randint(low_limit, high_limit))
		n.duration = random.choice(duration_values)
		note_stream.append(n)
	return note_stream

#A function to create a melody with a triangular distribution of pitches
def triangular_stream(notes_count, durations, low_limit, high_limit, mode_pitch):
	if low_limit < mode_pitch < high_limit:
		duration_values = get_duration_values(durations)
		note_stream = stream.Stream()
		for n in range(notes_count):
			n = note.Note(round(random.triangular(low_limit, high_limit, mode_pitch)))
			n.duration = random.choice(duration_values)
			note_stream.append(n)
		return note_stream
	else:
		print("The mode pitch is out of range!", end="\n")

#Function to create a melody with pitches in pitch_values control list
def control_stream(notes_count, durations, pitch_values):
	duration_values = get_duration_values(durations)
	note_stream = stream.Stream()
	for n in range(notes_count):
		n = note.Note(random.choice(pitch_values))
		n.duration = random.choice(duration_values)
		note_stream.append(n)
	return note_stream

#Functions to create a melody alternating pitch and duration values in a cycle
def circle_melody(note_list, duration_list):
	nc = len(note_list) #Notes count
	dc = len(duration_list) #Durations count
	notes = lowest_multiple(nc, dc) #Looking for lowest common multiple
	note_stream = stream.Stream()
	for n in range(notes):
		new_note = note.Note(note_list[n%nc]) #Adding the note
		new_note.duration = duration.Duration(duration_list[n%dc]) #Asigning the duration
		note_stream.append(new_note)
	return note_stream

def lowest_multiple(a, b):
	n = 1
	for i in range(1, b + 1, 1):
		n = a * i #Checking a multiples
		if (n%b == 0):
			break #We save the minumun which is b multiple too
	return n
