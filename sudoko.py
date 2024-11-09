from random import randint
from math import ceil

def display(grid):
	size = len(grid)  
	hr_line = "---"*((size*2)-2)
	print(hr_line)
	for row in range(size):
		for col in range(size):
			print(f"| {grid[row][col]} ", end='')
		print("|")
		print(hr_line)
	
	'''
	size = len(grid)
	hr_line = "-----"*size
	print(hr_line)
	for r in range(size):
		fs = '{ }|' * size
		fs = '|'+ fs
		print(fs.format(*[r]))
		print(hr_line)
	'''

def fill_grid(size):
	sudoku_state = [list(' '*size) for _ in range(size)]
	possibility = set(range(1,size+1))
	
	for row in range(size):
		for col in range(size):
			availability = set(sudoku_state[row] +[ r[col] for r in sudoku_state])
			candidates = list(possibility - availability)
			
			if candidates:
				sudoku_state[row][col] = candidates[randint(0,len(candidates)-1)]
			else:
				return fill_grid(size)
	
	return sudoku_state


def initialize():
	print("Welcome the Sudoku !!")
	
	size = int(input("Enter the grid size : "))
	
	#sudoku_state = [list(' '*size) for _ in range(size)]
	#sudoku_state[0][1] = 1
	#udoku_state[0][2] = 2
	state = fill_grid(size)
	
	game_levels = {1 : ('Very Easy',20),2 : ('Easy',30),3 : ('Medium',50),4 : ('Hard',60),5 : ('Very Hard',75)}
	
	print(f"There are {len(game_levels)} levels")
	
	for level, info in game_levels.items():
		print(f"Level{level}:{info[0]}")
	
	difficulty_level = int(input("Enter game level (1-5): "))
	hidden_fields = ceil(game_levels[difficulty_level][1] * size / 100)
    
	positions = []
	p = list(range(size*size))

	for _ in range(hidden_fields):
		popped = p.pop(randint(0,len(p)-1))
		positions.append((popped//size,popped%size))
	
	
	for row,col in positions:
		state[row][col] = "X"
	#display(state)

	return state,positions


def start_game(ss,positions):
	display(ss)
	for r,c in positions:
		ss[r][c] = int(input(f"Enter a value for row {r+1}, col {c+1}: "))




def is_valid_solution(grid):
	size = len(grid)
	possibility = set(range(1, size+1))
    
    # Check rows
	for row in grid:
		if set(row) != possibility:
			return False
    
    # Check columns
	for col in range(size):
		column_values = [grid[row][col] for row in range(size)]
		if set(column_values) != possibility:
			return False
    
	return True

def stop_game(ss):
	print("Your solution is given below : ")
	display(ss)
	
	if is_valid_solution(ss):
		print("Congratulations, you won!")
	else:
		print("Sorry, your solution is incorrect.")


def sudoku():
	sudoku_state , positions = initialize()
	start_game(sudoku_state,positions)#Grid position 
	stop_game(sudoku_state)
	
	#develop logic for stop_game that means winning logic which means check for the unique elements in each rows and cols
	
sudoku()

