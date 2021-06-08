import json as js
from texture import Texture

config_file = js.load(open("config/mobile_texture.json"))
t = Texture(config_file)
print(t)
t.show_score()
