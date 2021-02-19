class Board:
	def __init__(self, pattern):
		self.board = pattern

	
	def to_cells(self, pattern):
		cell_board = []
		longest_row = 0
		longest_i = 0
		for i in range(len(pattern)):
			row = pattern[i]
			row_len = len(row)
			if row_len > longest_row:
				longest_row = row_len
				longest_i = i

		if pattern[longest_i][0] != 0:
			longest_row += 1
			pattern[longest_i].insert(0, 0)
		if pattern[longest_i][-1] != 0:
			longest_row += 1
			pattern[longest_i].append(0)

		for row in pattern:
			

	


pattern = [
	[1, 1, 1, 1],
	[1],
	[1, 1, 1, 1]
]

pattern = [1, 1, 1, 0]

tboard = Board(pattern)
tboard.to_cells(pattern)

"""
test = [
	1 1 1
	1 0 1
	1 1 1
]
"""

"""
1 1 1 1
1
1 1 1 1
"""

"""
1 1 1
0 1
1 1 1
"""

class Cell:
	def __init__(self, state, underpop=2, overpop=3, repro=3):
		self._state = state
		self._neighbors = 0
		self.UNDERPOP = underpop
		self.OVERPOP = overpop
		self.REPRO = repro

	def __str__(self):
		if self._state == 0:
			return "Dead"
		else:
			return "Alive"

	def get_state(self):
		return self._state

	def change_state(self):
		if self._state == 0:
			self._state = 1
		else:
			self._state = 0

	def get_neighbors(self):
		return self._neighbors

	def add_neighbor(self):
		self._neighbors += 1

	def reset_neighbors(self):
		self._neighbors = 0

	def update_cell(self):
		if self._state == 0:
			if self._neighbors == self.REPRO:
				self.change_state()
		else:
			if self._neighbors < self.UNDERPOP or self._neighbors > self.OVERPOP:
				self.change_state()


"""
cell = Cell(0)
print(cell)
cell.add_neighbor()
cell.add_neighbor()
cell.add_neighbor()
cell.update_cell()
print(cell)
#cell.reset_neighbors()
cell.add_neighbor()
cell.update_cell()
print(cell)
"""