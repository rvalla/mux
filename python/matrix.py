import random as rd

class Matrix():
	"A matrix to make music"

	#Building an instance of a Matrix...
	def __init__(self, config):
		self.name = config["matrix"]
		self.type = config["type"]
		self.mod = config["module"]
		self.h = config["height"]
		self.w = config["width"]
		self.max_in_cell = config["maxcell"]
		self.data = []
		self.r_status = []
		self.c_status = []
		self.build_cells(config)
		self.build_status()

	#Function to transport the matrix...
	def transport(self, t):
		for r in range(self.h):
			for c in range(self.w):
				for v in range(len(self.data[r][c])):
					self.data[r][c][v] = (self.data[r][c][v] + t) % self.mod

	#Function to transport the matrix...
	def invert(self):
		for r in range(self.h):
			for c in range(self.w):
				for v in range(len(self.data[r][c])):
					self.data[r][c][v] = -(self.data[r][c][v]) % self.mod

	#Functions to change matrix status (order of rows and columns)
	def shuffle_status(self):
		self.shuffle_rows()
		self.shuffle_columns()

	def shuffle_rows(self):
		rd.shuffle(self.r_status)

	def shuffle_columns(self):
		rd.shuffle(self.c_status)

	#Printing matrix information...
	def __str__(self):
		return "-- Hi, I am a matrix to make music" + "\n" \
				+ "-- I have " + str(self.w) + " columns" + "\n" \
				+ "-- And " + str(self.h) + " rows" + "\n" \
				+ "-- I think I could sound perfectly." + "\n" \
				+ "-- My current status is: " + str(self.r_status) + ", " + str(self.c_status)

	#Function to print the matrix...
	def print_matrix(self):
		for r in range(self.h):
			row = "|    "
			for c in range(self.w):
				row += self.cell_text(self.data[self.r_status[r]][self.c_status[c]])
				row += "\t"
				row += "|"
				row += "    "
			print(row, end="\n")

	#Trying to print cells content...
	def cell_text(self, cell):
		c_size = len(cell)
		c_max = self.max_in_cell
		c_text = ""
		if c_size == 0:
			for l in range(c_max * 2):
				c_text += " "
		else:
			for l in range(c_max):
				if l < c_size:
					c_text += str(cell[l])
					c_text += " "
				else:
					c_text += " "
		return c_text

	#Function to build the status (order of rows and columns)
	def build_status(self):
		for r in range(self.h):
			self.r_status.append(r)
		for c in range(self.w):
			self.c_status.append(c)

	#Function to build the cells of the matrix...
	def build_cells(self, config):
		for r in range(self.h):
			row = []
			for c in range(self.w):
				row.append(self.get_values(config[str(r) + "," + str(c)]))
			self.data.append(row)

	def get_values(self, vector):
		values = []
		for v in range(len(vector)):
			n = int(vector[v])
			if n == 1:
				values.append(v)
		return values

	#Function to get information in a cell...
	def get_cell(self, r, c):
		rd.shuffle(self.data[self.r_status[r]][self.c_status[c]])
		return self.data[self.r_status[r]][self.c_status[c]]
