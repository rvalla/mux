import warnings
from ligeti import LigetiStorm

warnings.filterwarnings("ignore")

#Testing Ligeti's storms
title = "Storm canon"
composer = "Unkown machine"

#Defining the motif
pitches = [72, 73, 70, 65, 67, 76, 77, 78]
durations = [0.125, 0.25, 0.125, 0.25, 0.5, 0.125, 0.125, 0.5]

storm = LigetiStorm(title, composer, 0, "3/4", 19, 5, 0, 0.25, -3, pitches, durations)

#Showing the score...
storm.show_score()

#Saving a file...
storm.save_score("xml/", "s_test.xml", "xml")
