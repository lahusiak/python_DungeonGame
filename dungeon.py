import random
import sys
import os

# CELLS = [(0,0), (0,1), (0,2),
#         (1,0), (1,1), (1,2),
#         (2,0), (2,1), (2,2)]

def clear():
    """Clear the screen"""
    os.system('cls' if os.name == 'not' else 'clear')

def build_cells(width, height):
    """Create and return a width x heigh grid of two-tuples

    >>> cells = build_cells(2,2)
    >>> len(cells)
    4

    """
    cells = []
    for y in range(height):
        for x in range(width):
            cells.append((x, y))
    return cells

def get_locations(cells):
    """Randomly pick starting locations for the monster, the door and the player

    >>> cells = build_cells(2, 2)
    >>> m, d, p = get_locations(cells)
    >>> m != d and d != p
    True
    >>> d in cells
    True

    """
    monster = random.choice(cells)
    door = random.choice(cells)
    player = random.choice(cells)
    #if monster, door, or player are the same, do it again
    if monster == door or monster == player or door == player:
        return get_locations(cells)
    return monster, door, player

def move_player(player, move):
    #Get the player's current location
    x, y = player

    if move == 'LEFT':
        y -= 1
    elif move == 'RIGHT':
        y += 1
    elif move == 'UP':
        x -= 1
    elif move == 'DOWN':
        x += 1
    return x, y

def get_moves(player):
    """Based on the tuple of the player's postion, return the list
    of acceptabel moves

    >>> GAME_DIMENSIONS = (2, 2)
    >>> get_moves((0, 2))
    ['LEFT', 'DOWN']

    """
    moves = ['LEFT', 'RIGHT', 'UP', 'DOWN']
    if player[1] == 0:
        moves.remove('LEFT')
    if player[1] == 2:
        moves.remove('RIGHT')
    if player[0] == 0:
        moves.remove('UP')
    if player[0] == 2:
        moves.remove('DOWN')
    return moves

# def draw_map(player):
#     print(' _ _ _ ')
#     tile = '|{}'
#
#     for idx, cell in enumerate(CELLS):
#         if idx in [0, 1, 3, 4, 6, 7]:
#             if cell == player:
#                 print tile.format('X') ,
#             else:
#                 print tile.format('_') ,
#         else:
#             if cell == player:
#                 print tile.format('X|'),
#             else:
#                 print tile.format('_|')
#
#
# monster, door, player = get_locations(cells)
# print("Welcome to the dungeon!")
#
# while True:
#     moves = get_moves(player)
#     print("You're currently in the {}".format(player)) #fill in with player position
#
#     draw_map(player)
#
#     print("You can move {}".format(moves))
#     print("Enter QUIT to quit")
#
#     move = raw_input('> ')
#     move = move.upper()
#     print(move)
#
#     if move == 'QUIT':
#         break
#     if move in moves:
#         player = move_player(player, move)
#     else:
#         print("Walls are hard, stop walking into them")
#         continue
#     if player == door:
#         print("You escaped!")
#     elif player == monster:
#         print("You were eaten by the monster")
#         break
#     #If
