movements = [[0, 1],[1, 0], [0, -1], [-1, 0]]

def rat_in_a_maze(maze, destination, position=[0, 0]):
	if position == destination:
		return True

	for movement in movements:
		new_pos = [x + y for x, y in zip(position, movement)]

		if is_valid(maze, new_pos):
			maze[new_pos[1]][new_pos[0]] = 'r'
			if rat_in_a_maze(maze, destination, new_pos):
				return True

			table[new_pos[1]][new_pos[0]] = 0

	return False


def is_valid(table, position):
	return position[0] >= 0 and position[1] >= 0 and position[1] <= len(table)-1 and position[0] <= len(table[0])-1 and table[position[1]][position[0]] == 0


def print_table(table):
	for row in table:
		print(row)

if __name__ == '__main__':
	square_size = 5
	table = [[0 for _ in range(square_size)] for _ in range(square_size)]
	table[0][1] = 1
	table[0][2] = 1
	table[1][2] = 1
	table[1][4] = 1
	table[2][4] = 1
	table[3][4] = 1
	table[3][1] = 1
	table[3][2] = 1
	table[3][3] = 1
	table[4][1] = 1
	table[4][2] = 1
	table[4][3] = 1
	table[4][4] = 1


	if rat_in_a_maze(table, [0, 4]):
		print_table(table)
	else:
		print("no solution")
