import warnings
from ligeti import LigetiStorm
import json as js

warnings.filterwarnings("ignore")

config = js.load(open("config/test_ligeti.json"))

storm = LigetiStorm(config)

#Showing the score...
#storm.show_score()

#Saving a file...
filename = config["output"] + ".xml"
storm.save_score("xml/", filename, "xml")
