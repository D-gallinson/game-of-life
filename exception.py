class EndOfGame(Exception):
	def __init__(
		self, 
		condition: str,
		turns: int,
		final_cells: int,
		highest_living: int,
		highest_board: int,
		lowest_living: int,
		lowest_board: int
	):
		ends = {
			"stable": self.__stable,
			"dead": self.__dead,
			"turns": self.__turns,
			"unknown": self.__unknown
		}
		if condition not in ends.keys():
			self.condition = ends["unknown"]
		else:
			self.condition = ends[condition]
		self.turns = turns
		self.final_cells = final_cells
		self.highest_living = highest_living
		self.highest_board = highest_board
		self.lowest_living = lowest_living
		self.lowest_board = lowest_board

	def __str__(self):
		msg = "Game over. " + self.condition()
		return msg
		
	def __stable(self):
		msg = "Stable condition found."
		msg += self.__stats()
		return msg

	def __dead(self):
		msg = "All cells are dead."
		msg += self.__stats()
		return msg

	def __turns(self):
		msg = "Maximum number of turns reached."
		msg += self.__stats()
		return msg

	def __unknown(self):
		msg = "Error, unknown end game state (this is probably a bug)!"
		return msg

	def __stats(self):
		highest_boards = ",".join(map(str, self.highest_board))
		lowest_boards = ",".join(map(str, self.lowest_board))
		msg = (
		"\n\n---Game Statistics---\n"
		f"Number of turns: {self.turns}\n"
		f"Final living cells: {self.final_cells}\n"
		f"Highest living cells [board]: {self.highest_living} [board {highest_boards}]\n"
		f"Lowest living cells [board]: {self.lowest_living} [board {lowest_boards}]"
		)
		return msg



class InitializationError(Exception):
	def __init__(self, msg):
		self.msg = msg

	def __str__(self):
		return f"Error initializing board: {self.msg}"



class BoardStateError(Exception):
	def __init__(self, msg):
		self.msg = msg

	def __str__(self):
		return f"Error with board state: {self.msg}"