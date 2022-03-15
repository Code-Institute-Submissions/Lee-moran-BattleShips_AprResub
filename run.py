from random import randint

# LEGEND
#  X for placing ship and hitting of battleship
# ' ' for available space
# '-' for missed shots

# Board for holding ship locations
HIDDEN_BOARD = [[" "] * 9 for x in range(9)]
# Board for displaying hits and misses
GUESS_BOARD = [[" "] * 9 for i in range(9)]

letters_to_numbers = {
    'A': 0,
    'B': 1,
    'C': 2,
    'D': 3,
    'E': 4,
    'F': 5,
    'G': 6,
    'H': 7,
    'I': 8
}


def print_board(board):
    print('  A B C D E F G H I')
    print('  +-+-+-+-+-+-+-+-+')
    row_number = 1
    for row in board:
        print("%d|%s|" % (row_number, "|".join(row)))
        row_number += 1


def create_ships(board):
    """
    Playing against the computer - comp creates 6 ships
    """
    for ship in range(6):
        ship_row, ship_column = randint(0, 8), randint(0, 8)
        while board[ship_row][ship_column] == "X":
            ship_row, ship_column = get_ship_location()
        board[ship_row][ship_column] = "X"


def get_ship_location():
    row = input("\nEnter the row of the ship: ").upper()
    while row not in "123456789":
        print('Not an appropriate choice, please select a valid row')
        row = input("Please enter ship row from 1-9: ").upper()
    column = input("Enter a ship column: ").upper()
    while column not in "ABCDEFGHI":
        print('Not an appropriate choice, please enter a valid column')
        column = input("Please Enter a ship column of A-I: ").upper()
    return int(row) - 1, letters_to_numbers[column]


def count_hit_ships(board):
    """
    Counts the amount of ships that have been hit
    A hit Ship will be identifyed By an X.
    """
    count = 0
    for row in board:
        for column in row:
            if column == "X":
                count += 1
    return count


create_ships(HIDDEN_BOARD)
turns = 20
while turns > 0:
    '''
    We have 20 turns to find 6 ships..
    A HIT will identify as an X
    A Miss will identify as an -
    '''
    print("""/ 
   ___       _   _   _           _     _         
  / __\ __ _| |_| |_| | ___  ___| |__ (_)_ __    
 /__\/// _` | __| __| |/ _ \/ __| '_ \| | '_ \   
/ \/  \ (_| | |_| |_| |  __/\__ \ | | | | |_) |  
\_____/\__,_|\__|\__|_|\___||___/_| |_|_| .__/   
                                        |_|      
  ___   ___  _           _               _       
 ( _ ) / _ \( )__    ___| | __ _ ___ ___(_) ___  
 / _ \| | | |/ __|  / __| |/ _` / __/ __| |/ __| 
| (_) | |_| |\__ \ | (__| | (_| \__ \__ \ | (__  
 \___/ \___/ |___/  \___|_|\__,_|___/___/_|\___| 
                                                 
""")
    print("Object of the game is to sink 6 ships with 20 bullets\n")
    print("Legend:")
    print(" X for sucessful hit of battleship")
    print("' ' for available space (water)")
    print("'-' for missed shots\n")
    print_board(GUESS_BOARD)
    row, column = get_ship_location()
    if GUESS_BOARD[row][column] == '-':
        print("You already guessed that")
    elif HIDDEN_BOARD[row][column] == 'X':
        print("HIT")
        GUESS_BOARD[row][column] = "X"
        turns -= 1
    else:
        print("MISS!")
        GUESS_BOARD[row][column] = "-"
        turns -= 1
    if count_hit_ships(GUESS_BOARD) == 6:
        print("You WIN!")
        break
    print("You have " + str(turns) + " turns left")
    if turns == 0:
        print("You ran out of bullets")
        break