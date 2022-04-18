from random import randint

# LEGEND
#  X for placing ship and hitting of battleship
# | | for available space
# '-' for missed shots

# Board for holding ship locations
HIDDEN_BOARD = [[" "] * 9 for x in range(9)]
# Board for displaying hits and misses
GUESS_BOARD = [[" "] * 9 for i in range(9)]

SHIP = [2, 3, 4, 5, 6]

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
    print('\u001B[32m  A B C D E F G H I \u001B[0m')
    print('  +-+-+-+-+-+-+-+-+')
    row_number = 1
    for row in board:
        print("%d|%s|" % (row_number, "|".join(row)))
        row_number += 1


def create_ships(board):
    """
    Playing against the computer - comp creates 9 ships
    """
    for ship in range(9):
        ship_row, ship_column = randint(0, 8), randint(0, 8)
        while board[ship_row][ship_column] == "X":
            ship_row, ship_column = get_ship_location()
        board[ship_row][ship_column] = "X"


def get_ship_location():
    while True:
        try: 
            row = input("Enter the row of the ship: ")
            if row in '123456789':
                row = int(row) - 1
                break
        except ValueError:
            print('Enter a valid letter between A-I')
    while True:
        try: 
            column = input("Enter the column of the ship: ").upper()
            if column in 'ABCDEFGHI':
                column = letters_to_numbers[column]
                break
        except KeyError:
            print('Enter a valid letter between A-I')
    return row, column


def count_hit_ships(board):
    """
    Counts the amount of ships that have been hit
    A hit Ship will be identifyed By an X.
    """
    count = 0
    for row in board:
        for column in row:
            if column == "x":
                count += 1
    return count


create_ships(HIDDEN_BOARD)
turns = 30
while turns > 0:
    '''
    We have 30 turns to find 8 ships..
    A HIT will identify as an X
    A Miss will identify as an -
    '''
    print("""/
    \u001B[32m 
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
\u001B[0m                                               
""")
    print("\033[0;95m SINK ALL 9 SHIPS USING 30 BULLETS \n \u001B[0m")
    print(" \033[0;91m X \u001B[0m   Sucessful hit of battleship")
    print(" | |   Available space (water)")
    print("\033[0;93m  - \u001B[0m   Missed shots\n")
    print_board(GUESS_BOARD)
    row, column = get_ship_location()
    if GUESS_BOARD[row][column] == '-':
        print("You already guessed that")
    elif HIDDEN_BOARD[row][column] == 'X':
        print("HIT")
        GUESS_BOARD[row][column] = "\033[0;91mX\u001B[0m"
        turns -= 1
    else:
        print("MISS!")
        GUESS_BOARD[row][column] = "\033[0;93m-\u001B[0m"
        turns -= 1
    if count_hit_ships(GUESS_BOARD) == 9:
        print("You WIN!")
        break
    print("You have " + str(turns) + " turns left")
    if turns == 0:
        print("You ran out of bullets, GAME OVER")
        break
    
