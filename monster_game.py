# monster text game

# by thomas countoures

import random

GRID_POINTS = [(0, 0), (0, 1), (0, 2), (0, 3), (0, 4), (0, 5),
			   (1, 0), (1, 1), (1, 2), (1, 3), (1, 4), (1, 5),
			   (2, 0), (2, 1), (2, 2), (2, 3), (2, 4), (2, 5),
			   (3, 0), (3, 1), (3, 2), (3, 3), (3, 4), (3, 5),
			   (4, 0), (4, 1), (4, 2), (4, 3), (4, 4), (4, 5)]

def set_player_locations():
	# set location of monster
	monster = random.choice(GRID_POINTS)

	# set location of door
	door = random.choice(GRID_POINTS)

	# set location of player
	player = random.choice(GRID_POINTS)

	# if any of these are in the same place, re-do it again
	if monster == door or player == monster or player == door:
		return set_player_locations()

	return monster, door, player


def get_available_moves(player):
	moves = ['LEFT', 'RIGHT', 'UP', 'DOWN']
	locationX, locationY = player

	if locationX == 0:
		moves.remove('UP')
	if locationX == 4:
		moves.remove('DOWN')
	if locationY == 0:
		moves.remove('LEFT')
	if locationY == 5:
		moves.remove('RIGHT')

	return moves


def move_player(direction, player):
	
	locationX, locationY = player

	if direction == 'LEFT':
		locationX -= 1
	elif direction == 'RIGHT':
		locationX += 1
	elif direction == 'UP':
		locationY += 1
	elif direction == 'DOWN':
		locationY -= 1

	player = locationX, locationY

	return player

def draw_map(grid, player):

	tile_piece = '|{}'

	for idx, cell in enumerate(grid):
		if cell == player:
			print(tile_piece.format("X"))
		else:
			print(tile_piece.format("_"))



print("Welcome to the monster game! You are trapped in a room with a monster.")
print("There is a hidden door you need to find in order to escape.")
print("Type 'LEFT', 'RIGHT', 'UP', 'DOWN' to move your character around. Press QUIT to quit.")
print("Good luck!")

while True:	
	user_input = input("> ")
	user_input = user_input.upper()

	if user_input == "QUIT":
		break
	else:
		move_player(user_input)
