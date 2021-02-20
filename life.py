class Board:
	def __init__(self, pattern, underpop=2, overpop=3, repro=3):
		self.UNDERPOP = underpop
		self.OVERPOP = overpop
		self.REPRO = repro
		self.alive = self.count_living(pattern)
		if self.alive == 0:
			raise Exception("Please initialize the simulation with at least 1 living cell")
		self.board = self.__prep_board(pattern)
		self.height = len(self.board)
		self.width = len(self.board[0])
		self.change_flag = False


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
		if not self.change_flag:
			print("STABLE!")
		self.change_flag = False
		self.board = self.__prep_board(new_board)
		self.height = len(self.board)
		self.width = len(self.board[0])
		self.alive = self.count_living(new_board)


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


	def count_living(self, pattern):
		living = 0
		for row in pattern:
			living += sum(row)
		return living


	def __change_cell_state(self, cell, neighbors):
		if cell == 0:
			if neighbors == self.REPRO:
				self.change_flag = True
				return 1
		else:
			if neighbors < self.UNDERPOP or neighbors > self.OVERPOP:
				self.change_flag = True
				return 0
		return cell


	def __prep_board(self, board):
		board = self.__pad_board(board)
		board = self.__purge_deadzones(board)
		return board

	
	def __pad_board(self, board):
		longest_row = 0

		if any(self.__get_col(board, 0)):
			board = [[0] + row for row in board]
		if any(self.__get_col(board, -1)):
			board = [row + [0] for row in board]

		for row in board:
			row_len = len(row)
			if row_len > longest_row:
				longest_row = row_len

		for row in board:
			row_len = len(row)
			if row_len < longest_row:
				mult = longest_row - row_len
				row += [0 for _ in range(mult)]

		if any(board[0]):
			board.insert(0, [0 for _ in range(longest_row)])
		if any(board[-1]):
			board.append([0 for _ in range(longest_row)])

		return board


	def __purge_deadzones(self, board):
		directions = ["N", "E", "S", "W"]
		for direction in directions:
			board = self.__purge_cardinal(direction, board)
		return board


	#Takes in a matrix and removes any rows or cols such that at least two contiguous rows/cols contain
	#all zeros. Maintains the 0 pad. Direction corresponds to the direction that deadzones should be purged
	#(e.g. getting rid of right-column deadzones corresponds to direction="E").
	#NOTE: Expects that all rows are of the same length (run __pad_board() first to ensure this is true)
	def __purge_cardinal(self, direction, board):
		if direction == "N" or direction == "W":
			i = 0
			iter = 1
		else:
			i = len(board)-1 if direction == "S" else len(board[0])-1
			iter = -1

		deadzones = 0
		is_dead = True
		while is_dead:
			if direction == "N" or direction == "S":
				side = board[i]
			else:
				side = self.__get_col(board, i)
			is_dead = not any(side)
			i += iter

		if direction == "N":
			start = i - 2 if i - 2 >= 0 else 0
			board = board[start:]
		elif direction == "S":
			end = i + 3 if i + 3 <= len(board) else len(board)
			board = board[:end]
		elif direction == "W":
			start = i - 2 if i - 2 >= 0 else 0
			board = [row[start:] for row in board]
		else:
			end = end = i + 3 if i + 3 <= len(board[0]) else len(board[0])
			board = [row[:end] for row in board]

		return board


	def __get_col(self, mat, i):
		return [row[i] for row in mat]



pattern = [
	[1, 1, 1],
	[1]
]

game = Board(pattern)
print(game.alive)
print(game)

game.update()
print(game.alive)
print(game)

game.update()
print(game.alive)
print(game)

game.update()
print(game.alive)
print(game)

game.update()
print(game.alive)
print(game)