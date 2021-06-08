import json as js
from texture import Texture
from matrix import Matrix

config_file = js.load(open("config/cycle013527_3_matrix.json"))
m = Matrix(config_file)
m.print_matrix()
print()

config_file = js.load(open("config/chain013469swap_matrix.json"))
m = Matrix(config_file)
m.print_matrix()
