class Board:
	def __init__(self, pattern, underpop=2, overpop=3, repro=3):
		self.UNDERPOP = underpop
		self.OVERPOP = overpop
		self.REPRO = repro
		self.alive = self.__init_living(pattern)
		if self.alive == 0:
			raise Exception("Please initialize the simulation with at least 1 living cell")
		self.board = self.__pad_board(pattern)
		self.height = len(self.board)
		self.width = len(self.board[0])


	def __str__(self):
		board = ""
		for row in self.board:
			board += " ".join(map(str, row)) + "\n"
		return board


	def update(self):
		alive = 0
		new_board = []
		for row in range(self.height):
			new_row = []
			for col in range(self.width):
				cell = self.board[row][col]
				neighbors = self.check_surroundings(row, col, cell)
				new_cell = self.__change_cell_state(cell, neighbors)
				new_row.append(new_cell)
			new_board.append(new_row)
		self.board = new_board


	def check_surroundings(self, row, col, cell):
		alive = 0
		if cell == 1:
			alive -= 1
		start_row = row - 1
		end_row = row + 2
		start_col = col - 1
		end_col = col + 2
		
		if row == 0:
			start_row += 1
		elif row == self.height-1:
			end_row -= 1
		
		if col == 0:
			start_col += 1
		elif col == self.width-1:
			end_col -= 1

		for row_i in range(start_row, end_row):
			row = self.board[row_i]
			alive += sum(row[start_col:end_col])

		return alive


	def __init_living(self, pattern):
		living = 0
		for row in pattern:
			living += sum(row)
		return living


	def __change_cell_state(self, cell, neighbors):
		if cell == 0:
			if neighbors == self.REPRO:
				return 1
		else:
			if neighbors < self.UNDERPOP or neighbors > self.OVERPOP:
				return 0
		return cell

	
	def __pad_board(self, pattern):
		longest_row = 0

		if any(self.__get_col(pattern, 0)):
			pattern = [[0] + row for row in pattern]
		if any(self.__get_col(pattern, -1)):
			pattern = [row + [0] for row in pattern]

		for row in pattern:
			row_len = len(row)
			if row_len > longest_row:
				longest_row = row_len

		for row in pattern:
			row_len = len(row)
			if row_len < longest_row:
				mult = longest_row - row_len
				row += [0 for _ in range(mult)]

		if any(pattern[0]):
			pattern.insert(0, [0 for _ in range(longest_row)])
		if any(pattern[-1]):
			pattern.append([0 for _ in range(longest_row)])

		return pattern


	def __get_col(self, mat, i):
		return [row[i] for row in mat]



pattern = [
	[1, 1, 1],
	[1]
]

game = Board(pattern)
print(game)
game.update()
print(game)
game.update()
print(game)
game.update()
print(game)