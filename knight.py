import time

#                   x, y
possible_movements = [
[ 1,  2],
[ 2,  1],
[ 2, -1],
[ 1, -2],
[-1,  2],
[-1, -2],
[-2,  1],
[-2, -1],
]

def knight_tour(table, solution_vector=[], start=[0, 0]):

	if all_squares_visited(solution_vector):
		return True

	for mov in possible_movements:
		new_pos = [x + y for x, y in zip(start, mov)]


		if is_valid(table, new_pos):
			table[new_pos[1]][new_pos[0]] = len(solution_vector)+1
			solution_vector.append(new_pos)
			if knight_tour(table, solution_vector, new_pos):
				return True
				

			table[new_pos[1]][new_pos[0]] = 0
			solution_vector.pop()

	return False

def all_squares_visited(solution_vector):
	return len(solution_vector)>=63

def is_valid(table, position):
	return position[0] >= 0 and position[1] >= 0 and position[1] <= len(table)-1 and position[0] <= len(table[0])-1 and table[position[1]][position[0]] == 0

def print_table(table):
	for row in table:
		print(row)

if __name__ == '__main__':
	square_size = 8
	table = [[0 for _ in range(square_size)] for _ in range(square_size)]
	if knight_tour(table):
		print_table(table)
	else:
		print("No solutions")

"""
[ 0, 55, 46, 59, 42, 25,  8, 21]
[47, 60, 43, 56, 45, 22, 27, 24]
[54,  1, 58, 41, 26,  9, 20,  7]
[61, 48, 39, 44, 57, 28, 23, 10]
[38, 53,  2, 49, 40, 19,  6, 17]
[33, 62, 31, 36, 29, 16, 11, 14]
[52, 37, 34,  3, 50, 13, 18,  5]
[63, 32, 51, 30, 35,  4, 15, 12]
"""
