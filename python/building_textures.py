import json as js
from texture import Texture

#Example code to use matrix object to create a musical texture...
config_files = [js.load(open("config/chain013469_texture.json"))]

for c in config_files:
	for i in range(3):
		t = Texture(c)
		t.matrix.shuffle_status()
		t.matrix.translation(3)
		t.add_cycle()
		t.matrix.shuffle_status()
		t.matrix.translation(3)
		t.add_cycle()
		t.matrix.shuffle_status()
		t.matrix.translation(3)
		t.add_cycle()
		filename = c["texture"] + str(i + 3) + ".xml"
		#t.save_score("xml/", filename, "xml")
		t.show_score()
