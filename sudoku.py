from functools import reduce
from datetime import datetime
# A Backtracking program in Python to solve Sudoku problem 

class Sudoku:
	def __init__(self, grid):
		super().__init__()
		self._grid = grid
		self.iteration = 0
# Function to Find the entry in the Grid that is still not used 
# Searches the grid to find an entry that is still unassigned. If 
# found, the reference parameters row, col will be set the location 
# that is unassigned, and true is returned. If no unassigned entries 
# remain, false is returned. 
# 'l' is a list variable that has been passed from the solve_sudoku function 
# to keep track of incrementation of Rows and Columns 
	def find_empty_location(self,l): 
		for row in range(9): 
			for col in range(9): 
				if(self._grid[row][col]==0): 
					l[0]=row 
					l[1]=col 
					return True
		return False

	def __str__(self):
		return reduce(lambda x, y: str(x) + "\n" + str(y), self._grid)


# Checks whether it will be legal to assign num to the given row,col 
# Returns a boolean which indicates whether it will be legal to assign 
# num to the given row,col location. 
	def location_is_safe(self, row, col, num): 
		
		# Check if 'num' is not already placed in current row, 
		# current column and current 3x3 box 
		return not (self.used_in_row(row, num) or self.used_in_col(col, num) or self.used_in_box(row - row%3, col - col%3, num))

# Returns a boolean which indicates whether any assigned entry 
# in the specified row matches the given number. 
	def used_in_row(self, row, num): 
		for i in range(9): 
			if self.get(row, i) == num: 
				return True
		return False

# Returns a boolean which indicates whether any assigned entry 
# in the specified column matches the given number. 
	def used_in_col(self, col, num): 
		for i in range(9): 
			if self.get(i, col) == num:
				return True
		return False

# Returns a boolean which indicates whether any assigned entry 
# within the specified 3x3 box matches the given number 
	def used_in_box(self, row, col, num): 
		for y in range(3): 
			for x in range(3): 
				if self.get(y+row, x+col) == num: 
					return True
		return False

	def get(self, row, col):
		return self._grid[row][col]

	def set(self, row, col, num):
		self._grid[row][col] = num


# Takes a partially filled-in grid and attempts to assign values to 
# all unassigned locations in such a way to meet the requirements 
# for Sudoku solution (non-duplication across rows, columns, and boxes) 
def solve_sudoku(sudoku): 
	
	# 'l' is a list variable that keeps the record of row and col in find_empty_location Function	 
	l=[0,0] 
	
	# If there is no unassigned location, we are done	 
	if(not sudoku.find_empty_location(l)): 
		return True
	
	# Assigning list values to row and col that we got from the above Function 
	row=l[0] 
	col=l[1] 
	
	# consider digits 1 to 9 
	for num in range(1, 10): 
		
		# if looks promising 
		if(sudoku.location_is_safe(row, col, num)): 
			
			# make tentative assignment 
			sudoku.set(row, col, num)

			# return, if sucess, ya! 
			if(solve_sudoku(sudoku)): 
				return True
			# failure, unmake & try again 
			sudoku.set(row, col, 0)
			print(sudoku)
			print('')
			sudoku.iteration += 1
			
	# this triggers backtracking		 
	return False

# Driver main function to test above functions 
if __name__=="__main__": 
	
	# assigning values to the grid 
	grid=[[5,0,0,4,0,0,0,0,0], 
	      [0,0,0,0,0,9,0,1,2], 
	      [9,8,6,1,0,0,0,0,0], 
	      [0,0,0,0,2,6,1,0,0], 
	      [0,0,9,0,0,0,7,0,0], 
	      [0,0,8,3,7,0,0,0,0], 
	      [0,0,0,0,0,4,2,8,3], 
	      [1,4,0,2,0,0,0,0,0], 
	      [0,0,0,0,0,5,0,0,1]] 
	sudoku = Sudoku(grid)

	start = datetime.now()
	# if sucess print the grid 
	if(solve_sudoku(sudoku)): 
		end = datetime.now()
		print(sudoku) 
		print('')
		print('Tiempo transcurrido: ' + str(end-start))
		print('Intentos: ' + str(sudoku.iteration))
	else: 
		print ("No solution exists")

# The above code has been contributed by Harshit Sidhwa. 
