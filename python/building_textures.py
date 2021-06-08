import json as js
from texture import Texture

config_files = [js.load(open("config/chain013569_texture.json")),
				js.load(open("config/chain013569s_texture.json")),
				js.load(open("config/chain023568i_texture.json")),
				js.load(open("config/cycle013527_texture.json")),
				js.load(open("config/cycle0682410_texture.json"))]

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
		t.save_score("xml/", filename, "xml")
