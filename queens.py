def nqueen(n, table, queens=[]):
	if n == len(queens):
		return True


	for row in range(len(table)):
		for col in range(len(table[row])):
			if can_assign_queen(table, row, col, queens):
				table[row][col] = 1
				queens.append([row, col])
				if nqueen(n, table, queens):
					return True

				queens.pop()
				table[row][col] = 0
	return False


def can_assign_queen(table, row, col, queens):
	return no_queens_on_row(queens, row) and no_queens_on_col(queens, col) and no_queens_on_diagonal(queens, row, col)

def no_queens_on_row(queens, row):
	return no_queens_on(queens, row, 0)

def no_queens_on_col(queens, col):
	return no_queens_on(queens, col, 1)

def no_queens_on(queens, value, index):
	return len(list(filter(lambda queen: queen[index] == value, queens)))==0

def no_queens_on_diagonal(queens, row, col):
	return len(list(filter(lambda queen: abs(queen[0]-row) == abs(queen[1]-col), queens)))==0
	
if __name__ == '__main__':
	square_size = 4
	table = [[0 for _ in range(square_size)] for _ in range(square_size)]

	if nqueen(square_size, table):
		for row in table:
			print(row)
	else:
		print("NO SOLUTION")
