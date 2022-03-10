#LEGEND
# X for placing ship and hitting of battleship
# '' for available space
# '_' for missed shots
#
#


from random import randint

#Board for holding ship locations
HIDDEN_BOARD = [[" "] * 12 for x in range(12)]
# Board for displaying hits and misses
GUESS_BOARD = [[" "] * 12 for i in range(12)]

letters_to_numbers = {
    'A': 0,
    'B': 1,
    'C': 2,
    'D': 3,
    'E': 4,
    'F': 5,
    'G': 6,
    'H': 7,
    'I': 8,
    'J': 9,
    'K': 10,
    'L': 11  
}

def print_board(board):
    print('    A B C D E F G H I J K L')
    print('    +-+-+-+-+-+-+-+-+-+-+-+')
    row_number = 1
    for row in board:
        print("%d|%s|" % (row_number, "|".join(row)))
        row_number += 1

def create_ships(board):
    """
    Playing against the computer - creates 5 ships
    """
    for ship in range(5):
        ship_row, ship_column = randint(0, 11), randint(0, 11)
        while board[ship_row][ship_column] = "X":
            ship_row, ship_column = randint(0, 11), randint(0, 11)
        board[ship_row][ship_column] = 'X'

def get_ship_location():
    pass

def count_hit_ships():
    pass

create_ships()
turns = 10 
while turns > 0: